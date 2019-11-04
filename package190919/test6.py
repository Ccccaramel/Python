# 模块导入(异包同级*主动)
"""
调用与本模块的父级同级的目录下的子模块（异包）
需主动执行需要执行的方法或调用的变量
"""
import sys
sys.path.append("package190904A")   #相对路径
# sys.path.append("F:\PythonData\Practice\package190904A")  #绝对路径

# <方法一> 只导入模块名时，调用模块内的类、方法或变量前必须加上 包名. ,建议使用 <方法一>
# import test4A_1
# test4A_1.print_hi()
# print(test4A_1.str)

# <方法二> 意为导入模块内所有对象，当引入多个模块时注意避免同名情况
from test4A_1 import *
a=add(6,4)

try:
    if issubclass(a,object):
        print("cla1 is class!")
except:
    print("cla1 is not class!")

print("type(a):",type(a))
a.printf()
print_hi()
print(str)
add.say()