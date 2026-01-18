# -*- coding: utf-8 -*-
"""
Created on 16/01/2026 22:26

@author: Aidan
@project: CyclingTripPlannerAgent
@filename: trip
"""
from enum import Enum


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


class TripPreferences:
    origin: str | None
    destination: str | None
    start_month: str | None
    daily_distance_km: float | None
    accommodation: AccommodationPreference | None


class AccommodationPreference:
    primary: AccommodationType
    alt: AccommodationType | None = None
    alt_every_n_nights: int | None = None
    '''
        rules:
        if alt is not None, alt_every_n_nights must be set and must be > 2
        if alt is None, the system will treat as always prefer primary
    '''


class TripStateSummary:
    # for API response
    origin: str
    destination: str
    start_month: str
    daily_distance_km: float
    accommodation_primary: str
    accommodation_alt: str
    alt_every_n_nights: int


class DayPlan:
    day: int
    start_location: str
    end_location: str
    distance_km: float
    elevation_gain_m: float
    terrain_difficulty: str
    weather_summary: str
    stay: str


class TripPlan:
    title: str
    days: list[DayPlan]
    overall_distance_km: float
    overall_elevation_gain_m: float
    overall_notes: str
