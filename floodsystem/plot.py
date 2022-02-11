# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
plotting and visualizing data.

"""

import matplotlib.pyplot as plt
from datetime import datetime, timedelta

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