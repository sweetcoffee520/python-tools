'''
Author: sweetcoffee qq791227132@gmail.com
Date: 2022-04-28 22:20:46
LastEditors: sweetcoffee qq791227132@gmail.com
LastEditTime: 2022-11-24 10:07:40
FilePath: /python_code/tools/fit_caculate.py
Description: 

Copyright (c) 2022 by sweetcoffee qq791227132@gmail.com, All Rights Reserved.
'''
import numpy as np
import pandas as pd
from . import time_transfer as tt

def fit_caculate_line(t,y):
    if isinstance(t,pd.DatetimeIndex):
        t = tt.dateseries_to_timeseries(t)
    else:
        pass
    A = np.zeros((len(y),2))
    A[:,0] = np.ones((len(y)))
    A[:,1] = t
    para = np.dot(np.dot(np.linalg.inv(np.dot(A.T,A)),A.T),y) #(B^TPB)^-1*B^TPl
    fit_result = np.dot(A,para)
    # 验后方差
    residual =sum((y-fit_result)**2)/(len(y)-2)
    Qxx = np.linalg.inv(np.dot(A.T,A))
    # 验后方差乘上x的协因数阵得到x的协方差阵
    uncer = np.dot(residual,Qxx)

    return para,uncer

def fit_caculate_line_annual(t,y,*std):

    if isinstance(t,pd.DatetimeIndex):
        t = tt.dateseries_to_timeseries(t)
    else:
        pass
    # 等权最小二乘
    if len(std)==0:
        A = np.zeros((len(y),6))
        A[:,0] = np.ones((len(y)))
        A[:,1] = t
        A[:,2] = np.sin(2*np.pi*t)
        A[:,3] = np.cos(2*np.pi*t)
        A[:,4] = np.sin(4*np.pi*t)
        A[:,5] = np.cos(4*np.pi*t)
        # NBB^-1的逆为QXX
        para= np.linalg.inv(A.T@A)@A.T@y #(B^TPB)^-1*B^TPl
        fit_result = np.dot(A,para)
        residual =sum((y-fit_result)**2)/(len(y)-6)
        Qxx = np.linalg.inv(np.dot(A.T,A))
        uncer = np.dot(residual,Qxx)
    # 加权最小二乘
    elif (len(std))==1:
        P = np.diag(1/std) #设置权阵，对角阵，为1/std
        A = np.zeros((len(y),6))
        A[:,0] = np.ones((len(y)))
        A[:,1] = t
        A[:,2] = np.sin(2*np.pi*t)
        A[:,3] = np.cos(2*np.pi*t)
        A[:,4] = np.sin(4*np.pi*t)
        A[:,5] = np.cos(4*np.pi*t)
        # NBB^-1的逆为QXX
        para=np.linalg.inv(A.T@P@A)@A.T@P@y #(B^TPB)^-1*B^TPl
        fit_result = np.dot(A,para)
        residual =sum((y-fit_result)**2)/(len(y)-6)
        Qxx = np.linalg.inv(A.T@P@A)
        uncer = np.dot(residual,Qxx)

    return para,uncer