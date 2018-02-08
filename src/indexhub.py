# -*- coding: utf-8 -*-
# filename: indexhub.py


import os
import time
import pandas as pd
from initialize import GetParentDir


def GetIndexValue():
    print "entered GetIndexValue"
    refPath = os.path.join(GetParentDir(), 'ref', 'params.csv')
    df = pd.read_csv(refPath).set_index('key')
    timediff = int(time.time())-int(df['value']['indexTime'])
    print "before index calc"
    if timediff>1:
        os.system('python ' + df['value']['indexCodePath'])
        indexPath = pd.read_csv(df['value']['indexPath'])
        dfindex = pd.read_csv(indexPath)
        indexTime = dfindex['timestamp'][len(dfindex)-1]
        indexValue = int(dfindex['index'][len(dfindex)-1]*100)/100
        df['value']['indexTime'] = indexTime
        df['value']['indexValue'] = indexValue
        df.to_csv(refPath)
    else:
        indexValue = df['value']['indexValue']
    print "after index calc"
    return indexValue
    
    
