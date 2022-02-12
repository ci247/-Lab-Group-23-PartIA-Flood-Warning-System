# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold

def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    #Number of stations wanted
    N = 10

    #store list of tuples: stations_level_over_threshold(stations, -9999)
    stations_level_list = stations_level_over_threshold(stations,-9999)

    print(stations_level_list)
    level = []
    for i in range(N):
       level += stations_level_list[i][1]
    print(level)


    #store list of station objects: stations_highest_rel_level(stations, 10)
    stations_highest_list = stations_highest_rel_level(stations, N)
    highest = []
    for station in stations_highest_list:
        highest += [station.name]
    #print(highest)


if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()