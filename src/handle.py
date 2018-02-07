

# filename: handle.py
import os
import sys
import web
import hashlib
import pandas as pd


class Handle(object):

    def getParentDir(self):
        path = os.path.dirname(os.path.realpath(sys.argv[0]))
        return os.path.dirname(path)

    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr

            parentDir = self.getParentDir()
            path = os.path.join(parentDir, 'ref', 'params.csv')
            token = pd.read_csv(path).set_index('key')['value']['token']

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print "handle/GET func: hashcode, signature: ", hashcode, signature
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception, Argument:
            return Argument