# -*- coding: utf-8 -*-
# filename: indexhub.py


import os
import time
import pandas as pd
from initialize import GetParentDir


def GetIndexValue():
    refPath = os.path.join(GetParentDir(), 'ref', 'params.csv')
    print refPath
    df = pd.read_csv(refPath).set_index('key')
    print df
    timediff = int(time.time())-int(df['value']['indexTime'])
    print df['value']['indexCodePath']
    '''
    if timediff>3600:
        # os.system('python ' + df['value']['indexCodePath'])
        print 'back to GetIndexValue'
        indexPath = pd.read_csv(df['value']['indexPath'])
        print indexPath
        dfindex = pd.read_csv(indexPath)
        print dfindex
        indexTime = dfindex['timestamp'][len(dfindex)-1]
        print indexTime
        indexValue = round(dfindex['index'][len(dfindex)-1], 2)
        print indexValue
        df['value']['indexTime'] = indexTime
        df['value']['indexValue'] = indexValue
        print df
        df.to_csv(refPath)
    else:
        indexValue = df['value']['indexValue']
    '''
    indexValue = df['value']['indexValue']
    print "after index calc"
    return indexValue
    
    
