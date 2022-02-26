from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import build_station_list, update_water_levels

def test_stations_level_over_threshold():

     # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    slot = stations_level_over_threshold(stations, 0.3)

    assert type(slot) == list
    assert len(slot) >= 0
    for _ in slot:
        assert type(_) == tuple
        assert len(_) == 2
        assert type(_[0]) == object
        assert type(_[1]) == int
        assert _[1] >= 0.3

def test_stations_highest_rel_level():

     # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    shrl = stations_highest_rel_level(stations, 96)

    assert type(shrl) == list
    assert len(shrl) == 96
    for _ in shrl:
        assert type(_) == object
