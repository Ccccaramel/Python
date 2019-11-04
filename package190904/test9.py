# 元组(一个元素+访问元组+修改元组×,连接组合√+删除元组+元组运算符+元组索引与截取+元组内置函数)
# 元组内元素不能修改
tup1=()  #创建空元组

print("-----一个元素-----")
# 元组只包含一个元素时,需要在元素后面添加逗号,否则括号会被当做运算符使用
tup2=(3)
print("type(tup2):",type(tup2))  #不加逗号,类型为整型
tup3=(3,)
print("type(tup3):",type(tup3))  #加上逗号,类型为元组

print("-----访问元组-----")
tup4=('google','taobao',1996,2009)
print("tup4[0]:",tup4[0])
print("tup4[1,4]:",tup4[1:4])

print("-----修改元组×,连接组合√-----")
tup5=('a','b','c')
tup6=('d','e','f')
# tup5[1]='z'  #报错
tup7=tup5+tup6
print("tup7:",tup7)

print("-----删除元组-----")
del tup7
# print("tup7:",tup7)  #报错,未找到

print("-----元组运算符-----")
print("len('one','two','three','four','five'):",len(('one','two','three','four','five')))
print("(1,2,3)+(4,5,6):",(1,2,3)+(4,5,6))
print("('Hi!',)*4:",('Hi!',)*4)
print("3 in (1, 2, 3):",3 in (1, 2, 3))
for x in (1,2,3) :
    print(x)

print("-----元组索引与截取-----")
print("tup5[1]:",tup5[1])
print("tup[-1]:",tup5[-1])
print("tup5[1:]:",tup5[1:])

print("-----元组内置函数-----")
"""
len(tuple)      计算元组元素个数
max(tuple)      返回元组中元素最大值
min(tuple)      返回元组中元素最小值
tuple(seq)      将列表转换为元组
"""