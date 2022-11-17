import numpy as np
import itertools

def left_divide(A,y):
    """matlab左除

    Args:
        A (array): 系数阵
        y (array): 常数阵
    """

    m,n=A.shape
    p=y.shape
    if(m!=p[0]):
        print('dimensions do not match!')
        return -1
    if(m==n):
        return np.linalg.solve(A,y)
    else:
        a = np.dot(A.T,A)
        b = np.dot(A.T,y)
        return np.linalg.solve(a,b)

def nchoosek(startnum,endnum,step=1,n=1):
    # * b = nchoosek(n,k) returns the binomial coefficient, defined as n!/(k!(n-k)!),
    c = []
    for i in itertools.combinations(range(startnum,endnum+1,step),n):
        c.append(list(i))
    return np.array(c)