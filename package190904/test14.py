# 迭代器与生成器
print("*****iter()*****")
list1 = [1,2,3,4]
dict1 = {"1": 123, "qqq": "www", "123": "m"}
it = iter(list1)  # 创建迭代器对象
print(next(it))  # 输出迭代器的下一个元素
print(next(it))
print(next(it))
print(next(it))

# 通过for语句遍历
it = iter(list1)
for x in it:
    print(x, end=" ")
print()

for k in dict1:
    print("key:{},value:{}".format(k,dict1[k]))

# 通过next()函数
# import sys
# it=iter(list1)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()  此句会终止程序
print("*****将类作为一个迭代器*****")
"""
把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 和 __next__()
__iter__() 方法返回一个特殊的迭代器对象,这个迭代器对象实现了 __next()__ 方法并通过 Stoplteration 异常标识迭代的完成
__next__() 返回下一个迭代器对象
Stoplteration 异常用于标识迭代的完成,防止出现无限循环的情况,
    在 __next__()方法中我们可以设置在完成指定循环次数后触发Stoplteration异常来结束迭代
"""


class MyNumbers:
    def __iter__(self):
        self.a = 1
        print("self.a:",self.a)
        return self

    def __next__(self):
        if self.a <= 6:
            x = self.a
            print("a:", self.a, "x:", x)
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

print("*****生成器*****")
"""
在python中,使用了yield的函数被称为生成器
生成器是一个返回迭代器的函数,只能用于迭代操作,或者说生成器就i是一个迭代器
在调用生成器运行的过程中,每次遇到yield时函数会暂停并保存当前所有的运行信息,返回yield的值,
并在下一次执行next()方法时从当前位置继续运行
调用一个生成器函数,返回的是一个迭代器对象
"""
import sys


def fibonacci(n):
    a, b, counter=0, 1, 0
    while True:
        if counter > n:
            return
        yield a  # 在此处暂停并返回a值
        a, b = b, a+b
        counter += 1


f = fibonacci(10)  # f是一个迭代器,由生成器返回生成
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()

