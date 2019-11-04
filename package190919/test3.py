# 为以创建的类或对象添加新的方法
import sys
import os
import subprocess
class a:
    pass

def hello(self,name):
    print("Hello %s"%name)
a.hello=hello
a().hello("somebody")

def age(self,num):
    age=num
    print(age)
a.age=age
a().age(10)  #类直接调用时必须加括号

b=a()

b.hello("wuv")  #对象引用时无需括号

# a = dict(a=1,b=2,c=3) 
# for k,v in a.items():
#     print ('%s,%s'%(k,v))