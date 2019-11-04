# 循环语句(while+while..else+range()+range与遍历+range与创建列表+pass)
print("-----while-----")
i = 0
while i < 4:
    print(i)
    i += 1
print("-----while..else-----")
while i < 3:  # 遇到无限循环想要终止时可用Ctrl+c
    print(i)
else:
    print("i大于或等于4")
print("-----for-----")
languages = ["C", "C++", "Java", "PHP"]
for x in languages:
    if x == 'C++':
        break
    if x == 'Java':
        break
    print(x)
print("*****range()*****")
for i in range(5):
    print(i)
for i in range(2, 6):
    print(i)
for i in range(0, 10, 2):
    print(i)
for i in range(-10, -100, -30):
    print(i)
print("-----range与遍历-----")
for i in range(len(languages)):
    print(i, languages[i])
print("-----range与创建列表-----")
list1 = list(range(5))
print(list1)
print("*****pass*****")
# pass是空语句,占位语句,不做任何事情,为了保持程序结构的完整性


# import os
# import sys
# sys.path.append("package190904A")
# from fun import *

# class fun1():
#     def run(n1,n2):
#         print(fun.addNum(n1,n2))

# fun1.run(4,5)
