#!/usr/bin/env python
# -*- coding :utf-8 -*-
#author:shirenxiang time:2019/12/24 17:57
# import MySQLdb
import pymysql.cursors

# 打开数据库连接
# db = pymysql.connector.connect("192.168.10.145", "root", "cntv4g", "hadoop", charset='utf8' )
db = pymysql.connect(host="192.168.10.145",user="root", passwd="cntv4g",database="hadoop")
# 使用cursor()方法获取操作游标
cursor = db.cursor()
sql="select *from hot_key"
# 使用execute方法执行SQL语句
# cursor.execute("SELECT VERSION()")
cursor.execute(sql)
# 使用 fetchone() 方法获取一条数据
# data = cursor.fetchone()
# 取出全部
data = cursor.fetchall()
for i in data:
    print(i)
# print(data)

# 关闭数据库连接
db.close()