# -*- coding: utf-8 -*-
"""
Created on 16/01/2026 22:26

@author: Aidan
@project: CyclingTripPlannerAgent
@filename: elevation
"""
from src.configuration import easy_elevation_threshold, medium_elevation_threshold, hard_elevation_threshold
from src.schemas.tools import GetElevationProfileRequest, GetElevationProfileResponse

# demo data
city_elevation = {
    'Amsterdam': 2123, 'Utrecht': 53, 'Arnhem': 13, 'Osnabrück': 63,
    'Bremen': 12, 'Hamburg': 612, 'Lübeck': 13, 'Rostock': 13,
    'Malmö': 121, 'Copenhagen': 14, 'London': 35, 'Canterbury': 3,
    'Dover': 12, 'Calais': 45, 'Amiens': 353, 'Paris': 3555
}


def get_elevation_profile(req:GetElevationProfileRequest) -> GetElevationProfileResponse:
    elevation_gain_m = city_elevation[req.destination] - city_elevation[req.origin]
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
