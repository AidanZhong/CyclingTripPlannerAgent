# -*- coding: utf-8 -*-
"""
Created on 18/01/2026 22:48

@author: Aidan
@project: CyclingTripPlannerAgent
@filename: render
"""
from src.schemas.trip import TripPlan


def render_trip_plan(trip_plan: TripPlan) -> str:
    lines = []
    lines.append(trip_plan.title)
    if trip_plan.overall_distance_km is not None:
        lines.append(f"Distance: {trip_plan.overall_distance_km:.2f} km")
    if trip_plan.overall_elevation_gain_m is not None:
        lines.append(f"Elevation gain: {trip_plan.overall_elevation_gain_m:.2f} m")

    lines.append("")

    for d in trip_plan.days:
        header = f"Day {d.day}: {d.start_location} -> {d.end_location}"
        if d.distance_km is not None:
            header += f" | {d.distance_km:.2f} km"
        lines.append(header)

        sub = []
        if d.elevation_gain_m is not None:
            sub.append(f"Elevation gain: {d.elevation_gain_m:.2f} m")
        if d.terrain_difficulty is not None:
            sub.append(f"Terrain difficulty: {d.terrain_difficulty}")
        if d.weather_summary is not None:
            sub.append(f"Weather: {d.weather_summary}")
        lines.append(" | ".join(sub))

        if d.stay:
            lines.append(f"Stay: {d.stay}")

        lines.append("")

    return '\n'.join(lines).strip()
