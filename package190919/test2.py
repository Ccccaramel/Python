# 获取变量类型+判断变量类型+万物皆对象(object)
from inspect import isfunction
num1 = 123
num2 = 123.123
str1 = "123"
var1 = 'Hello World!'
list1 = ['Google', 'Runoob', 1997, 2000]
tup1 = ('Google', 'Runoob', 1997, 2000)
dict1 = {'abc': 456}
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}


class cla(object):
    pass


class cla0(object):
    pass


cla1 = cla()


def fun1():
    return 0


def fun2():
    pass

#  通过 isinstance() 判断对象类型，但无法判断方法和实例


if isinstance(num1, int):
    print("num1's type is int")
else:
    print("num1's type is not int")

if (type(fun1)) == type(fun2):
    print("f1's type is def")
else:
    print("f1's type is not def")

print("type(cla):", type(cla))


print(type(num1))
print(type(num2))
print(type(str1))
print(type(list1))
print(type(tup1))
print(type(dict1))
print(type(basket))
print(type(fun1))
print(type(cla))
print(type(cla1))

# 通过 type() is [typename] 判断对象类型，但无法判断方法和实例
if type(num1) is int:
    print("num1 is int!")
else:
    print("num1 is not int!")

if type(dict1) is dict:
    print("dict1 is dict!")
else:
    print("dict1 is not dict!")

if type(cla) is type:
    print("cla is type!")
else:
    print("cla is not type!")


k = "12"
if k.isnumeric():
    print("ok")

# 只能判断对象是不是类，无法判断是否为实例
try:
    if issubclass(cla, object):
        print("cla is class!")
except:
    print("cla is not class!")

if isinstance(cla1, object):
    print("在 python 中万物皆对象")
