

# filename: handle.py
import os
import sys
import web
import receive
import reply
import hashlib
import pandas as pd


class Handle(object):
    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData
            # Write to log
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = "test"
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
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
