# -*- coding: utf-8 -*-
"""
Created on 16/01/2026 22:26

@author: Aidan
@project: CyclingTripPlannerAgent
@filename: route
"""
from typing import Dict, Tuple

from src.schemas.tools import GetRouteRequest, GetRouteResponse, Waypoint

# demo
ROUTES: Dict[Tuple[str, str], dict] = {
    ("amsterdam", "copenhagen"): {
        "total_distance_km": 650,
        "waypoints": ["Amsterdam", "Utrecht", "Arnhem", "Osnabrück", "Bremen", "Hamburg", "Lübeck", "Rostock", "Malmö",
                      "Copenhagen"],
    },
    ("london", "paris"): {
        "total_distance_km": 460,
        "waypoints": ["London", "Canterbury", "Dover", "Calais", "Amiens", "Paris"],
    },
}


def get_route(request: GetRouteRequest) -> GetRouteResponse:
    origin_key, destination_key = request.origin.lower(), request.destination.lower()
    if not origin_key or not destination_key:
        raise ValueError("Origin and destination must be specified")

    key = (origin_key, destination_key)
    if key in ROUTES:
        data = ROUTES[key]
        total = data["total_distance_km"]
        waypoints = [Waypoint(name=w) for w in data["waypoints"]]
    else:
        raise ValueError("No route found between these locations")

    estimated_days = max(1, (total // request.daily_distance_km))
    return GetRouteResponse(
        total_distance_km=total,
        estimated_days=estimated_days,
        waypoints=waypoints
    )
