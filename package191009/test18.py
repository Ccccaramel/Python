// 直接赋值+浅拷贝+深度拷贝
/*
直接赋值:对象的引用
浅拷贝(copy):拷贝父对象,不会拷贝对象的内部的子对象
深拷贝(deepcopy): copy 模块的 deepcopy 方法,完全拷贝了父对象及其子对象,两者是完全独立的
 */
import copy

a = {1:[1,2,3]}
b = b.copy()
print(a, b)
a[1].append(4)
print(a, b)

c = copy.deepcopy(a)
print(a, c)
a[1].append(5)
print(a, c)
