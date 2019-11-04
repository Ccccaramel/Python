# 字典(访问字典里的值+键值对添加+修改字典+删除字典元素或清空字典+键的特性+字典内置函数与方法)
"""
字典是一种可变容器模型,可存储任意类型对象
字典的每一个键值对用冒号分割,每个对之间用逗号分割
键必须唯一且不可变
"""
dict0={}  #空字典
dict0={0:10,1:11,2:12,3:13,"4":13}
for k in dict0 :
    print("key:",k,"type(k):",type(k),",v:",dict0[k])
print("-----访问字典里的值-----")
dict1={'Name':'Tom','Age':12,'Tel':120}
print("dict1['Age']:",dict1['Age'])

print("-----键值对添加-----")
dict1['Class']='First'

print("-----修改字典-----")
dict1['Age']=22

print("-----删除字典元素或清空字典-----")
del dict1['Class']
print(dict1)
dict1.clear()  #清空字典
print(dict1)
del dict1  #删除字典
# print(dict1)  #报错,未定义

print("-----键的特性-----")
dict2={'year':2019,'month':9,'day':18,'hour':11,'minute':3,'year':2020}
print("dict2:",dict2)
print("dict2['year']:",dict2['year'])
del dict2['year']
# print("dict2['year']:",dict2['year'])  #报错

print("-----字典内置函数与方法-----")
"""
len(dict)           计算字典元素个数，即键的总数
str(dict)           输出字典，以可打印的字符串表示
type(variable)      返回输入的变量类型，如果变量是字典就返回字典类型

radiansdict.clear()                            删除字典内所有元素
radiansdict.copy()                             返回一个字典的浅复制
radiansdict.fromkeys()                         创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
radiansdict.get(key, default=None)             返回指定键的值，如果值不在字典中返回default值
key in dict                                    如果键在字典dict里返回true，否则返回false
radiansdict.items()                            以列表返回可遍历的(键, 值) 元组数组
radiansdict.keys()                             返回一个迭代器，可以使用 list() 来转换为列表
radiansdict.setdefault(key, default=None)      和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
radiansdict.update(dict2)                      把字典dict2的键/值对更新到dict里
radiansdict.values()                           返回一个迭代器，可以使用 list() 来转换为列表
pop(key[,default])                             删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
popitem()                                      随机返回并删除字典中的最后一对键和值。
"""