# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
from distutils.command.build import build
from floodsystem.stationdata import build_station_list
from haversine import haversine, Unit


print(geo.stations_by_distance(build_station_list(), (52.2053, 0.1218))[:10])