# -*- coding: utf-8 -*-
"""
Created on 18/01/2026 16:55

@author: Aidan
@project: CyclingTripPlannerAgent
@filename: demo_data
"""
from typing import List

from src.utils.intent_matching import build_tfidf

# demo city data
CITY_DATA = {
    "Amsterdam": {"lat": 52.3676, "lon": 4.9041, "elevation_m": 14},
    "Utrecht": {"lat": 52.0907, "lon": 5.1214, "elevation_m": 9},
    "Arnhem": {"lat": 51.9851, "lon": 5.8987, "elevation_m": 14},
    "Osnabrück": {"lat": 52.2799, "lon": 8.0472, "elevation_m": 65},
    "Bremen": {"lat": 53.0793, "lon": 8.8017, "elevation_m": 12},
    "Hamburg": {"lat": 53.5511, "lon": 9.9937, "elevation_m": 8},
    "Lübeck": {"lat": 53.8699, "lon": 10.6866, "elevation_m": 13},
    "Rostock": {"lat": 54.0924, "lon": 12.0991, "elevation_m": 13},
    "Malmö": {"lat": 55.6050, "lon": 13.0038, "elevation_m": 12},
    "Copenhagen": {"lat": 55.6761, "lon": 12.5683, "elevation_m": 14},
    "London": {"lat": 51.5074, "lon": -0.1278, "elevation_m": 11},
    "Canterbury": {"lat": 51.2802, "lon": 1.0789, "elevation_m": 5},
    "Dover": {"lat": 51.1265, "lon": 1.3134, "elevation_m": 8},
    "Calais": {"lat": 50.9513, "lon": 1.8587, "elevation_m": 6},
    "Amiens": {"lat": 49.8941, "lon": 2.2958, "elevation_m": 27},
    "Paris": {"lat": 48.8566, "lon": 2.3522, "elevation_m": 35},
}
print(CITY_DATA.keys())
cities = ['Amsterdam', 'Utrecht', 'Arnhem', 'Osnabrück', 'Bremen', 'Hamburg', 'Lübeck', 'Rostock', 'Malmö',
          'Copenhagen', 'London', 'Canterbury', 'Dover', 'Calais', 'Amiens', 'Paris']

CITY_GRAPH = {
    # Amsterdam - fully connected with nearby cities
    "Amsterdam": ["Utrecht", "Arnhem", "Bremen"],
    "Utrecht": ["Amsterdam", "Arnhem", "Osnabrück"],
    "Arnhem": ["Amsterdam", "Utrecht", "Osnabrück"],
    "Osnabrück": ["Utrecht", "Arnhem", "Bremen"],
    "Bremen": ["Amsterdam", "Osnabrück", "Hamburg"],

    # Hamburg region - fully connected
    "Hamburg": ["Bremen", "Lübeck", "Copenhagen"],
    "Lübeck": ["Hamburg", "Rostock", "Malmö", "Hamburg"],
    "Rostock": ["Lübeck", "Copenhagen"],
    "Malmö": ["Lübeck", "Copenhagen", "Rostock"],
    "Copenhagen": ["Hamburg", "Rostock", "Malmö"],

    # UK - fully connected triangle
    "London": ["Canterbury", "Dover"],
    "Canterbury": ["London", "Dover"],
    "Dover": ["London", "Canterbury", "Calais"],

    # France - fully connected
    "Calais": ["Dover", "Amiens", "Paris"],
    "Amiens": ["Calais", "Paris"],
    "Paris": ["Calais", "Amiens"]
}

