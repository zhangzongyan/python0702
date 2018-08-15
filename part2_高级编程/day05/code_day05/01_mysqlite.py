
import sqlite3

# 连接sqlite3
conn = sqlite3.connect("./test.db")

# 游标对象
c = conn.cursor()

# 执行sql语句 创建表
c.execute('''CREATE TABLE IF NOT EXISTS 
student(no INTEGER PRIMARY KEY AUTOINCREMENT , name varchar(20) NOT NULL , score integer)''')

# 插入
c.execute('''INSERT INTO student(name, score) VALUES ("caishaowei", 100)''')

# 查询
c.execute('''SELECT * FROM student''')
res = c.fetchall()
print(res)

# 关闭游标
c.close()

# 提交
conn.commit()

# 关闭
conn.close()


