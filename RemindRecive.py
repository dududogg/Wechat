import connectserver as cs
import connectclient as cl
import time
import itchat
from itchat.content import *




# 提醒事件录入
# wechat get message and auto-replay
@itchat.msg_register([TEXT])
def text_reply(msg):
    if not msg['FromUserName']=='@b9e5eadf1b6ff8168fc84f714967a99b97d82f909464e69b4d89f7c68d78ec16':
        msg.user.send('提醒要求已收到')
        username = itchat.search_friends(userName=msg.FromUserName)['NickName']
        print(username,msg.text)
        #Things & Remind_time can't seprated now, wait to resole.
        #TODO 拆分时间和提醒事项
        Record = msg.text.split('#')
        time1 = Record[0].ljust(14,'0')
        ThingS = Record[1]
        time2 = "{}-{}-{} {}:{}:{}".format(time1[0:4],time1[4:6],time1[6:8],time1[8:10],time1[10:12],time1[12:14])
        UpdateRemindSql = "INSERT INTO main_list (Person,Things,Update_time,Remind_time,Done) \
        VALUES ('{}','{}','{}','{}',{})".format(username,ThingS,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ,time2,'0')
        print(UpdateRemindSql)
        cs.insert(UpdateRemindSql)

# itchat auto login and longtime stay
# itchat.auto_login(hotReload=True)
# itchat.run()

cl.login()
