'''
Author: sweetcoffee qq791227132@gmail.com
Date: 2022-04-28 22:20:46
LastEditors: sweetcoffee qq791227132@gmail.com
LastEditTime: 2022-07-19 17:19:14
FilePath: /python_code/tools/monte_carlo_rate_sigma.py
Github: https://github.com/sweetcoffee520
Description: 
Copyright (c) 2022 by sweetcoffee qq791227132@gmail.com, All Rights Reserved.
'''
import numpy as np
from scipy.fft import fft, ifft
from . import matlab_addition


# def monte_carlo_rate_sigma(t, y, trials_num):
#     N = len(t)
#     A = np.vstack((np.ones((1, N)), t)).T
#     # print(A)
#     para = matlab_addition.left_divide(A, y)
#     slopest = para[1]
#     residual = y - np.dot(A, para)
#     dsynth = np.zeros((np.size(t), trials_num),dtype='complex_')
#     strial = np.zeros(trials_num,dtype='complex_')

#     R = np.abs(fft(residual))
#     for i in range(trials_num):
#         if np.mod(i, 100) == 0:
#             pass

#         r = np.random.randn(int(N/2)-1)
#         p = np.insert(np.append(np.append(r, 0), -np.flipud(r)), 0, 0)*2*np.pi
#         dsynth[:, i] = slopest*t + ifft(R*np.exp(1j*p))
#         b = matlab_addition.left_divide(A, dsynth[:, i])
#         strial[i] = b[1]

#     smean = np.mean(strial) - slopest

#     # 自由度为n-1的残差方差
#     ssd = np.std(strial - slopest, ddof = 1)

#     return slopest, smean, ssd, strial

def monte_carlo_rate_sigma(t, y, trials_num):
    N = len(t)
    L = np.vstack((np.ones((1, N)), t)).T
    para = matlab_addition.left_divide(L, y)
    slopest = para[1]
    residual = y - np.dot(L, para)
    R = np.abs(fft(residual))
    strial = np.zeros(trials_num, dtype='complex_')
    dsynth = np.zeros((np.size(t), trials_num), dtype='complex_')
    for i in range(trials_num):
        r = np.random.randn(N//2-1,2)
        Rsynth = 0.707*((r[:,0]+1j*r[:,1])*R[1:N//2])
        # Rsynth = np.insert(np.append(np.append(Rsynth, 0), -np.flipud(Rsynth)), 0, R[0])
        Rsynth = np.insert(np.append(np.append(Rsynth,R[N//2]),np.flipud(np.conjugate(Rsynth))),0,R[0])
        dsynth[:,i] = slopest*t + ifft(Rsynth)
        b = matlab_addition.left_divide(L,dsynth[:,i])
        strial[i] = b[1]
    smean = np.mean(strial)-slopest+ifft(Rsynth)
    ssd = np.std(strial-slopest, ddof=1)
    return slopest, smean, ssd, strial