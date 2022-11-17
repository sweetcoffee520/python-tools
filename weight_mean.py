'''
Author: sweetcoffee qq791227132@gmail.com
Date: 2022-04-28 22:20:46
LastEditors: sweetcoffee qq791227132@gmail.com
LastEditTime: 2022-11-13 13:47:34
FilePath: /python_code/tools/weight_mean.py
Github: https://github.com/sweetcoffee520
Description: 
Copyright (c) 2022 by sweetcoffee qq791227132@gmail.com, All Rights Reserved.
'''
import numpy as np
from . import sphere_unit_area

def latitudinal_weight(grd,lat,grd_mask=None):
    """纬度加权

    Args:
        grd (array): 被加权格网
        lat (array): 纬度数组
        grd_mask (array): 掩膜格网

    Returns:
        array: 加权后的值
    """

    lat_mask = np.cos(np.deg2rad(lat))
    if grd_mask is None:
        ave_result = np.sum(grd*lat_mask[:,None,None],(0,1))/np.sum(np.repeat(lat_mask,np.size(grd,1)))
    else:
        ave_result = np.sum(grd*lat_mask[:,None,None]*grd_mask[...,None],(0,1))/np.sum(lat_mask[:,None]*grd_mask)

    return ave_result

def latitudinal_weight_mask(grd,lat,grd_mask):
    """变化mask的纬度加权

    Args:
        grd (array): 被加权格网
        lat (array): 纬度数组,与grd大小相同
        grd_mask (array): 掩膜格网

    Returns:
        array: 加权后的值
    """

    lat_mask = np.cos(np.deg2rad(lat))
    ave_result = np.sum(grd*lat_mask[:,None,None]*grd_mask,(0,1))/np.sum(lat_mask[:,None,None]*grd_mask,(0,1))

    return ave_result

def area_weight(grd,lat,res,grd_mask=None):
    """面积加权

    Args:
        grd (array): 被加权格网
        lat (array): 纬度数组
        res (float): 格网的分辨率大小
        grd_mask (array): 掩膜格网

    Returns:
        array: 加权后的值
    """

    radius = 6371004  # 地球平均半径：单位米
    area = np.zeros(len(lat))
    # 循环每个相邻纬度的单位经度面积大小
    for i in range(len(lat)):
        area[i] = sphere_unit_area.sphere_unit_area(lat[i]-res/2,lat[i]+res/2,res,radius)
    if grd_mask is None:
        ave_result = np.sum(grd*area[:,None,None],(0,1))/np.sum(np.repeat(area,np.size(grd,1)))
    else:
        ave_result = np.sum(grd*area[:,None,None]*grd_mask[...,None],(0,1))/np.sum(area[:,None]*grd_mask)
    return ave_result


