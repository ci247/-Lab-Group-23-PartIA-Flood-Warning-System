# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit

def rivers_with_station(stations):
    """Build and return a list of all rivers with river level monitoring stations
    based on data provided to the fucniton. The expected input is a list of MonitoringStation
    objects.

    """

    # Create empty list to store rivers with monitoring stations
    rivers = []
    
    # Store river name in list if it does not already exist.
    for station in stations:
        if (station.river != None) and (station.river not in rivers):
            rivers.append(station.river)

    return rivers

def stations_by_river(stations):
    """Build and return a dictionary of rivers mapped to their level monitoring stations
    based on data provided to the fucniton. The expected input is a list of MonitoringStation
    objects.

    """
    
    # Create empty dictionary to be returned
    stations_by_river_dict = {}

    # Iteratre through the list of stations and map station to relevant river
    for station in stations:
        if station.river != None:
            try:
                stations_by_river_dict[station.river].append(station.name)
            except:
                stations_by_river_dict[station.river] = [station.name]

    return stations_by_river_dict

def rivers_by_station_number(stations, N=1):
    """Build and return a list of N tuples of N rivers with the greatest number of
    level monitoring stations based on data provided to the fucniton. The expected
    input is a list of MonitoringStation objects and an integer N. In the case that
    there are more rivers with the same number of stations as the N th entry, include
    these rivers in the list.

    """
    
    # Create empty list to be returned
    rivers_by_station_number_list = []

    stations_by_river_dict = stations_by_river(stations)

    for river_name, river_stations in stations_by_river_dict.items():
        rivers_by_station_number_list.append((river_name,len(river_stations)))

    sorted_stations_dict = sorted_by_key(rivers_by_station_number_list, 1, reverse=True)
    return [pair for pair in sorted_stations_dict if pair[1] >= sorted_stations_dict[N][1]]

def stations_by_distance(stations, p):
    """Build and return a list of (station, distance) tuples based on data provided to the function.
    The expected input is a list of MonitoringStation station objects and a coordinate p"""

    # Create empty list to be returned
    list_of_tuples = []

    # Building list of tuples of (station name, distance from point p) using haversine function
    for station in stations:
        list_of_tuples += [(station, haversine(station.coord,p))]
    
    # Sorts final result in ascending order of distances from point p and returns list_of_tuples
    return sorted_by_key(list_of_tuples, 1)

def stations_within_radius(stations, centre, r):
    """Build and return a list of stations based on data provided to the function.
    The expected input is a list of MonitoringStation station objects and a coordinate p"""

    # Create empty list to be returned
    list = []

    # Building list of stations within the radius using if condition and calculating distance between each station and the "centre"
    for station in stations:
        if haversine(station.coord,centre) <= r:
            list += [station] 
    # Sorts final result in ascending order of distances from point p and returns list_of_tuples
    return list