'''
Author: sweetcoffee qq791227132@gmail.com
Date: 2022-11-05 18:04:34
LastEditors: sweetcoffee qq791227132@gmail.com
LastEditTime: 2022-11-17 17:49:30
FilePath: /python_code/tools/spatial_distribution.py
Github: https://github.com/sweetcoffee520
Description: 
Copyright (c) 2022 by sweetcoffee qq791227132@gmail.com, All Rights Reserved.
'''
from tools import fit_result_error as fre
import numpy as np

def spatial_trend_amp(time,grd):
    """空间趋势,周年和版周年振幅

    Args:
        time (array): 时间数组
        grd (array): 格网数组(三纬)

    Returns:
        (tuple): (trend,amp,semiamp)
    """
    shape = np.shape(grd)
    trend = np.zeros((shape[0],shape[1]))
    amp = np.zeros((shape[0],shape[1]))
    semiamp = np.zeros((shape[0],shape[1]))
    for i in range(shape[0]):
        for j in range(shape[1]):
            if np.any(grd[i,j,:])!=0:
                temp,_ = fre.annual_season_fit(time,grd[i,j,:])
                trend[i,j] = temp[0]
                amp[i,j] = temp[1]
                semiamp[i,j] = temp[2]

    return trend,amp,semiamp