# demo data
demo_accommodation_data = {
    'Amsterdam': {
        'camping': ['Coastal Campground', 'Canal Retreat'],
        'hostel': ['Amsterdam Inn', 'International House', 'Downtown Hub'],
        'hotel': ['Imperial Resort', 'Louvre Residence'],
    },
    'Utrecht': {
        'hostel': ['Utrecht Lodge', 'Central Stay'],
        'hotel': ['Regal Palace', 'Utrecht Suites'],
    },
    'Arnhem': {
        'camping': ['Valley Park', 'Forest Oasis'],
        'hostel': ['Arnhem Inn', 'Student Point'],
        'hotel': ['Grand Towers'],
    },
    'Osnabrück': {
        'hostel': ['City Base', 'Urban Lodge'],
        'hotel': ['Royal Hotel', 'Continental Residence'],
    },
    'Bremen': {
        'camping': ['Mountain Hideaway'],
        'hostel': ['Bremen Hostel', 'Traveler House'],
        'hotel': ['Majestic Retreat', 'Bremen Suites'],
    },
    'Hamburg': {
        'hostel': ['Hamburg Hub', 'Port Stay'],
        'hotel': ['Metropolitan Inn', 'Harbor Resort'],
    },
    'Lübeck': {
        'camping': ['Riverside Resort'],
        'hostel': ['Lübeck House'],
        'hotel': ['Boutique Hotel', 'Lübeck Residence'],
    },
    'Rostock': {
        'hostel': ['Rostock Lodge', 'Youth Base'],
        'hotel': ['Plaza Suites'],
    },
    'Malmö': {
        'camping': ['Coastal Park'],
        'hostel': ['Malmö Inn', 'Scandinavian Point'],
        'hotel': ['Swedish Palace'],
    },
    'Copenhagen': {
        'hostel': ['Copenhagen Hostel', 'Nyhavn House', 'Danish Hub'],
        'hotel': ['Royal Towers', 'Tivoli Retreat'],
    },
    'London': {
        'camping': ['Thames Campsite'],
        'hostel': ['London Eye Stay', 'British Base', 'Big Ben Inn'],
        'hotel': ['Grand Hotel', 'Royal Palace', 'Thames Residence'],
    },
    'Canterbury': {
        'hostel': ['Canterbury Lodge'],
        'hotel': ['Boutique Suites'],
    },
    'Dover': {
        'camping': ['Coastal Hideaway'],
        'hostel': ['Dover House'],
    },
    'Calais': {
        'hostel': ['Calais Hostel', 'Central Point'],
        'hotel': ['Continental Hotel'],
    },
    'Amiens': {
        'hostel': ['Amiens Inn'],
        'hotel': ['Regal Resort'],
    },
    'Paris': {
        'camping': ['Seine Campground'],
        'hostel': ['Paris Hub', 'Eiffel House', 'French Stay'],
        'hotel': ['Champs-Élysées Palace', 'Luxury Hotel', 'Seine Suites'],
    },
}

BASE_PRICE = {"camping": 18.0, "hostel": 38.0, "hotel": 85.0}

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

# a sample corpus used for demo
INTENT_CORPUS: List[str] = [
    "i want to cycle from X to Y",
    "my route is from X to Y",
    "plan a trip from X to Y",

    "i can do about X km per day",
    "around X km a day",
    "my daily distance is X km",

    "traveling in june",
    "going in july",
    "in august",

    "i prefer camping",
    "i want hostels",
    "i prefer hotels",

    "prefer camping but want a hostel every 4th night",
    "hostel every 3 nights",
    "hotel every 5th night",
]

INTENT_LABELS: List[str] = [
    "PROVIDE_ROUTE",
    "PROVIDE_ROUTE",
    "PROVIDE_ROUTE",

    "PROVIDE_DAILY_DISTANCE",
    "PROVIDE_DAILY_DISTANCE",
    "CHANGE_DAILY_DISTANCE",

    "PROVIDE_MONTH",
    "PROVIDE_MONTH",
    "PROVIDE_MONTH",

    "PROVIDE_ACCOMMODATION_PRIMARY",
    "PROVIDE_ACCOMMODATION_PRIMARY",
    "PROVIDE_ACCOMMODATION_PRIMARY",

    "PROVIDE_ACCOMMODATION_PATTERN",
    "PROVIDE_ACCOMMODATION_PATTERN",
    "PROVIDE_ACCOMMODATION_PATTERN",
]

VECTORIZE, CORPUS_VECS = build_tfidf(INTENT_CORPUS)