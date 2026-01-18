# -*- coding: utf-8 -*-
"""
Created on 16/01/2026 22:26

@author: Aidan
@project: CyclingTripPlannerAgent
@filename: elevation
"""
from src.configuration import easy_elevation_threshold, medium_elevation_threshold, hard_elevation_threshold
from src.schemas.tools import GetElevationProfileRequest, GetElevationProfileResponse
from src.utils.path_finding import dijkstra_path_finding, get_total_elevation_gain


def get_elevation_profile(req:GetElevationProfileRequest) -> GetElevationProfileResponse:
    origin = req.origin.lower()
    destination = req.destination.lower()

    path = dijkstra_path_finding(origin, destination)
    if not path:
        raise ValueError("No route found between these locations")

    elevation_gain_m = get_total_elevation_gain(path)

    if elevation_gain_m <= easy_elevation_threshold:
        difficulty = "easy"
    elif elevation_gain_m <= medium_elevation_threshold:
        difficulty = "medium"
    elif elevation_gain_m <= hard_elevation_threshold:
        difficulty = "hard"
    else:
        difficulty = "very hard"

    return GetElevationProfileResponse(
        elevation_gain_m=elevation_gain_m,
        difficulty_rating=difficulty
    )
