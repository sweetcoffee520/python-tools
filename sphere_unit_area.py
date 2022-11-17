import numpy as np

def sphere_unit_area(minlat,maxlat,lonres,r):
    """计算弧面面积

    Args:
        minlat (float): 最小纬度
        maxlat (float): 最大纬度
        lonres (float)): 经度分辨率
        r (float): 球体半径

    Returns:
        array: 弧面面积
    """

    area = np.abs(np.sin(np.deg2rad(maxlat))-np.sin(np.deg2rad(minlat)))*np.deg2rad(lonres)*r**2

    return area