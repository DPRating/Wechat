

# filename: log.py
import os
import sys
import time
import pandas as pd


def GetParentDir():
    path = os.path.dirname(os.path.realpath(sys.argv[0]))
    return os.path.dirname(path)


def CreateRecord(keys, values, dir, file):
    df = {keys[0]:[values[0]]}
    for i in range(1,len(keys)):
        df[keys[i]] = [values[i]]
    df = pd.DataFrame(df)
    df = df[keys]

    if not os.path.exists(dir):
        os.mkdir(dir)
    df.to_csv(os.path.join(dir,file), index=False)
    print(file+' created')


def CreateLog():
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
        CreateRecord(keys, values, dir, file)




