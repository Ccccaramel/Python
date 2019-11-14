# sorted()
"""
sort 是应用在 list 上的方法
list 的 sort 方法返回的是对已经存在的列表进行操作

sorted 可以对所有可迭代的对象进行排序操作
内建函数 sorted 方法返回的是一个新的list
而不是在原来的基础上进行操作

sorted(iterable, key = None, reverse = False)
iterable:可迭代对象
key:主要是用来进行比较的元素,只有一个参数,具体的函数的参数就是取自于可迭代对象中,指定可迭代对象中的一个元素来进行排序
reverse:排序规则, reverse=True 降序, reverse=False 升序(默认)
返回重新排序的列表
"""
list1 = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
print("sorted(list1):{}(默认升序)".format(sorted(list1)))
print("sorted(list1):{}(降序)".format(sorted(list1,reverse=True)))

list2 = [{"age": 17, "name": "Lili"}, {"age": 11, "name": "Jick"}, {"age": 19, "name": "Tom"}, {"age": 11, "name": "Bock"}, {"age": 15, "name": "Hansen"}]
print("sorted(list2):{}(默认升序<age>)".format(sorted(list2,key=lambda x: x["age"])))
print("sorted(list2):{}(降序<age>)".format(sorted(list2,key=lambda x: x["age"], reverse=True)))
print("sorted(list2):{}(默认升序<name>)".format(sorted(list2,key=lambda x: x["name"])))
print("sorted(list2):{}(默认升序<age,name>)".format(sorted(list2,key=lambda x: (-x["age"], x["name"]))))  # -x["age"] 意味着降序, "age" 对应的值均为 int ,仅值均为 int 才可加 - 号
