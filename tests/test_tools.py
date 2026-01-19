# -*- coding: utf-8 -*-
"""
Created on 16/01/2026 22:27

@author: Aidan
@project: CyclingTripPlannerAgent
@filename: test_tools
"""
import pytest

from src.schemas.tools import GetRouteRequest, GetElevationProfileRequest
from src.tools.elevation import get_elevation_profile
from src.tools.route import get_route


def test_get_route_happy_path():
    req = GetRouteRequest(origin="Amsterdam", destination="Copenhagen", daily_distance_km=100)
    resp = get_route(req)

    assert resp is not None
    assert getattr(resp, "total_distance_km") > 0
    waypoints = getattr(resp, "waypoints")
    assert waypoints is not None and len(waypoints) >= 2
    assert waypoints[0].name.lower() == "amsterdam"
    assert waypoints[-1].name.lower() == "copenhagen"
    assert getattr(resp, "estimated_days") >= 1


def test_get_route_unknown_route_raises():
    req = GetRouteRequest(origin="Amsterdam", destination="Tokyo", daily_distance_km=100)
    with pytest.raises(Exception):
        get_route(req)


def test_get_elevation_profile_basic():
    req = GetElevationProfileRequest(origin="Amsterdam", destination="Copenhagen")
    resp = get_elevation_profile(req)

    assert resp is not None
    gain = getattr(resp, "elevation_gain_m")
    assert isinstance(gain, (int, float))
    diff = getattr(resp, "difficulty_rating", None) or getattr(resp, "difficulty", None)
    assert diff in {"easy", "medium", "hard", "very hard"}
