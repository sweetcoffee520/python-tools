'''
Author: sweetcoffee qq791227132@gmail.com
Date: 2022-05-12 13:16:13
LastEditors: sweetcoffee qq791227132@gmail.com
LastEditTime: 2022-11-20 13:04:54
FilePath: /python_code/tools/gaussian_smooth.py
Description: 

Copyright (c) 2022 by sweetcoffee qq791227132@gmail.com, All Rights Reserved.
'''
import numpy as np
import scipy.fft as fft
from scipy.signal import windows

def gaussian_smooth_frequency(x,n):
    """频域的高斯平滑

    Args:
        x (array): 时间序列
        n (array): 窗口大小

    Returns:
        array: 平滑后的时间序列
    """
    X = fft.fft(x)
    g = windows.gaussian(n,1)
    g = g[int(n/2):]
    g=np.insert(np.append(np.append(g,np.zeros(len(x)-n-1)),g[::-1]),0,1)
    xs = fft.ifft(g*X)

    return xs