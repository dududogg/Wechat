import connectserver as cs
import connectclient as cl
import time
import itchat
from itchat.content import *



# friend example：
#<User: {'MemberList': <ContactList: []>, 'Uin': 0, 'UserName': '@22d04eb011b99283d237b963b28843c4', 'NickName': '葛亚东',
# 'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=679561237&username=@22d04eb011b99283d237b963b28843c4&skey=@crypt_ad485dd7_3bbd7751ec658f07a2ef41035ed2f1e0',
# 'ContactFlag': 3, 'MemberCount': 0, 'RemarkName': '', 'HideInputBarFlag': 0, 'Sex': 1, 'Signature': '', 'VerifyFlag': 0, 'OwnerUin': 0, 'PYInitial': 'GYD',
# 'PYQuanPin': 'geyadong', 'RemarkPYInitial': '', 'RemarkPYQuanPin': '', 'StarFriend': 0, 'AppAccountFlag': 0, 'Statues': 0, 'AttrStatus': 98343,
# 'Province': '江苏', 'City': '南京', 'Alias': '', 'SnsFlag': 49, 'UniFriend': 0, 'DisplayName': '', 'ChatRoomId': 0, 'KeyWord': 'gey', 'EncryChatRoomId': '',
# 'IsOwner': 0}>

@itchat.msg_register([TEXT])
def text_reply(msg):
    if not msg['FromUserName']=='@b9e5eadf1b6ff8168fc84f714967a99b97d82f909464e69b4d89f7c68d78ec16':
        msg.user.send('提醒要求已收到')
        userid = itchat.search_friends(userName=msg.FromUserName)['NickName']
        print(userid)
        print(msg.text)

# @itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
# def text_reply(msg):
#     msg.user.send('%s: %s' % (msg.type, msg.text))
#     userid = itchat.search_friends(userName=msg.FromUserName)['NickName']
#     print(userid,msg.text)

# @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
# def download_files(msg):
#     msg.download(msg.fileName)
#     typeSymbol = {
#         PICTURE: 'img',
#         VIDEO: 'vid', }.get(msg.type, 'fil')
#     return '@%s@%s' % (typeSymbol, msg.fileName)
#
# @itchat.msg_register(FRIENDS)
# def add_friend(msg):
#     msg.user.verify()
#     msg.user.send('Nice to meet you!')
#
# @itchat.msg_register(TEXT, isGroupChat=True)
# def text_reply(msg):
#     if msg.isAt:
#         msg.user.send(u'@%s\u2005I received: %s' % (
#             msg.actualNickName, msg.text))

itchat.auto_login(hotReload=True)
itchat.run()
a=itchat.search_friends(nickName='葛亚东')
print(a)