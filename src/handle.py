# -*- coding: utf-8 -*-
# filename: handle.py


import os
import sys
import web
import reply
import receive
import hashlib
import pandas as pd
from function import GetToken, GetDarpal30Value, GetDarpal30Doc, GetBvixValue, GetBvixDoc


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
                if recMsg.Content in ['大炮综指', '大炮30', 'Darpal30']:
                    str1 = u'当前指数：'.encode('utf-8') + str(GetDarpal30Value())
                    str2 = u'\n大炮综指是由市值前30的数字货币按市值加权得到的指数，'.encode('utf-8')
                    str3 = u'可以反映出市场整体行情，想进一步了解可回复「大炮综指详情」'.encode('utf-8')
                    content = str1 + str2 + str3
                elif recMsg.Content in ['大炮综指详情', '大炮30详情']:
                    content = str(GetDarpal30Doc())
                elif recMsg.Content in ['BVIX', '恐慌指数', '波动率指数']:
                    str1 = u'当前指数：'.encode('utf-8') + str(GetBvixValue())
                    str2 = u'\nBVIX恐慌指数是从比特币期权市场中提取出的未来30天隐含波动率，'.encode('utf-8')
                    str3 = u'指数值越高意味着比特币未来价格的不确定性越大，'.encode('utf-8')
                    str4 = u'想进一步了解可回复「BVIX详情」'.encode('utf-8')
                    content = str1 + str2 + str3 + str4
                elif recMsg.Content in ['BVIX详情']:
                    content = str(GetBvixDoc())
                else:
                    content = ''
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            else:
                print "bypass"
                return "success"
        except Exception, Argument:
            return Argument



