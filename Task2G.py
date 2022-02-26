# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

import datetime
from matplotlib.dates import date2num
import numpy as np

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import polyfit
from floodsystem.flood import stations_highest_rel_level
from floodsystem.utils import sorted_by_key


def run():
    """Requirements for Task 2G"""

    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    """Criteria for flooding:
    Relative water level list
    Rate of change (rising or falling)
    For both catrgories:
    top 25 percentile +3 points
    top 50 percentile +2 points
    bottom 50 percentile +1 points
    bottom 25 percentile +0 points
    Add points from both categories and check ranges for follding risk:
    == 6 Severe
    >= 4 Moderate
    >= 2 High
    Low

    """

    # Number of stations wanted
    N = 150 #len(stations)

    # Store list of station objects to plot: stations_highest_rel_level(stations, 10)
    stations_highest_list = stations_highest_rel_level(stations, N)

    # Create list of tuples to store risk of flooding ratings and points for each station
    flooding_risk = []

    for station in stations_highest_list:
        # Fetch data over past 2 days
        dt = 2
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        
        # Calculate if water levels are rising or falling
        try:
            poly, date_shift = polyfit(dates, levels, 4)
            poly_gradient = np.polyder(poly)
            x1 = date2num(dates)
            gradient = poly_gradient(x1[-1]-date_shift)

            # Assign points. perecentile ranking of relative water level + 10 * gradient. Gradient of levels is a more important
            # factor for predicting flood risk and has a greater weight of 10
            points = stations_highest_list.index(station)/len(stations_highest_list) + 10*gradient
        except:
            points = 0

        #Assign rating
        if points >= 10:
            rating = "Severe"
        elif points >= 0:
            rating = "High"
        elif points >= -5:
            rating = "Moderate"
        else:
            rating = "Low"
        
        print("Processing", stations_highest_list.index(station), "out of ", len(stations_highest_list))
        flooding_risk.append((station.name, rating, points))

    # Sort by risk of flooding (points)
    flooding_risk = sorted_by_key(flooding_risk, 2)

    for station_name, rating, points in flooding_risk:
        print(station_name, rating, points)

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
