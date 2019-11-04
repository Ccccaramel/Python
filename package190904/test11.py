# 集合(去重功能+集合间的运算+添加元素(add与update)+移除元素+清空集合+判断元素是否在集合中存在+集合内置方法)
"""
集合是一个无序的不重复元素序列
创建格式:
  parme={value1,value2,...}
  set(value)
"""
set0=set()  #空集合
print("-----去重功能-----")
set1={'apple','banana','pear','apple','orange','banana'}
print("set1:",set1)

print("-----集合间的运算-----")
set2=set('123456')
set3=set('24680')
print("set2:",set2)
print("set3:",set3)
print("set2-set3:",set2-set3)
print("set3-set2:",set3-set2)
print("set2|set3:",set2|set3)
print("set2&set3:",set2&set3)
print("set2^set3:",set2^set3)

print("-----添加元素(add与update)-----")
set2.add('7')# 如果元素已存在则不进行任何操作
print("set2:",set2)
# update可有多个值,参数可以是列表,元组,字典等等
set3=set(('red','green','blue','orange'))
set3.update({'yellow','black'})
print("set3:",set3)
set3.update(['gray','pink'],['purple','white'])
print("set3:",set3)

print("-----移除元素-----")
set3.remove("blue")
print("set3.remove(\"blue\"):",set3)  #若不存在会报错
print("set3.pop:",set3.pop())  #随机删除,pop是删除集合的第一个元素(排序后的集合的第一个元素)
print("set3:",set3)
 
print("-----清空集合-----")
set4=set('123')
print("请空前的set4:",set4)
set4.clear()
print("清空后的set4:",set4)

print("-----判断元素是否在集合中存在-----")
print("\"green\" in set4:",("green" in set3))  #多运行几次说不定就被随机删掉返回False

print("-----集合内置方法-----")
"""
add()                              为集合添加元素
clear()                            移除集合中的所有元素
copy()                             拷贝一个集合
difference()                       返回多个集合的差集
difference_update()                移除集合中的元素，该元素在指定的集合也存在
discard()                          删除集合中指定的元素
intersection()                     返回集合的交集
intersection_update()              返回集合的交集
isdisjoint()                       判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False
issubset()                         判断指定集合是否为该方法参数集合的子集
issuperset()                       判断该方法的参数集合是否为指定集合的子集
pop()                              随机移除元素
remove()                           移除指定元素
symmetric_difference()             返回两个集合中不重复的元素集合
symmetric_difference_update()      移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中
union()                            返回两个集合的并集
update()                           给集合添加元素
"""