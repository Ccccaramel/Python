# abs()
# 返回数字的绝对值
print("abs(-1):{}".format(abs(-1)))

# all()
"""
用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE
如果是返回 True ,否则返回 False
元素除了是 0、空、None、False 外都算 True
"""
list1 = ['a', 'b', 'c', 'd']
list2 = ['a', 'b', 0, 'd']
print("all(list1):{}".format(all(list1)))
print("all(list2):{}".format(all(list2)))

# any()
"""
用于判断给定的可迭代参数 iterable 是否全部为 False ,则返回 False
如果有一个为 True ,则返回 True
元素除了是 0、空、FALSE 外都算 TRUE
"""
list3 = [0, '', False]
list4 = [0, '', False, 'd']
print("any(list3):{}".format(any(list3)))
print("any(list4):{}".format(any(list4)))

# basestring()
"""
basestring() 方法是 str 和 unicode 的超类（父类） ,也是抽象类
因此不能被调用和实例化
但可以被用来判断一个对象是否为 str 或者 unicode 的实例
isinstance(obj, basestring) 等价于 isinstance(obj, (str, unicode)) ---> 仅限于python2!!!
注:python2 中的 unicode() 在python3中被归纳进 str 中
"""
print("isinstance(\"Hello world\", str):{}".format(isinstance("Hello world", str)))

# bin()
# 返回一个整数 int 或者长整数 long int 的二进制表示
print("bin(10):{}".format(bin(10)))

# bool()
"""
用于将给定参数转换为布尔类型,如果没有参数,返回 False
bool 是 int 的子类
"""
print("bool():{}".format(bool()))
print("bool(0):{}".format(bool(0)))
print("bool(1):{}".format(bool(1)))

# bytearray()
"""
返回一个新字节数组.注意!是字节!,ngklghl
这个数组里的元素是可变的
并且每个元素的值范围: 0 <= x < 256

clas bytearray([source[, encoding[, errors]]])
source:
    整数:返回一个长度为 source 的初始化数组
    字符串:按照指定的 encoding 将字符串转换为字节序列
    可迭代类型:元素必须为【0, 255】中的整数
    与 buffer 接口一致的对象:则此对象也可以被用于初始化 bytearray
    无任何参数:默认就是初始化数组为0个元素
"""
list5 = [1, 2, 3]
print("bytearray():{}".format(bytearray()))
print("bytearray(list5):{}".format(bytearray(list5)))
"""
\xnn 是什么?指的是基本 ASCII 码值,匹配 ASCII 中十六进制代码为 nn 的字符
[x00-x7f] 匹配 ASCII 值从0-127 的字符
0-127 表示单字节字符.也就是数字、英文字符、半角符号,以及某些控制字符
"""
print("bytearray('python', 'utf-8'):{}".format(bytearray('python', 'utf-8')))
