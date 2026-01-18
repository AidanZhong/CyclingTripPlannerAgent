# -*- coding: utf-8 -*-
"""
Created on 16/01/2026 22:26

@author: Aidan
@project: CyclingTripPlannerAgent
@filename: accommodation
"""
from src.demo_data import demo_accommodation_data, BASE_PRICE
from src.schemas.tools import FindAccommodationRequest, FindAccommodationResponse, AccommodationOption
from src.schemas.trip import AccommodationType


def find_accommodation(req: FindAccommodationRequest) -> FindAccommodationResponse:
    res = FindAccommodationResponse()
    for accommodation_type in demo_accommodation_data[req.near]:
        for accommodation in demo_accommodation_data[req.near][accommodation_type]:
            res.results.append(AccommodationOption(
                name=accommodation,
                type=AccommodationType.from_string(accommodation_type),
                approx_price_per_night=BASE_PRICE[accommodation_type]
            ))
            if res.results.__len__() >= req.limit:
                break

    return res
