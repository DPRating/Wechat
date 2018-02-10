# -*- coding: utf-8 -*-
# filename: handle.py


import os
import sys
import web
import reply
import receive
import hashlib
import pandas as pd
from function import GetToken, GetDapao30


class Handle(object):
    
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = GetToken()
            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception, Argument:
            return Argument

    def POST(self):
        try:
            webData = web.data()
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                if recMsg.Content in ['大炮30', '大炮综指']:
                    toUser = recMsg.FromUserName
                    fromUser = recMsg.ToUserName
                    suffix = u'\n回复「大炮综指详情」可获取相关文章'.encode('utf-8')
                    content = str(GetDapao30()) + suffix
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



