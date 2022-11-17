'''
Author: sweetcoffee qq791227132@gmail.com
Date: 2022-04-28 22:20:46
LastEditors: sweetcoffee qq791227132@gmail.com
LastEditTime: 2022-11-15 15:30:44
FilePath: /python_code/tools/extract_function.py
Github: https://github.com/sweetcoffee520
Description: 
Copyright (c) 2022 by sweetcoffee qq791227132@gmail.com, All Rights Reserved.
'''
import numpy as np

def extract_range(grd,lat,lon,lat_range,lon_range=None):
    """截取格网数组

    Args:
        grd (array): 格网数组
        lat (array): 纬度数组
        lon (array): 经度数组
        lat_range (tuple): 纬度范围
        lon_range (tuple): 经度范围

    Returns:
        array: 截取之后的纬度数组，经度数组，格网数组
    """
    if lon_range is None:
        latm = lat[(lat>=lat_range[0])&(lat<=lat_range[1])]
        lonm = lon
        if np.ndim(grd) == 2:
            grdm = grd[(lat>=lat_range[0])&(lat<=lat_range[1]),:]
        elif np.ndim(grd) ==3:
            grdm = grd[(lat>=lat_range[0])&(lat<=lat_range[1]),:,:]
    else:
        latm = lat[(lat>=lat_range[0])&(lat<=lat_range[1])]
        lonm = lon[(lon>=lon_range[0])&(lon<=lon_range[1])]
        if np.ndim(grd) == 2:
            grdm = grd[(lat>=lat_range[0])&(lat<=lat_range[1]),:][:,(lon>=lon_range[0])&(lon<=lon_range[1])]
        elif np.ndim(grd) == 3:
            grdm = grd[(lat>=lat_range[0])&(lat<=lat_range[1]),:,:][:,(lon>=lon_range[0])&(lon<=lon_range[1]),:]

    return latm,lonm,grdm

def extract_mask_from_global(res_lonlat,lat_range,lon_range=None):
    """对全球格网提取mask,有效值赋1

    Args:
        grd (array): 零数组
        res_lonlat (float): 分辨率
        lat_range (tuple): 纬度范围
        lon_range (tuple): 经度范围

    Returns:
        array: 截取之后的纬度数组，经度数组，格网数组
    """
    if res_lonlat == 1:
        lat = np.arange(-89.5,89.6,res_lonlat)
        lon = np.arange(0.5,359.6,res_lonlat)
    elif res_lonlat == 0.5:
        lat = np.arange(-89.75,89.76,res_lonlat)
        lon = np.arange(0.25,359.76,res_lonlat)
    elif res_lonlat == 0.25:
        lat = np.arange(-89.875,89.876,res_lonlat)
        lon = np.arange(0.125,359.876,res_lonlat)
    grd = np.zeros((len(lat),len(lon)))
    if lon_range is None:
        grd[(lat>=lat_range[0])&(lat<=lat_range[1]),:] = 1
    else:
        lat_loc = np.where((lat>=lat_range[0])&(lat<=lat_range[1]))
        lon_loc = np.where((lon>=lon_range[0])&(lon<=lon_range[1]))
        latmin = np.min(lat_loc[0])
        latmax = np.max(lat_loc[0])
        lonmin = np.min(lon_loc[0])
        lonmax = np.max(lon_loc[0])
        grd[latmin:latmax+1,lonmin:lonmax+1] = 1

    return lat,lon,grd

def extract_mask_from_grd(grd,lat,lon,lat_range,lon_range=None):
    """对grd大小的格网提取mask,有效值赋1

    Args:
        grd (array): 零数组
        res_lonlat (float): 分辨率
        lat_range (tuple): 纬度范围
        lon_range (tuple): 经度范围

    Returns:
        array: 截取之后的纬度数组，经度数组，格网数组
    """
    grdm = np.zeros_like(grd)
    if lon_range is None:
        grdm[(lat>=lat_range[0])&(lat<=lat_range[1]),:] = 1
    else:
        lat_loc = np.where((lat>=lat_range[0])&(lat<=lat_range[1]))
        lon_loc = np.where((lon>=lon_range[0])&(lon<=lon_range[1]))
        latmin = np.min(lat_loc[0])
        latmax = np.max(lat_loc[0])
        lonmin = np.min(lon_loc[0])
        lonmax = np.max(lon_loc[0])
        grdm[latmin:latmax+1,lonmin:lonmax+1] = 1

    return grdm