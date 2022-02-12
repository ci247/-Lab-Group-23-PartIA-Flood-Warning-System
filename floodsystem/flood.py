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
            if station.relative_water_levels() > tol:
                ans += [(station, station.relative_water_levels())]
            else:
                pass
        except:
            pass
    ans.sort(key = lambda a: a[1], reverse = True)
    return ans

def stations_highest_rel_level(stations, N):
    #stores all [(station objects, relative water levels)] as list of tuples in descending order
    all_descending = stations_level_over_threshold(stations, -9999)
    ans = []
    for i in range(N):
        ans += [all_descending[i][0]]
    return ans