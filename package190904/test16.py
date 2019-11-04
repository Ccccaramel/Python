# 数据结构(列表+遍历技巧)
print("*****列表(list)*****")
list1=r"""
-----将列表当作堆栈使用-----
列表方法使得列表可以很方便的作为一个堆栈来使用,堆栈作为特定的数据结构,最先进入的元素最后一个被释放(后进先出)
用append()方法可以把一个元素添加到堆栈顶,用不指定索引pop()方法可以把一个元素从堆栈顶释放出来
"""
print(list1)
list2=r"""
-----将列表当作队列使用-----
也可以把列表当作队列使用,只是在队列里第一加入的元素,第一个取出来,但是拿列表做这样的目的效率不高
在列表的最后添加或者弹出元素速度快,然而列表里插入或者从头部弹出速度却不快(因为所有其它的元素都得一个一个地移动)
"""
print(list2)
list3=r"""
-----列表推导式-----
列表推导式提供了从序列创建列表的简单途径,通常应用程序将一些操作应用于某个序列的每个元素
用其获得的结果作为生成新列表的元素,或者根据确定的判断条件创建子序列
每个列表推导式都在for之后跟一个表达式,然后有零到多个for或if子句
返回结果是一个根据表达从其后的for和if上下文环境中生成出来的列表
如果希望表达式推导出一个元组,就必须使用括号
"""
print(list3)
list4=[2,4,6]
print("list4:",list4)
print("将列表中每个数值乘3:",[ 3*x for x in list4 ])
print("将每个元素替换成子列表,并在子列表中添加一个新元素(该元素的平方):",[[x,x**2] for x in list4])
print("用if子句作为过滤器:",[ x*3 for x in list4 if x>3])
list5=['   aaa','bbb   ','cc    c','   ddd   ']
print("list5:",list5)
print("对每个元素调用方法:",[ x.strip() for x in list5 ])
list6=[1,3,5]
print(list6)
print("二重循环:",[x*y for x in list4 for y in list6])
print("更复杂点的表达式:",[str(round(355/113,x)) for x in range(1,6)])
list7=[
    [1,2,3,4],
    [5,6, ,8],
    [9,10,11,12],
]
print("list7:",list7)
print("矩阵旋转(方法1):",[[arr[i] for arr in list7 ] for i in range(4) ])
tran1=[]
for i in range(4):
    tran1.append([ arr[i] for arr in list7])
print("矩阵旋转(方法2):",tran1)
tran2=[]
for i in range(4):
    tran2_row=[]
    for arr in list7:
        tran2_row.append(arr[i])
    tran2.append(tran2_row)
print("矩阵旋转(方法3):",tran2)

print("*****遍历技巧*****")

# 遍历字典
dict1={'add1':'BeiJing','add2':'Shanghai','add3':'shenzhen','add4':'wuhan'}
for k,v in dict1.items():
    print(k,v)

# 遍历列表带索引位置
for i,v in enumerate(list6):
    print(i,v)

# 同时遍历多个序列
list8=['Name','Age','Tel']
list9=['Jim','12','112']
for str1,str2 in zip(list8,list9):
    print(str1+":"+str2)

# 反向遍历
for i in reversed(range(1,10,2)):
    print(i)

