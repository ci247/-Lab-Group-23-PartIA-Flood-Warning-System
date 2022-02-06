# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the geo module"""

from floodsystem.geo import *


def test_rivers_with_station():
    """Test rivers_with_station"""

    # Build list of stations
    stations = build_station_list()

    rivers = rivers_with_station(stations)

    assert type(rivers) == list
    assert len(rivers) > 0
    for _ in rivers:
        assert type(_) == str

def test_stations_by_river():
    """Test stations_by_river"""

    # Build list of stations
    stations = build_station_list()

    stations_by_river_dict = stations_by_river(stations)

    assert type(stations_by_river_dict) == dict
    assert len(stations_by_river_dict) > 0
    for key, value in stations_by_river_dict.items():
        assert type(key) == str
        assert type(value) == list
        for _ in value:
        assert type(_) == str

def test_rivers_by_station_number():
    """Test rivers_by_station_number"""

    # Build list of stations
    stations = build_station_list()

    rivers = rivers_by_station_number(stations, 9)

    assert type(rivers) == list
    assert len(rivers) >= 9
    for _ in rivers:
        assert type(_) == tuple
        assert len(2) == 2
        assert type(_[0]) == str
        assert type(_[1]) == int
        assert t_[1] > 0

def test_stations_by_distance():
    """Test stations_by_distance"""

    # Build list of stations
    stations = build_station_list()

    stations_by_distance_list = stations_by_distance(stations, (52.2053, 0.1218))

    assert type(stations_by_distance_list) == list
    assert len(stations_by_distance_list) == len(stations)
    for _ in stations_by_distance_list:
        assert type(_) == tuple
        assert len(2) == 2
        assert type(_[1]) == float
        assert _[1] > 0

def test_stations_within_radius():
    """Test stations_within_radius"""

    # Build list of stations
    stations = build_station_list()

    stations_within_radius_list = stations_within_radius(stations, (52.2053, 0.1218), 10)

    assert type(stations_within_radius_list) == list
    assert len(stations_within_radius_list) > 0

