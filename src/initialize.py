# -*- coding: utf-8 -*-
# filename: initialize.py


import os
import sys
import time
import pandas as pd


def GetParentDir():
    path = os.path.dirname(os.path.realpath(sys.argv[0]))
    return os.path.dirname(path)


def CreateRecord(keys, values, dir, file, reqPrint=False):
    df = {keys[0]:[values[0]]}
    for i in range(1,len(keys)):
        df[keys[i]] = [values[i]]
    df = pd.DataFrame(df)
    df = df[keys]

    if not os.path.exists(dir):
        os.mkdir(dir)
    df.to_csv(os.path.join(dir,file), index=False)
    if reqPrint:
        print(file+' created')

    
def AppendRecord(keys, values, dir, file, reqPrint=False):
    df = {keys[0]:[values[0]]}
    for i in range(1,len(keys)):
        df[keys[i]] = [values[i]]
    df = pd.DataFrame(df)
    df = df[keys]
    df.to_csv(os.path.join(dir,file), mode='a', header=False, index=False)
    if reqPrint:
        print(file+' updated')
        
        
def RegisterIndex():
    parentDir = GetParentDir()
    refPath = os.path.join(parentDir, 'ref', 'params.csv')
    indexPath = pd.read_csv(refPath).set_index('key')['value']['indexPath']
    df = pd.read_csv(indexPath)
    indexValue = int(df['index'][len(df)-1]*100)/100
    indexTime = df['timestamp'][len(df)-1]
    print ('Index value is '+str(indexValue)+' at '+str(indexTime))
    
    keys = ['indexValue', 'indexTime']
    values = [indexValue, indexTime]
    dir = os.path.dirname(refPath)
    file = 'params.csv'
    AppendRecord(keys, values, dir, file, reqPrint=True)

    
def LaunchIndexProgram():
    parentDir = GetParentDir()
    refPath = os.path.join(parentDir, 'ref', 'params.csv')
    indexCodePath = pd.read_csv(refPath).set_index('key')['value']['indexCodePath']
    os.system('python ', indexCodePath)
    
    
def Initialize():
    dir = os.path.join(GetParentDir(), 'log')
    file = 'log.csv'
    if os.path.exists(os.path.join(dir,file)):
        print(file + ' already exists')
    else:
        ts = int(time.time())
        readableTime = time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(ts))
        record = 'Log.csv created'
        keys = ['timestamp', 'datetime', 'record']
        values = [ts, readableTime, record]
        CreateRecord(keys, values, dir, file, reqPrint=True)
        RegisterIndex()
        LaunchIndexUpdate()



