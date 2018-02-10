# -*- coding: utf-8 -*-
# filename: function.py


import os
import sys
import json


def LoadParam():
    parentDir = os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[0])))
    paramPath = os.path.join(parentDir, 'ref', 'param.json')
    with open(paramPath) as f:
        param = json.load(f)
    token = param['token']
    dapao30Time = param['dapao30Time']
    dapao30Value = param['dapao30Value']
    return parentDir, token, dapao30Time, dapao30Value
    
