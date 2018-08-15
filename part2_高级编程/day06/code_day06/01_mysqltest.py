# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     01_mysqltest
   Description :
   Author :       zongyanzhang
   date：          2018/8/10
-------------------------------------------------
   Change Activity:
                   2018/8/10:
-------------------------------------------------
"""
__author__ = 'admin'

import mysql.connector

config = {
    'host': '127.0.0.1', # 连接地址
    'user': 'root', # 用户
    'password': '123', # 用户密码
    'port': 3306, # mysql服务端口
    'database': 'test', # 数据库名字
    'charset': 'utf8' # 编码
}

# 连接数据库
# mysql.connector.connetc(host="", user="")
conn = mysql.connector.connect(**config)

# 游标
c = conn.cursor()

# sql语句
c.execute("create table student(no INT NOT NULL, name CHAR (20))")

c.execute("insert into student(no, name) values(1, 'python')")

c.close()
conn.commit()
conn.close()

