# -*- coding: utf-8 -*-
"""
Created on 16/01/2026 22:26

@author: Aidan
@project: CyclingTripPlannerAgent
@filename: route
"""
import math
from typing import Dict, Tuple

from src.demo_data import CITY_DATA
from src.schemas.tools import GetRouteRequest, GetRouteResponse, Waypoint
from src.utils.path_finding import dijkstra_path_finding, get_total_distance


def get_route(request: GetRouteRequest) -> GetRouteResponse:
    origin_key, destination_key = request.origin.lower(), request.destination.lower()
    if not origin_key or not destination_key:
        raise ValueError("Origin and destination must be specified")

    path = dijkstra_path_finding(origin_key, destination_key)
    if not path:
        raise ValueError("No route found between these locations")

    waypoints = [
        Waypoint(name=c, lat=CITY_DATA[c]['lat'], lon=CITY_DATA[c]['lon'])
        for c in path
    ]

    total_km = get_total_distance(path)

    estimated_days = max(1, math.ceil(total_km / request.daily_distance_km))
    return GetRouteResponse(
        total_distance_km=total_km,
        estimated_days=estimated_days,
        waypoints=waypoints
    )
