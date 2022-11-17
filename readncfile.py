'''
Author: sweetcoffee qq791227132@gmail.com
Date: 2022-04-28 22:20:46
LastEditors: sweetcoffee qq791227132@gmail.com
LastEditTime: 2022-06-26 13:55:18
FilePath: /python_code/tools/readncfile.py
Description: 

Copyright (c) 2022 by sweetcoffee qq791227132@gmail.com, All Rights Reserved.
'''
from netCDF4 import Dataset
import numpy as np
def readGlobalAttrs(path):
    nc_file = Dataset(path)
    attr_list = []
    global_attr = dict()
    # print 'Global attributes:'
    for attr_name in nc_file.ncattrs():
        # print attr_name, '=', getattr(nc_file, attr_name)
        attr_list.append(attr_name)
        atts = getattr(nc_file, attr_name)
        global_attr.update({attr_name:atts})
    return attr_list, global_attr


# --------------------------------------------------
# read and return variables and their attributes
# --------------------------------------------------


def readVars(path):
    # print 'Variables:'
    # dictionary of variables:values
    nc_file = Dataset(path)
    var_attr_dict = dict()
    var_data_dict = dict()
    var = nc_file.variables.keys()
    for var_name in var:
        attr = nc_file.variables[var_name]
        vardata = nc_file.variables[var_name][:].data
        try:
            if attr._FillValue is not None:
                vardata[vardata==attr._FillValue]=np.nan
        except:
            pass
        try:
            if attr.FillValue_ is not None:
                vardata[vardata==attr.FillValue_]=0
        except:
            pass
        try:
            if attr.valid_max is not None and attr.valid_min is not None:
                vardata[(vardata<attr.valid_min)|(vardata>attr.valid_max)]=np.nan
        except:
            pass

        if np.ndim(vardata)==3:
            vardata = np.transpose(vardata,(1,2,0))
            # vardata.transpose(1,2,0)
        elif np.ndim(vardata) == 4:
            vardata = vardata.transpose(2,3,1,0)

        var_attr_dict.update({var_name:attr})
        var_data_dict.update({var_name:vardata})
    return var, var_attr_dict, var_data_dict