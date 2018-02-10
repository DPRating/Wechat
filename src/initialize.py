# -*- coding: utf-8 -*-
# filename: initialize.py


import os
import time
import pandas as pd
from function import GetParentDir


def CreateFile(keys, values, dir, file, reqPrint=True):
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


def CreateLogFile(timestamp, timeinfo, parentDir):
    record = '[Initialize] Initialization is completed'
    keys = ['timestamp', 'timeinfo', 'record']
    values = [timestamp, timeinfo, record]
    dir = os.path.join(parentDir, 'log')
    file = 'log.csv'
    CreateFile(keys, values, dir, file)
    print(record)       
    
    
def Initialize():
    parentDir = GetParentDir()
    dir = os.path.join(parentDir, 'log')
    file = 'log.csv'
    if os.path.exists(os.path.join(dir,file)):
        print('Initialization is skipped cause index.csv already exists')
    else:
        timestamp = int(time.time())
        timeinfo = time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(timestamp))
        CreateLogFile(timestamp, timeinfo, parentDir)



