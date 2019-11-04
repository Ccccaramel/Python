# MYSQL
import MySQLdb.connections


def show():
    num = 0
    for x in mycursor:
        print("<{}> : {}".format(num, x))
        num += 1


mydb = MySQLdb.connect(
    host="127.0.0.1",
    user="root",
    password="123456"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("create database test_db")  # 创建数据库
mycursor.execute("show databases")  # 查看数据库,注意: databases 是复数
mycursor.execute("drop database test_db")  # 删除数据库,注意: databases 是复数

show()

mycursor.execute("use test_db")  # 选择数据库,说通俗点就是进入指定数据库,当然你也可以在连接数据库的时候加上 database="test_db"

mycursor.execute("create table user (name varchar(24),age int,gender int)")  # 创建表

mycursor.execute("show tables")  # 查看数据库所有表,注意: tables 是复数

show()

mycursor.execute("alter table user add column id int auto_increment primary key")  # 添加列并设置为自增主键

mycursor.execute("alter table user modify column gender varchar(4)")  # 更改列属性

mycursor.execute("insert into user(name,age,gender) values(%s,%d,%s)", ("Tom".encode("utf-8"), 12, "男".encode("utf-8")))  # 插入语句

mydb.commit()  # 数据表内容有更新必须执行此语句

print(" 1 条记录已插入,ID: {}".format(mycursor.lastrowid))

mycursor.execute("select * from user")

myresult = mycursor.fetchall()  # fetchall() 获取所有记录

for x in myresult:
    print(x)

myresult = mycursor.fetchone()  # 读取一条字段
print(myresult)
