# -*- coding: utf-8 -*-
# filename: function.py


import os
import sys
import json
import pandas as pd


def GetParentDir():
    path = os.path.dirname(os.path.realpath(sys.argv[0]))
    return os.path.dirname(path)


def GetToken():
    path = os.path.join(GetParentDir(), 'ref', 'param.json')
    with open(path) as f:
        param = json.load(f)
    return param['token']
    

def GetDarpal30Value():
    path = os.path.join(GetParentDir(), 'ref', 'index.csv')
    df = pd.read_csv(path).set_index('name')
    return df['value']['Darpal30']


def GetDarpal30Doc():
    path = os.path.join(GetParentDir(), 'ref', 'index.csv')
    df = pd.read_csv(path).set_index('name')
    return df['doc']['Darpal30']

def GetBvixValue():
    path = os.path.join(GetParentDir(), 'ref', 'index.csv')
    df = pd.read_csv(path).set_index('name')
    return df['value']['BVIX']


def GetBvixDoc():
    path = os.path.join(GetParentDir(), 'ref', 'index.csv')
    df = pd.read_csv(path).set_index('name')
    return df['doc']['BVIX']
