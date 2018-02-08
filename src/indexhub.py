# -*- coding: utf-8 -*-
# filename: indexhub.py


import os
import time
import pandas as pd
from initialize import GetParentDir


def GetIndexValue():
    refPath = os.path.join(GetParentDir(), 'ref', 'params.csv')
    df = pd.read_csv(refPath).set_index('key')
    '''
    # The logic below has been tranferred to Dapao30 code
    timediff = int(time.time())-int(df['value']['indexTime'])
    if timediff>3600:
        os.system('python ' + df['value']['indexCodePath'])
        indexPath = pd.read_csv(df['value']['indexPath'])
        dfindex = pd.read_csv(indexPath)
        indexTime = dfindex['timestamp'][len(dfindex)-1]
        indexValue = round(dfindex['index'][len(dfindex)-1], 2)
        df['value']['indexTime'] = indexTime
        df['value']['indexValue'] = indexValue
        df.to_csv(refPath)
    else:
        indexValue = df['value']['indexValue']
    '''
    indexValue = round(float(df['value']['indexValue']), 2)
    print indexValue
    return indexValue
    
    
