# -*- coding: utf-8 -*-
"""
Created on 16/01/2026 22:27

@author: Aidan
@project: CyclingTripPlannerAgent
@filename: tools
"""
from typing import Optional

from pydantic import BaseModel

from src.schemas.trip import AccommodationType


# -------Route--------
class GetRouteRequest(BaseModel):
    origin: str
    destination: str
    daily_distance_km: float


class GetRouteResponse(BaseModel):
    total_distance_km: float
    estimation_days: int
    waypoints: list["Waypoint"]


class Waypoint(BaseModel):
    name: str
    lat: Optional[float] = None
    lon: Optional[float] = None


# -------Accommodation--------
class FindAccommodationRequest(BaseModel):
    near: str
    type: AccommodationType
    limit: int = 3


class AccommodationOption(BaseModel):
    name: str
    type: AccommodationType
    approx_price_per_night: Optional[float] = None


class FindAccommodationResponse(BaseModel):
    results: list[AccommodationOption]


# -------Weather--------
class GetWeatherRequest(BaseModel):
    location: str
    month: str


class GetWeatherResponse(BaseModel):
    avg_high_temp_c: float
    avg_low_temp_c: float
    raining_days_estimate: int


# -------Elevation--------
class GetElevationProfileRequest(BaseModel):
    origin: str
    destination: str


class GetElevationProfileResponse(BaseModel):
    elevation_gain_m: float
    difficulty_rating: str
