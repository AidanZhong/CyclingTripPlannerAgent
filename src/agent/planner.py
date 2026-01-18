# -*- coding: utf-8 -*-
"""
Created on 16/01/2026 22:25

@author: Aidan
@project: CyclingTripPlannerAgent
@filename: planner
"""
from src.schemas.tools import GetRouteResponse, Waypoint, GetElevationProfileRequest, GetWeatherRequest, \
    FindAccommodationRequest
from src.schemas.trip import TripPlan, TripPreferences, DayPlan
from src.tools.accommodation import find_accommodation
from src.tools.elevation import get_elevation_profile
from src.tools.weather import get_weather_data
from src.utils.path_finding import distance_between_city, get_total_elevation_gain


def build_trip_plan(preferences: TripPreferences, route_response: GetRouteResponse) -> TripPlan:
    """
    1. choose day stops from route waypoints
    2. assign per-day distances
    3. for each day: call elevation/weather/accommodation tools
    4. assemble trip plan
    """
    if not preferences.origin or not preferences.destination:
        raise ValueError("Origin and destination must be specified")
    if not preferences.daily_distance_km:
        raise ValueError("Daily distance must be specified")
    if not preferences.start_month:
        raise ValueError("Start month must be specified")
    if not preferences.accommodation or not preferences.accommodation.primary:
        raise ValueError("Accommodation must be specified")

    stops, day_distances = segment_by_daily_target(route_response.waypoints, preferences.daily_distance_km)

    day_plans = []
    total_gain = 0.0

    for day in range(1, len(stops)):
        from_wp, to_wp = stops[day - 1], stops[day]
        dist_km = day_distances[day - 1]

        elev = get_elevation_profile(GetElevationProfileRequest(
            origin=from_wp.name,
            destination=to_wp.name
        ))
        gain = elev.elevation_gain_m
        total_gain += gain

        weather = get_weather_data(GetWeatherRequest(location=to_wp.name, month=preferences.start_month))
        weather_summary = f"Avg {getattr(weather, 'avg_high_c', '?')}°C/{getattr(weather, 'avg_low_c', '?')}°C"

        stay_type = get_accommodation_type_for_specific_night(preferences, day)
        accommodation = find_accommodation(FindAccommodationRequest(near=to_wp.name, limit=3, type=stay_type))
        best = accommodation.results[0] if accommodation.results else None
        stay_summary = f"{best.name} ({best.type.value})" if best else "No accommodation found"

        day_plans.append(DayPlan(
            day=day,
            start_location=from_wp.name,
            end_location=to_wp.name,
            distance_km=dist_km,
            elevation_gain_m=gain,
            terrain_difficulty=elev.difficulty_rating,
            weather_summary=weather_summary,
            stay=stay_summary
        ))

    title = f"{preferences.origin} → {preferences.destination} ({preferences.month})"
    return TripPlan(
        title=title,
        days=day_plans,
        overall_distance_km=sum(day_distances),
        overall_elevation_gain_m=total_gain
    )


def segment_by_daily_target(waypoints: list[Waypoint], daily_distance_km):
    stops = [waypoints[0]]
    distances = []
    current = 0.0

    for i in range(1, len(waypoints)):
        a, b = waypoints[i - 1], waypoints[i]
        current += distance_between_city(a.name, b.name)

        if current >= daily_distance_km:
            # we dont take this stop
            stops.append(a)
            distances.append(current)
            current = 0.0
    if stops[-1] != waypoints[-1]:
        stops.append(waypoints[-1])
    distances.append(current)
    return stops, distances


def get_accommodation_type_for_specific_night(pref: TripPreferences, night_index):
    acc = pref.accommodation
    primary = acc.primary
    alt = acc.alt
    n = acc.alt_every_n_nights
    if alt and n and int(n) >= 2 and night_index % n == 0:
        return alt
    return primary
