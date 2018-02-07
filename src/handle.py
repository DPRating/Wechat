# -*- coding: utf-8 -*-
# filename: handle.py


import os
import sys
import web
import receive
import reply
import hashlib
import pandas as pd
from initialize import GetParentDir
from indexhub import GetIndexValue


class Handle(object):
    def __init__(self):
        parentDir = GetParentDir()
        path = os.path.join(parentDir, 'ref', 'params.csv')
        path = pd.read_csv(path).set_index('key')['value']['indexPath']
        df = pd.read_csv(path)
        self.index = df['index'][len(df)-1]
        self.datetime = df['datetime'][len(df)-1]
        print ('Index value is '+str(self.index)+' at '+str(self.datetime))

    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData
            # Write to log
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                if recMsg.Content in ['大炮30', '大炮综指']:
                    toUser = recMsg.FromUserName
                    fromUser = recMsg.ToUserName
                    content = GetIndexValue()
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                else:
                    print "bypass"
                    return "success"
            else:
                print "bypass"
                return "success"
        except Exception, Argument:
            return Argument

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

    def getParentDir(self):
        path = os.path.dirname(os.path.realpath(sys.argv[0]))
        return os.path.dirname(path)
