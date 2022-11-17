'''
Author: sweetcoffee qq791227132@gmail.com
Date: 2022-04-28 22:20:46
LastEditors: sweetcoffee qq791227132@gmail.com
LastEditTime: 2022-11-15 18:17:48
FilePath: /python_code/tools/polygon.py
Github: https://github.com/sweetcoffee520
Description: 
Copyright (c) 2022 by sweetcoffee qq791227132@gmail.com, All Rights Reserved.
'''
import numpy as np
import shapely.geometry
from matplotlib.path import Path

# Points located inside or on edge of polygonal region
def inpolygon(xq, yq, xv, yv):
    shape = xq.shape
    xq = xq.reshape(-1)
    yq = yq.reshape(-1)
    xv = xv.reshape(-1)
    yv = yv.reshape(-1)
    q = [(xq[i], yq[i]) for i in range(xq.shape[0])]
    p = Path([(xv[i], yv[i]) for i in range(xv.shape[0])])
    return p.contains_points(q).reshape(shape)

def boundary2mask(boundary_file, resolution):
    """
    将边界转换为mask
    boundary_file: 边界文件(区域边界的经纬度)
    resolution: 分辨率大小
    """

    with open(boundary_file,'r') as f:
        # _表示这个变量不需要
        boundary = np.reshape(np.array(f.read().split()),(-1,2))
    x = boundary[:,0].astype(np.float32)
    y = boundary[:,1].astype(np.float32)
    x[x<0] += 360
    lonmin = np.min(x)
    lonmax = np.max(x)
    latmin = np.min(y)
    latmax = np.max(y)
    if resolution == 1:
        lat = np.arange(-89.5,89.6,resolution)
        lon = np.arange(0.5,359.6,resolution)
    elif resolution == 0.5:
        lat = np.arange(-89.75,89.76,resolution)
        lon = np.arange(0.25,359.76,resolution)
    elif resolution == 0.25:
        lat = np.arange(-89.875,89.876,resolution)
        lon = np.arange(0.125,359.876,resolution)

    lg_mask = np.zeros((len(lat),len(lon)))
    for i in range(len(lat)):
        for j in range(len(lon)):
            if lat[i]>=latmin and lat[i]<=latmax and lon[j]>=lonmin and lon[j]<=lonmax:
                in_ = inpolygon(lon[j],lat[i],x,y)
                if in_ == True:
                    lg_mask[i,j] = 1
    if lonmin<0:
        temp = lg_mask.copy()
        middle_location = int(len(lon)/2)
        lg_mask[:,:middle_location] = temp[:,middle_location:]
        lg_mask[:,middle_location:] = temp[:,:middle_location]

    return lat,lon,lg_mask

# Create buffer around points, lines, or polyshape objects
def polybuffer(P,d):
    if isinstance(P,shapely.geometry.Point):
        return P.buffer(d)
    elif isinstance(P,shapely.geometry.LineString):
        return P.buffer(d)
    elif isinstance(P,shapely.geometry.Polygon):
        return P.buffer(d)
    elif isinstance(P,np.ndarray):
        return shapely.geometry.MultiPolygon([polybuffer(shapely.geometry.Point(p),d) for p in P])
    elif isinstance(P,shapely.geometry.MultiPolygon):
        return shapely.geometry.MultiPolygon([polybuffer(shapely.geometry.Point(p),d) for p in P])
    else:
        raise TypeError('{} is not a valid type'.format(type(P)))

def equidistant_zoom_contour(contour, margin):
    """
    等距放大轮廓
    contour: 输入轮廓
    margin: 放大距离
    :return: 输出轮廓
    """
    # 轮廓长度
    length = contour.shape[0]
    # 轮廓中心坐标
    center = np.array([np.mean(contour[:, 0]), np.mean(contour[:, 1])])
    # 轮廓放大后的轮廓
    new_contour = np.zeros((length, 2))
    # 等距放大轮廓
    for i in range(length):
        if contour[i,0]>center[0]:
            new_contour[i,0] = contour[i,0] + margin
        elif contour[i,0]<center[0]:
            new_contour[i,0] = contour[i,0] - margin
        if contour[i,1]>center[1]:
            new_contour[i,1] = contour[i,1] + margin
        elif contour[i,1]<center[1]:
            new_contour[i,1] = contour[i,1] - margin
    return new_contour

CSR_lat_SH,CSR_lon_SH,mask30 = boundary2mask('mask.txt',0.5)