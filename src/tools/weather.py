# -*- coding: utf-8 -*-
"""
Created on 16/01/2026 22:26

@author: Aidan
@project: CyclingTripPlannerAgent
@filename: weather
"""
from src.demo_data import demo_weather_data
from src.schemas.tools import GetWeatherRequest, GetWeatherResponse


def get_weather_data(req: GetWeatherRequest) -> GetWeatherResponse:
    month = req.month.strip().capitalize()
    if month not in demo_weather_data:
        raise ValueError(f"Invalid month: {month}")
    avg_high_temp_c, avg_low_temp_c, raining_days_estimate = demo_weather_data[month]
    return GetWeatherResponse(
        avg_high_temp_c=avg_high_temp_c,
        avg_low_temp_c=avg_low_temp_c,
        raining_days_estimate=raining_days_estimate
    )
