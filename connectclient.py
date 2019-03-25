import itchat
#from itchat.content import TEXT

@itchat.msg_register('TEXT')
# def simple_reply(msg):
#     print(msg.text)
def text_reply(msg):
    # 当消息不是由自己发出的时候
    if not msg['FromUserName'] == myUserName:
        # 发送一条提示给文件助手
        itchat.send_msg(u"[%s]收到好友@%s 的信息：%s\n" %
                        (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
                         msg['User']['NickName'],
                         msg['Text']), 'filehelper')
        # 回复给好友
        return u'[自动回复]您好，我现在有事不在，一会再和您联系。\n已经收到您的的信息：%s\n' % (msg['Text'])


#itchat.auto_login(enableCmdQR=2, hotReload=True)
def login():
    itchat.auto_login(hotReload=True)
    itchat.run()

def SendMessage(name, message):
    target = itchat.search_friends(nickName=name)
    userName = target[0]['UserName']
    itchat.send(msg=message, toUserName= userName )

#  @itchat.msg_register(Text)
#  def Simple_reply(msg):
#      itchat.send_msg('已经收到了文本消息，消息内容为%s'%'Text',toUserName=msg['FromUserName'])
#      return "T reveived: %s" % "Text"

