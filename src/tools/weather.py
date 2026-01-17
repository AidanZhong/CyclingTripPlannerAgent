# -*- coding: utf-8 -*-
"""
Created on 16/01/2026 22:26

@author: Aidan
@project: CyclingTripPlannerAgent
@filename: weather
"""
from src.schemas.tools import GetWeatherRequest, GetWeatherResponse

# demo weather data (assume all the city has the similar weather conditions)

demo_weather_data = {
    "January": (4.0, -1.0, 12),
    "February": (5.0, 0.0, 10),
    "March": (9.0, 2.0, 10),
    "April": (13.0, 5.0, 9),
    "May": (17.0, 8.0, 9),
    "June": (20.0, 11.0, 8),
    "July": (22.0, 13.0, 8),
    "August": (22.0, 13.0, 9),
    "September": (18.0, 10.0, 9),
    "October": (13.0, 6.0, 11),
    "November": (8.0, 3.0, 12),
    "December": (5.0, 0.0, 13),
}


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
