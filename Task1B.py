# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
from haversine import haversine, Unit


def run():
    """Requirements for Task 1A"""

    # Build list of stations
    stations = build_station_list()

    # Print number of stations
    print("Number of stations: {}".format(len(stations)))

    # Display data from 3 stations:
    for station in stations:
        if station.name in [
                'Bourton Dickler', 'Surfleet Sluice', 'Gaw Bridge'
        ]:
            print(station)

print("The 10 closest entries (in km) are ", stations_by_distance(build_station_list(), (52.2053, 0.1218))[:10])
print("The 10 furthest entries (in km) are ", stations_by_distance(build_station_list(), (52.2053, 0.1218))[-10:])