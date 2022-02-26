# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to assessing flood risk by level"""
from operator import itemgetter

def stations_level_over_threshold(stations, tol):
    ans = []
    consistent_stations = [station for station in stations if station.typical_range_consistent()]
    for station in consistent_stations:
        try:
            if station.relative_water_levels() > tol and station.relative_water_levels() < 10:
                ans += [(station, station.relative_water_levels())]
        except:
            pass

    #sorts tuples inside the list in terms of relative water level elements
    ans.sort(key = lambda a: a[1], reverse = True)

    #returns a list of tuples, each tuple holds (i) a station (object) at which the latest relative water level is over tol and (ii) the relative water level at the station
    return ans

def stations_highest_rel_level(stations, N):

    #stores all [(station objects, relative water levels)] as list of tuples in descending order
    all_descending = stations_level_over_threshold(stations, -9999)

    #stores all the "station object" element of each tuple in a list of length N
    ans = []
    for i in range(N):
        ans += [all_descending[i][0]]

    #returns a list of the N stations (objects) at which the water level, relative to the typical range, is highest
    return ans