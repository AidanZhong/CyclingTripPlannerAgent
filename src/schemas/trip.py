# -*- coding: utf-8 -*-
"""
Created on 16/01/2026 22:26

@author: Aidan
@project: CyclingTripPlannerAgent
@filename: trip
"""
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class AccommodationType(str, Enum):
    camping = "camping"
    hotel = "hotel"
    hostel = "hostel"
    other = "other"

    @classmethod
    def from_string(cls, value: str) -> "AccommodationType":
        try:
            return cls(value.lower())
        except ValueError:
            return cls.other


class AccommodationPreference(BaseModel):
    primary: AccommodationType
    alt: Optional["AccommodationType"] = None
    alt_every_n_nights: Optional[int] = None
    '''
        rules:
        if alt is not None, alt_every_n_nights must be set and must be > 2
        if alt is None, the system will treat as always prefer primary
    '''


class TripPreferences(BaseModel):
    origin: Optional[str] = None
    destination: Optional[str] = None
    start_month: Optional[str] = None
    daily_distance_km: Optional[float] = None
    accommodation: Optional[AccommodationPreference] = None


class TripStateSummary(BaseModel):
    # for API response
    origin: str
    destination: str
    start_month: str
    daily_distance_km: float
    accommodation_primary: str
    accommodation_alt: str
    alt_every_n_nights: int


class DayPlan(BaseModel):
    day: int
    start_location: str
    end_location: str
    distance_km: float
    elevation_gain_m: float
    terrain_difficulty: str
    weather_summary: str
    stay: str


class TripPlan(BaseModel):
    title: str
    days: list[DayPlan]
    overall_distance_km: float
    overall_elevation_gain_m: float
