# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from turtle import distance
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
from haversine import haversine, Unit


def run():
    """Requirements for Task 1A"""

    # Build list of stations
    stations = build_station_list()

    # Stores entries within the radius
    stations_within_radius_list = stations_within_radius(stations, (52.2053, 0.1218), 10)

    # Creates empty list to be returned
    answer = []

    # Loop adds all the entries within the radius to the list of stations (answer) and then sorts them alphabetically
    for station in stations_within_radius_list:
        answer += [station.name]
    answer.sort()
    print("The stations within a {} KM radius are {}".format(10,answer))

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()

