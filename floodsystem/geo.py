# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

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

