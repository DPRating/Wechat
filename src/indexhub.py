

# filename: indexhub.py
import os
import time
import pandas as pd
from initialize import GetParentDir


def GetIndexValue():
    refPath = os.path.join(GetParentDir(), 'ref', 'params.csv')
    df = pd.read_csv(refPath).set_index('key')
    timediff = int(time.time())-int(df['value']['indexTime'])
    if timediff>3600:
        indexPath = pd.read_csv(df['value']['indexPath'])
        dfindex = pd.read_csv(indexPath)
        indexTime = dfindex['timestamp'][len(dfindex)-1]
        indexValue = int(dfindex['index'][len(dfindex)-1]*100)/100
        df['value']['indexTime'] = indexTime
        df['value']['indexValue'] = indexValue
        df.to_csv(refPath)
    else:
        indexValue = df['value']['indexValue']
    return indexValue
    
    
