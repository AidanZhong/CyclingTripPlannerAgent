# -*- coding: utf-8 -*-
"""
Created on 18/01/2026 16:55

@author: Aidan
@project: CyclingTripPlannerAgent
@filename: demo_data
"""
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
CORPUS = [
    ("I want to cycle from Amsterdam to Copenhagen", "PROVIDE_ROUTE"),
    ("from Paris to Lyon", "PROVIDE_ROUTE"),
    ("100km a day", "PROVIDE_DAILY_DISTANCE"),
    ("I can do around 80 km/day", "PROVIDE_DAILY_DISTANCE"),
    ("travelling in June", "PROVIDE_MONTH"),
    ("in September", "PROVIDE_MONTH"),
    ("prefer camping", "PROVIDE_ACCOMMODATION_PRIMARY"),
    ("I want hotels", "PROVIDE_ACCOMMODATION_PRIMARY"),
    ("hostel every 4th night", "PROVIDE_ACCOMMODATION_PATTERN"),
    ("camping but a hostel every 4 nights", "PROVIDE_ACCOMMODATION_PATTERN"),
    ("change to 80km/day", "CHANGE_DAILY_DISTANCE"),
    ("actually make it 120km per day", "CHANGE_DAILY_DISTANCE"),
    ("switch to hotels", "CHANGE_ACCOMMODATION"),
]
