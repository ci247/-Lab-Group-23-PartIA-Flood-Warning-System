# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to assessing flood risk by level"""
from operator import itemgetter

def stations_level_over_threshold(stations, tol):
    ans = []
    for station in stations:
        try:
            if station.relative_water_levels() > tol:
                ans += [(station, station.relative_water_levels())]
            else:
                pass
        except:
            pass
    ans.sort(key = lambda a: a[1], reverse = True)
    return ans