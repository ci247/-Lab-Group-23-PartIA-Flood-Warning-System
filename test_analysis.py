# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the analysis module"""

from matplotlib.dates import date2num
import numpy as np
from datetime import datetime, timedelta
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.analysis import polyfit


def test_polyfit():

     # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    stations_highest_list = stations_highest_rel_level(stations, 10)

    dt = 2
    dates, levels = fetch_measure_levels(stations_highest_list[0].measure_id, dt=datetime.timedelta(days=dt))
    
    # Calculate if water levels are rising or falling
    output = polyfit(dates, levels, 4)

    assert type(output) == tuple
    assert len(output) == 2
    poly, date_shift = output