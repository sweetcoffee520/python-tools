'''
Author: sweetcoffee qq791227132@gmail.com
Date: 2022-04-28 22:20:46
LastEditors: sweetcoffee qq791227132@gmail.com
LastEditTime: 2022-06-26 00:25:24
FilePath: /python_code/tools/sen.py
Description: 取STL趋势项trend值

Copyright (c) 2022 by sweetcoffee qq791227132@gmail.com, All Rights Reserved.
'''
import numpy as np
from . import matlab_addition as ma
def sen(x,y):
    """

    Args:
        x (array): time
        y (array): timeseries

    Returns:
        s (float): mean estimate slope
        b (float): y-intercept
    """

    comb = np.flipud(ma.nchoosek(1,len(x),1,2).flatten())
    s = np.median(np.diff(y[comb-1],1)/np.diff(x[comb-1],1))
    b = np.median(y-s*x)

    return s,b