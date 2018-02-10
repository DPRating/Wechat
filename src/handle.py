# -*- coding: utf-8 -*-
# filename: handle.py


import os
import sys
import web
import reply
import receive
import hashlib
import pandas as pd
from function import GetToken, GetDapao30Value, GetDapao30Doc


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
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.Content in ['大炮30', '大炮综指']:
                    str1 = u'当前指数：'.encode('utf-8') + str(GetDapao30Value())
                    str2 = u'\n大炮综指是由市值前30的数字货币按市值加权得到的指数，'.encode('utf-8')
                    str3 = u'可以反映出市场整体行情，想进一步了解可回复「大炮综指详情」'.encode('utf-8')
                    content = str1 + str2 + str3
                elif recMsg.Content in ['大炮30详情', '大炮综指详情']:
                    content = str(GetDapao30Doc())
                else:
                    content = ''
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            else:
                print "bypass"
                return "success"
        except Exception, Argument:
            return Argument



