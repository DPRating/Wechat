

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
    
