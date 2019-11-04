# 列表(访问+更新+删除+列表脚本操作符+列表截取与拼接+嵌套列表+list常用内置函数)
list1 = ['baidu', 'wangyi', 'tengxun', 1996, 2019]
list2 = [1, 2, 3, 4, 5]

print("-----访问-----")
print("list1[0]:", list1[0])
print("list2[1:4]", list2[1:4])

print("-----添加-----")
print("添加前的list1[4]:", list1)
list1 += ["new"]
print("添加后的list1[4]:", list1)

print("-----更新-----")
print("更新前的list1[4]:", list1[4])
list1[4] = 2020
print("更新后的list1[4]:", list1[4])

print("-----删除-----")
print("删除元素前的list1:", list1)
del list1[4]
print("删除元素后的list1:", list1)

print("-----列表脚本操作符-----")
list3 = ['a', 'b', 'c'] + ['d', 'e', 'f']
print("list3:", list3)
print("['Hi!']*4:", ["Hi!"] * 4)
print("3 in [1,2,3]:", 3 in [1, 2, 3])
for x in [1, 2, 3]:
    print(x, end=" ")

print("-----列表截取与拼接-----")
print("list1[-2]:", list1[-2])
print("list1[1:]:", list1[1:])
list2 += list1
print("list2+=list1:", list2)

print("-----嵌套列表-----")
list4 = [list1, list3]
print("list4[0]:", list4[0])
print("list4[0][1]:", list4[0][1])

print("-----list常用内置函数-----")
"""
list.append(obj)                         在列表末尾添加新的对象
list.count(obj)                          统计某个元素在列表中出现的次数
list.extend(seq)                         在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list.index(obj)                          从列表中找出某个值第一个匹配项的索引位置
list.insert(index, obj)                  将对象插入列表
list.pop([index=-1])                     移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list.remove(obj)                         移除列表中某个值的第一个匹配项
list.reverse()                           反向列表中元素
list.sort( key=None, reverse=False)      对原列表进行排序
list.clear()                             清空列表
list.copy()                              复制列表
"""
list5 = [1, 2, 3, 4, 5]
list6 = [6, 7, 8, 9, 0]
list5 = list6
for x in list5:
    print("x:", x, ",type(x):", type(x))
