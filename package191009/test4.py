# __name__ + __main__ + python -m/-u
print("*****进一步理解 from...import *****")
"""
虽然只导入 test4A 中的 PI 变量
但依旧运行了 testA 的 print() 方法
故通过 from...import 引入模块的同时会将模块执行一遍
"""
print("this is line 15 of the test16.py")

from test4A import PI

# from test4A import *
# main()  #只引入了 PI ，并未引入 main()
print("this is line 17 of the test4.py")


def calc_round_area(radius):
    return PI * (radius ** 2)


def main():
    print("round area:", calc_round_area(2))


"""
在引入的模块中也存在 main() 但未被引用
若引用则会被覆盖，除非在覆盖前或赋值给新变量
"""
main()

print("*****模块引用与模拟程序接口*****")
"""
(改动部分在 test4B.py 中,包含 __name__ 与 __main__ 之间的关系)
"""
from test4B import E


def mantissa(E):
    return E - 2


def main():
    print("the mantissa of E:", mantissa(E))


main()

"""
运行 python 程序的若干种方式
<1>python xxx.py         直接运行 xxx.py 文件。把 xxx.py 文件所在的目录放到 sys.path 属性中
<2>python -m xxx.py      把 xxx.py 当做模(mú)板运行。把输入命领所在的文件(即当前工作路径)放到 sys.path 属性中
<3>python -u xxx.py      不经缓存直接把输出重定向到日志文件?

 sys.path 是什么? 见 test5.py

"""
import sys

print(sys.path)
"""
将目录转到 package191009 的父目录下
分别执行 python -m package191009 和 python package191009
python package191009         仅执行 __main__.py
python -m package191009      __init__.py 和 __main__.py 都依次执行

 __main__.py 是一个包或目录的入口程序
 无论 python package 或 python -m package ，__min__.py均被执行
"""
