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
    
    # Store river name in list if it exists.
    for station in stations:
        if station.river != None:
            rivers.append(Station.river)
    
    # Conver to set data type as it automatically removes duplicates
    return set(rivers)