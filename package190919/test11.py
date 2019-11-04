# 获取模块的属性列表+查看列表的方法+内存地址

# 全局变量
# import __builtin__
# __builtin__.__dict__["_"] = lambda argument:argument
# __builtin__.__dict__["printex"] = printex
# __builtin__.__dict__["get_printex_str"] = get_printex_str

# 获取全局变量类型以及内存地址
na=12  #普通变量
na1=34
def abc():  #方法
    pass
class fun:  #类
    pass

print(type(na))  #查看 na 的类型
print(type(fun))  #查看 fun类 的类型

print("获得当前模块的属性列表")
print("dir():",dir())

print("查看列表的方法")
print("dir([]):",dir([]))  #查看列表的方法

# li.__dict__= lambda ar:Argume
for v in dir() :
    i=id(v)  #迭代获取变量名的内存地址
    tem=eval(v)  #转化，否则type()的结果都是str
    print(v,":",i,",type:",type(tem))  #变量名+地址+类型