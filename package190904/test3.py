# 字符串(String)(+引号+转义符+截取)、import与from...import、print
print("*****字符串*****")
str="123abc"   # python的字符串不可改变
print(str)
print(str[0])
print(str[0:])
print(str[:4])
print(str[0:4])
print(str[0:-4])
print(str*2)
print(str+"ABC")
print('hello\nworld')   # 输出 hello 后换行
print(r'hello\nworld')   # 字符串前添加 r (raw,即raw string)，表示原始字符串，不会发生转义

print("*****import与from...import*****")
"""
在 python 用 import 或者 from...import 来导入相应的模块。
将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *
"""
# import sys
# print('命令行参数为:')
# for i in sys.argv:
#     print(i)
# print('\n python 路径为',sys.path)
print("----------")
from sys import argv,path
print('path:',path)

print("*****print*****")
print("13579",end="*")
print("24680",end="$")
