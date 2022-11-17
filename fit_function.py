import numpy as np

def annual_seasonal_trend(t, *p):
    """带有周年项和半周年项的拟合函数

    Args:
        t (numpy.dtype(float)): 时间数组
    """
    return p[0]+p[1]*t+p[2]*np.sin(2*np.pi*t)+p[3]*np.cos(2*np.pi*t)+p[4]*np.sin(4*np.pi*t)+p[5]*np.cos(4*np.pi*t)

def seasonal_trend(t, *p):
    """带有周年项的拟合函数

    Args:
        t (numpy.dtype(float)): 时间数组
    """
    return p[0]+p[1]*t+p[2]*np.sin(2*np.pi*t)+p[3]*np.cos(2*np.pi*t)

def line_trend(t, *p):
    """只有线性项的拟合函数

    Args:
        t (numpy.dtype(float)): 时间数组
    """
    return p[0]+p[1]*t

def acceleration(t, *p):
    """带有线性项和加速度项的拟合函数

    Args:
        t (numpy.dtype(float)): 时间数组
    """
    return p[0]+p[1]*t+p[2]*t**2