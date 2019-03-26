import connectserver as cs
import connectclient as cl
import time
import itchat

#TODO 如何实现轮巡，是否时间需要精确到秒

# itchat auto login and longtime stay
itchat.auto_login(hotReload=True)

# 事件提醒
# Mysql login & finish search
# TODO name
name = '葛亚东'
sql = "select * from main_list where Person = '{}'".format(name)
events = cs.update(sql)
number = len(events)

# Reminder
for i in range(0,number):
    remind_time1 = '{}'.format(events[i][4])
    remind_time2 = time.mktime(time.strptime(remind_time, '%Y-%m-%d %H:%M:%S'))
    if (remind_time2 > (time.time()+0.0417)) and (remind_time2 < (time.time()+0.83)):
        cl.SendMessage(name,'{} {} 需要完成'.format(events[i][4],events[i][1]))


