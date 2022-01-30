# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number


def run():
    """Requirements for Task 1E"""

    # Build list of stations
    stations = build_station_list()

    # Build list of 9 rivers by number of stations
    rivers_by_station_number_list = rivers_by_station_number(stations, 9)

    # Display data
    print(rivers_by_station_number_list,'\n')


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System *** \n\n")
    run()
