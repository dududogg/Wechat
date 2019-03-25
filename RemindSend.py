import connectserver as cs
import connectclient as cl
import time
import itchat

# itchat auto login and longtime stay
itchat.auto_login(hotReload=True)

# 事件提醒
# Mysql login & finish search
name = '葛亚东'
sql = "select * from main_list where Person = '{}'".format(name)
events = cs.update(sql)
number = len(events)

# Reminder
for i in range(0,number):
    remind_time = '{}'.format(events[i][4])
    if time.mktime(time.strptime(remind_time, '%Y-%m-%d %H:%M:%S')) > time.time():
        cl.SendMessage(name,'{} {} 需要完成'.format(events[i][4],events[i][1]))


