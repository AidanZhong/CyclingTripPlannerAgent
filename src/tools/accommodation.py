# -*- coding: utf-8 -*-
"""
Created on 16/01/2026 22:26

@author: Aidan
@project: CyclingTripPlannerAgent
@filename: accommodation
"""
from src.schemas.tools import FindAccommodationRequest, FindAccommodationResponse, AccommodationOption
from src.schemas.trip import AccommodationType

# demo data
demo_accommodation_data = {
    'Amsterdam': {
        'camping': ['Coastal Campground', 'Canal Retreat'],
        'hostels': ['Amsterdam Inn', 'International House', 'Downtown Hub'],
        'hotels': ['Imperial Resort', 'Louvre Residence'],
    },
    'Utrecht': {
        'hostels': ['Utrecht Lodge', 'Central Stay'],
        'hotels': ['Regal Palace', 'Utrecht Suites'],
    },
    'Arnhem': {
        'camping': ['Valley Park', 'Forest Oasis'],
        'hostels': ['Arnhem Inn', 'Student Point'],
        'hotels': ['Grand Towers'],
    },
    'Osnabrück': {
        'hostels': ['City Base', 'Urban Lodge'],
        'hotels': ['Royal Hotel', 'Continental Residence'],
    },
    'Bremen': {
        'camping': ['Mountain Hideaway'],
        'hostels': ['Bremen Hostel', 'Traveler House'],
        'hotels': ['Majestic Retreat', 'Bremen Suites'],
    },
    'Hamburg': {
        'hostels': ['Hamburg Hub', 'Port Stay'],
        'hotels': ['Metropolitan Inn', 'Harbor Resort'],
    },
    'Lübeck': {
        'camping': ['Riverside Resort'],
        'hostels': ['Lübeck House'],
        'hotels': ['Boutique Hotel', 'Lübeck Residence'],
    },
    'Rostock': {
        'hostels': ['Rostock Lodge', 'Youth Base'],
        'hotels': ['Plaza Suites'],
    },
    'Malmö': {
        'camping': ['Coastal Park'],
        'hostels': ['Malmö Inn', 'Scandinavian Point'],
        'hotels': ['Swedish Palace'],
    },
    'Copenhagen': {
        'hostels': ['Copenhagen Hostel', 'Nyhavn House', 'Danish Hub'],
        'hotels': ['Royal Towers', 'Tivoli Retreat'],
    },
    'London': {
        'camping': ['Thames Campsite'],
        'hostels': ['London Eye Stay', 'British Base', 'Big Ben Inn'],
        'hotels': ['Grand Hotel', 'Royal Palace', 'Thames Residence'],
    },
    'Canterbury': {
        'hostels': ['Canterbury Lodge'],
        'hotels': ['Boutique Suites'],
    },
    'Dover': {
        'camping': ['Coastal Hideaway'],
        'hostels': ['Dover House'],
    },
    'Calais': {
        'hostels': ['Calais Hostel', 'Central Point'],
        'hotels': ['Continental Hotel'],
    },
    'Amiens': {
        'hostels': ['Amiens Inn'],
        'hotels': ['Regal Resort'],
    },
    'Paris': {
        'camping': ['Seine Campground'],
        'hostels': ['Paris Hub', 'Eiffel House', 'French Stay'],
        'hotels': ['Champs-Élysées Palace', 'Luxury Hotel', 'Seine Suites'],
    },
}

BASE_PRICE = {"camping": 18.0, "hostel": 38.0, "hotel": 85.0}


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
