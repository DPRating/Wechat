# -*- coding: utf-8 -*-
# filename: function.py


import os
import sys


def GetParentDir():
    path = os.path.dirname(os.path.realpath(sys.argv[0]))
    return os.path.dirname(path)


def GetToken():
    paramPath = os.path.join(GetParentDir(), 'ref', 'param.json')
    with open(paramPath) as f:
        param = json.load(f)
    

def GetDapao30():
    paramPath = os.path.join(GetParentDir(), 'ref', 'param.json')
    with open(paramPath) as f:
        param = json.load(f)
    return param['dapao30Value']

