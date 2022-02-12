# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
analyzing data.

"""

import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import numpy as np

def polyfit(dates, levels, p):
    x = date2num(dates)
    y = levels

    # Find coefficients of best-fit polynomial f(x) of degree 4
    p_coeff = np.polyfit(x-x[0], levels, p)

    # Convert coefficient into a polynomial that can be evaluated,
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)

    return (poly, x[0])

    



