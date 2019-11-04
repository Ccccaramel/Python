# 运算符(算术运算符、位运算符、成员运算符、身份运算符)
print("-----算术运算符-----")
a,b,c=2,3,11
print("a=",a,",b=",b,",c=",c)
print("a的b次幂:a**b=",a**b)
print("取整除(向下取接近除数的整数):c//a=",c//a)
print("取整除(向下取接近除数的整数):(-c)//a=",(-c)//a)

print("-----位运算符-----")
x=60    #0011 1100
y=13    #0000 1101
z=0
c=x&y
print("x&y的值为:",c)
c=x|y
print("x|y的值为:",c)
c=x^y
print("x^y的值为:",c)
c=~x
print("~x的值为:",c)
c=x<<2
print("x<<2的值为:",c)
c=x>>2
print("x>>2的值为:",c)

print("-----成员运算符-----")
# 在指定的序列(字符串、列表、元组)中判断指定的值是否存在，返回值True或False
a=10
b=20
list=[1,2,3,4,5];

if(a in list):
    print("变量a在给定的列表中list中")
else:
    print("变量a不在给定的列表中list中")
if(b not in list):
    print("变量b不在给定的列表中list中")
else:
    print("变量b在给定的列表中list中")

a=2
if(a in list):
    print("变量a在给定的列表中list中")
else:
    print("变量a不在给定的列表中list中")

print("-----身份运算符-----")
# 判断两个标识符是不是引用同一个对象，返回值True或False
a=20
b=20
if(a is b):
    print("a和b有相同的标识")
else:
    print("a和b没有相同的标识")
if(id(a)==id(b)):
    print("a和b有相同的标识")
else:
    print("a和b没有相同的标识")

b=30
if(a is b):
    print("a和b有相同的标识")
else:
    print("a和b没有相同的标识")
if(a is not b):
    print("a和b没有相同的标识")
else:
    print("a和b有相同的标识")

"""

**                  (高)                指数 (最高优先级)
~ + -                                   按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
* / % //                                乘，除，取模和取整除
+ -                                     加法减法
>> <<                                   右移，左移运算符
&                                       位 'AND'
^ |                                     位运算符
<= < > >=                               比较运算符
<> == !=                                等于运算符
= %= /= //= -= += *= **=                赋值运算符
is is not                               身份运算符
in not in                               成员运算符
not and or          (低)                逻辑运算符
"""