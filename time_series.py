import numpy as np

from .polygon import inpolygon
from . import weight_mean
from . import fit_function as ff
from scipy.optimize import curve_fit
from . import extract_function


def grd_series_latitudinal(grd, nannum, lat, lat_range=None):
    """ 计算mask之后的时间序列,纬度加权

    Args:
        grd (array): 格网数组
        lat (array): 纬度数组
        lat_rane (tuple): 纬度范围
        nannum (float or int): 无效值大小

    Returns:
        array: 时间序列
    """
    row,col,_ = np.shape(grd)
    mask = np.ones(len(row),len(col))
    mask[grd[...,0]==nannum] = 0
    if lat_range is None:
        weighted_ave = weight_mean.latitudinal_weight(grd, lat, mask)
    else:
        loc = (lat>=lat_range[0])&(lat<=lat_range[1])
        weighted_ave = weight_mean.latitudinal_weight(grd[loc,:,:], lat[loc], mask[loc,:])
    return weighted_ave


def grd_series_area(grd, res, nannum, lat, lat_range = None):
    """ 计算mask之后的时间序列,面积加权

    Args:
        grd (array): 格网数组
        lat (array): 纬度数组
        lat_range (tuple): 纬度范围
        res (float): 格网分辨率大小
        nannum (float or int): 无效值大小

    Returns:
        array: 时间序列
    """
    row,col,_ = np.shape(grd)
    mask = np.ones(len(row),len(col))
    mask[grd[...,0]==nannum] = 0
    if lat_range is None:
        weighted_ave = weight_mean.area_weight(grd, lat, res, mask)
    else:
        loc = (lat>=lat_range[0])&(lat<=lat_range[1])
        weighted_ave = weight_mean.area_weight(grd[loc,:,:], lat[loc], res, mask[loc,:])

    return weighted_ave


def global_mass_area_series(grd,lat_range,lon_range=None):
    """计算全球格网中区域的时间序列

    Args:
        grd (array): 格网数组
        lat_range (tuple): 纬度范围
        lon_range (tuple): 经度范围,默认为无

    Returns:
        weighted_average (array): 纬度加权后时间序列
    """
    grd_shape = np.shape(grd)
    if grd_shape[0] ==180:
        res_lonlat = 1
        lat = np.arange(-89.5,89.6,res_lonlat)
    elif grd_shape[0] == 360:
        res_lonlat = 0.5
        lat = np.arange(-89.75,89.76,res_lonlat)
    elif grd_shape[0] == 720:
        res_lonlat = 0.25
        lat = np.arange(-89.875,89.876,res_lonlat)
    area_mask = np.zeros(np.shape(grd[:, :, 0]))
    extract_function.extract_mask(area_mask,res_lonlat,lat_range,lon_range)
    weighted = np.cos(np.deg2rad(lat[:,None]))*area_mask
    weighted_average = np.sum(grd*weighted[...,None])/np.sum(weighted)
    return weighted_average


def series_latitudinal(grd, mask, lat, lat_range=None):
    """计算给定格网的时间序列，纬度加权

    Args:
        grd (array): 格网数组
        mask (array): 掩膜格网数组
        lat (array): 纬度数组
        lat_range (tuple): 纬度范围

    Returns:
        array: 时间序列
    """
    if lat_range is None:
        weighted_average = weight_mean.latitudinal_weight(grd, lat, mask)
    else:
        loc = (lat>=lat_range[0])&(lat<=lat_range[1])
        weighted_average = weight_mean.latitudinal_weight(grd[loc,:,:], lat[loc], mask[loc,:])

    return weighted_average

def series_latitudinal_mask(grd,mask,lat,lat_range=None):
    """计算变化mask的时间序列,纬度加权

    Args:
        grd (array): 格网数组
        mask (array): 掩膜格网数组,与grd大小相同
        lat (array): 纬度数组
        lat_range (tuple): 纬度范围
    """
    if lat_range is None:
        weighted_average = weight_mean.latitudinal_weight_mask(grd, lat, mask)
    else:
        loc = (lat>=lat_range[0])&(lat<=lat_range[1])
        weighted_average = weight_mean.latitudinal_weight_mask(grd[loc,:,:], lat[loc], mask[loc,:,:])

    return weighted_average

def series_area(grd, mask, res, lat, lat_range = None):
    """计算给定格网的时间序列，面积加权

    Args:
        grd (array): 格网数组
        ocean_mask (array): 海洋掩膜格网数组
        lat (array): 纬度数组
        lat_range (tuple): 纬度范围
        res (float): 格网分辨率大小

    Returns:
        array: 海洋时间序列
    """
    if lat_range is None:
        weighted_average = weight_mean.area_weight(grd, lat, res, mask)
    else:
        loc = (lat>=lat_range[0]&lat<=lat_range[1])
        weighted_average = weight_mean.area_weight(grd[loc,:,:], lat[loc], res, mask[loc,:])

    return weighted_average

def time_series_remove_seasonal_cycle(t,y):
    """移除周期性的时间序列

    Args:
        t (array): 时间数组
        y (array): y值

    Returns:
        array: 移除周期性后的时间序列
    """

    popt,_= curve_fit(ff.annual_seasonal_trend,t,y,p0=[1,1,1,1,1,1])
    y_fit = y - (ff.annual_seasonal_trend(t,*popt)-ff.line_trend(t,*popt))

    return y_fit