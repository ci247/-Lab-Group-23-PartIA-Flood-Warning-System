# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number
from floodsystem.station import inconsistent_typical_range_stations


def run():
    """Requirements for Task 1F"""

    # Build list of stations
    stations = build_station_list()

    # Build list of stations with inconsistent typical range data
    inconsistent_stations_list = inconsistent_typical_range_stations(stations)

    # Display data
    print([station.name for station in inconsistent_stations_list])


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System *** \n\n")
    run()
