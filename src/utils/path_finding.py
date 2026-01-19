# -*- coding: utf-8 -*-
"""
Created on 18/01/2026 17:11

@author: Aidan
@project: CyclingTripPlannerAgent
@filename: path_finding
"""
import heapq
import math
from functools import cache

from src.demo_data import CITY_DATA, cities, CITY_GRAPH


def get_distance_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    R = 6371  # the radius of the Earth in km
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dLon / 2) * math.sin(dLon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c


@cache
def distance_between_city(city1: str, city2: str):
    lat1, lon1, elev1 = CITY_DATA[city1].values()
    lat2, lon2, elev2 = CITY_DATA[city2].values()
    return get_distance_km(lat1, lon1, lat2, lon2)


def dijkstra_path_finding(start: str, dest: str):
    if start not in cities or dest not in cities:
        raise ValueError("City not in the dataset, cant find path")

    distance = {start: 0.0}
    prev = {}
    q = [(0.0, start)]
    visited = set()

    while q:
        dist, node = heapq.heappop(q)
        if node in visited:
            continue
        visited.add(node)

        if node == dest:
            break

        for neighbour in CITY_GRAPH[node]:
            new_dist = dist + distance_between_city(node, neighbour)
            if new_dist < distance.get(neighbour, float("inf")):
                distance[neighbour] = new_dist
                prev[neighbour] = node
                heapq.heappush(q, (new_dist, neighbour))

    if dest not in distance:
        return None

    # reverse building path
    path = [dest]
    cur = dest
    while cur != start:
        cur = prev[cur]
        path.append(cur)
    path.reverse()
    return path


def get_total_distance(path: list[str]):
    total = 0.0
    for i in range(len(path) - 1):
        total += distance_between_city(path[i], path[i + 1])
    return total

def get_total_elevation_gain(path: list[str]):
    total = 0.0
    for i in range(len(path) - 1):
        total += CITY_DATA[path[i + 1]]['elevation_m'] - CITY_DATA[path[i]]['elevation_m']
    return total
