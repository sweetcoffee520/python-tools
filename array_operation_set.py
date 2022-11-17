'''
Author: sweetcoffee qq791227132@gmail.com
Date: 2022-11-15 15:51:51
LastEditors: sweetcoffee qq791227132@gmail.com
LastEditTime: 2022-11-15 16:10:38
FilePath: /python_code/tools/array_operation_set.py
Github: https://github.com/sweetcoffee520
Description: 
Copyright (c) 2022 by sweetcoffee qq791227132@gmail.com, All Rights Reserved.
'''
import numpy as np

def swaplr(array):
    """左右调换数组

    Args:
        array (array): 目标数组
    """

    array_shape = np.shape(array)
    # asser expresssion [,arguments],如果不符合条件则抛出异常
    assert array_shape[1]%2==0,'列长度不能为奇数'
    midloc = array_shape[1]//2
    array_temp = np.zeros_like(array)
    array_temp[:,:midloc] = array[:,midloc:]
    array_temp[:,midloc:] = array[:,:midloc]

    return array_temp

def swapud(array):
    """上下调换数组

    Args:
        array (array): 目标数组
    """

    array_shape = np.shape(array)
    # asser expresssion [,arguments],如果不符合条件则抛出异常
    assert array_shape[0]%2==0,'列长度不能为奇数'
    midloc = array_shape[0]//2
    array_temp = np.zeros_like(array)
    array_temp[:midloc,:] = array[midloc:,:]
    array_temp[midloc:,:] = array[:midloc,:]

    return array_temp