'''
Author: sweetcoffee qq791227132@gmail.com
Date: 2022-04-28 22:20:46
LastEditors: sweetcoffee qq791227132@gmail.com
LastEditTime: 2022-06-26 00:14:34
FilePath: /python_code/tools/smooth.py
Github: https://github.com/sweetcoffee520
Description: 
Copyright (c) 2022 by sweetcoffee qq791227132@gmail.com, All Rights Reserved.
'''
import numpy as np

def move_avg(x, n):
    """
    Moving average filter
    """
    return np.convolve(x, np.ones((n,))/n, mode='valid')

def gaussian_smoothing(x, size, sigma):
    """
    Gaussian smoothing filter
    """
    return np.convolve(x, np.exp(-np.arange(-size,size+1)**2/2/sigma**2), mode='same')