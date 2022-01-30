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