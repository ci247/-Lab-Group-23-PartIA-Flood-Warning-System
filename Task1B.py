# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from turtle import distance
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
from haversine import haversine, Unit


def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    # Stores information from function
    stations_by_distance_list = stations_by_distance(stations, (52.2053, 0.1218))

    # Creates empty list to be returned
    answer = []

    # Loop adds new tuples to the list of tuples until all the information from stations_by_distance_list has been used
    for station,distance in stations_by_distance_list:
        answer += [(station.name, station.town, distance)]
    print("The 10 closest stations from Cambridge city centre ", answer[:10])
    print("The 10 furthest stations from Cambridge city centre ", answer[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()