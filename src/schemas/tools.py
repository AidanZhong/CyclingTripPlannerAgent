# -*- coding: utf-8 -*-
"""
Created on 16/01/2026 22:27

@author: Aidan
@project: CyclingTripPlannerAgent
@filename: tools
"""
from src.schemas.trip import AccommodationType


# -------Route--------
class GetRouteRequest:
    origin: str
    destination: str
    daily_distance_km: float


class GetRouteResponse:
    total_distance_km: float
    estimation_days: int
    waypoints: list[Waypoint]


class Waypoint:
    name: str
    lat: float | None = None
    lon: float | None = None


# -------Accommodation--------
class FindAccommodationRequest:
    near: str
    type: AccommodationType
    limit: int = 3


class AccommodationOption:
    name: str
    type: AccommodationType
    approx_price_per_night: float | None = None


class FindAccommodationResponse:
    results: list[AccommodationOption]


# -------Weather--------
class GetWeatherRequest:
    location: str
    month: str


class GetWeatherResponse:
    avg_high_temp_c: float
    avg_low_temp_c: float
    raining_days_estimate: int


# -------Elevation--------
class GetElevationProfileRequest:
    origin: str
    destination: str


class GetElevationProfileResponse:
    elevation_gain_m: float
    difficulty_rating: float
