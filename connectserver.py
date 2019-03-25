import pymysql


def update(Sql):
    db = pymysql.connect('103.40.18.51', 'reminder','Geyadong123','Reminder')
    cursor = db.cursor()
    cursor.execute(Sql)
    results = cursor.fetchall()
    return(results)
    db.close()


def insert(Sql):
    db = pymysql.connect('103.40.18.51', 'reminder', 'Geyadong123', 'Reminder')
    cursor = db.cursor()
    try:
        cursor.execute(Sql)
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    db.close()