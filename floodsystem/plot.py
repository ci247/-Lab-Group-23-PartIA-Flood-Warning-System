# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
plotting and visualizing data.

"""

import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from .analysis import polyfit

def plot_water_levels(station, dates, levels):
    """Plot a graph of water level data at given dates for a river level monitoring station
    based on data provided to the fucniton. The expected input is a MonitoringStation
    object, list of dates and list of levels.

    """

    min_level = station.typical_range[0]
    max_level = station.typical_range[1]

    # Plot
    plt.plot(dates, levels)
    plt.plot([dates[0], dates[-1]],[station.typical_range[0], station.typical_range[0]])
    plt.plot([dates[0], dates[-1]],[station.typical_range[1], station.typical_range[1]])

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("Station {}".format(station.name))

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    """Plot a graph of water level data at given dates and the best fit line for a river level monitoring station
    based on data provided to the fucniton. The expected input is a MonitoringStation
    object, list of dates and list of levels.

    """

    min_level = station.typical_range[0]
    max_level = station.typical_range[1]

    # Plot original data points
    plt.plot(dates, levels)
    plt.plot([dates[0], dates[-1]],[station.typical_range[0], station.typical_range[0]])
    plt.plot([dates[0], dates[-1]],[station.typical_range[1], station.typical_range[1]])


    # Plot polynomial fit at 30 points along interval
    poly, date_shift = polyfit(dates, levels, p)
    x1 = date2num(dates)
    plt.plot(x1, poly(x1-date_shift))

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("Station {}".format(station.name))

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()