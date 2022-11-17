'''
Author: sweetcoffee qq791227132@gmail.com
Date: 2022-07-11 15:40:29
LastEditors: sweetcoffee qq791227132@gmail.com
LastEditTime: 2022-10-04 20:56:58
FilePath: /python_code/tools/interpolate_data.py
Github: https://github.com/sweetcoffee520
Description: 
Copyright (c) 2022 by sweetcoffee qq791227132@gmail.com, All Rights Reserved.
'''
import xarray as xr
from scipy.interpolate import griddata
import numpy as np

def interpolate_data(data, lat, lon, lat_interp, lon_interp,method='linear'):
    """数据插值或降采样

    Args:
        data (array): 待插值或降采样数组
        lat (array): data的纬度数组
        lon (array): data的经度数组
        lat_interp (array): 插值纬度数组
        lon_interp (array): 插值经度数组
        method (str, optional): 插值方法('linear','nearest','cubic'). Defaults to 'linear'.

    Returns:
        _type_: _description_
    """
    shapenum = data.ndim
    xv,yv = np.array(np.meshgrid(lon,lat))
    point = np.c_[xv.flatten(),yv.flatten()]
    interp_xv,interp_yv = np.array(np.meshgrid(lon_interp,lat_interp))
    interp_point = np.c_[interp_xv.flatten(),interp_yv.flatten()]
    if shapenum == 2:
        data_interp = griddata(point,data.flatten(),interp_point,method=method).reshape(len(lat_interp),len(lon_interp))
    elif shapenum == 3:
        data_interp = np.zeros((len(lat_interp),len(lon_interp),data.shape[2]))
        for i in range(np.size(data,2)):
            data_interp[:,:,i] = griddata(point,data[:,:,i].flatten(),interp_point,method=method).reshape(len(lat_interp),len(lon_interp))

    return data_interp