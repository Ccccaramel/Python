# 输入与输出(输出格式美化+旧式字符串格式化+读取键盘输入+读写文件+文件对象的方法+pickle模块+append)
"""
python的两种输出方式:表达式语句和print()函数
第三种方式是使用文件对象的write()方法,标准输出文件可以用sys.stdout引用
若想输出的形式更多样,可以使用str.format()函数来格式化输出值
若想将输出的值转成字符串,可以使用repr()或str()函数来实现
  str:函数返回一个用户易读的表达形式
  repr():产生一个解释器易读的表达形式
"""
print("-----输出格式美化-----")
print(repr((123, 'ert', 'yui')))
# print("(123,'ert','yui')")  #与上面输出的不一样
str1 = 'hello!'
print("str1:", str1)
print("str(str1):", str(str1))
print("repr(str1):", repr(str1))
# repr():即使rjust()的值为0,数值之间至少有一个空格,但format会拼接在一起
print("平方&立方表---repr:")
for x in range(1, 11):
    print(repr(x).rjust(3), repr(x * x).rjust(4), end=' ')
    print(repr(x * x * x).rjust(5))
print("平方&立方表---format:")
for x in range(1, 11):
    print('{0:3d}{1:4d}{2:5d}'.format(x, x * x, x * x * x))
"""
类似的方法如ljust()和center(),这些方法并不会写任何东西,它们仅仅返回新的字符串
另一种方法zfill()它会在数字的左边填充0,如下所示
"""
print("'14'.zfill(4):", '14'.zfill(4))
print("-----str.format()-----")
print('{}网址:"{}!"'.format('百度', 'www.baidu.com'))
print('{1} and {0}'.format('alibaba', 'wangyi'))
print('Name:{name},Age:{age},Tel:{tel}'.format(tel='12315934568', name='Tom', age='45'))  # 位置和关键字可以任意结合也没问题

"""
!a   使用ascii()
!s   使用str()
!r   使用repr()
用于在格式化某个值之前对其进行转化
"""
import math

print('常量PI的值近似为:{!r}'.format(math.pi))
print('常量PI的值近似为:{0:.4f}'.format(math.pi))
dict1 = {'Google': 1, 'Tianmao': 2, 'Yili': 3}
for name, number in dict1.items():
    print('{0:10}==>{1:10d}'.format(name, number))

# 如果有一个很长的格式化字符串但又不想将它们分开,最简单的方式就是传入一个字典,用 [] 访问键值
print(' Tianmao : {0[Tianmao]:d}; Yili : {0[Yili]:d}; Google : {0[Google]:d} '.format(dict1))
# 也可以通过在table变量前使用**来实现相同的功能
print(' Tianmao : {Tianmao:d}; Yili : {Yili:d}; Google : {Google:d} '.format(**dict1))

print("-----旧式字符串格式化-----")
"""
% 操作符也可以实现字符串格式化,它将左边的参数作为类似sprintf()式的格式化字符串,而将右边的代入,然后返回格式化后的字符串
多使用str.format()
"""
print('常量PI的值近似为:%5.3f' % math.pi)

print("-----读取键盘输入-----")
"""
python提供了input()内置函数从标准输入读入一行文本,默认的标准输入是键盘
"""
str2 = input("Please input:")
print("What you enter is:", str2)

print("-----读写文件-----")
"""
open()将返回一个file对象
open(filename,mode)
  filename:包含了你要访问的文件名称的字符串值
  mode:决定了打开文件的模式:只读,写入,追加等,所有可取值见下表,且为可选参数,默认模式只读(r)

r       以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式
rb      以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头
r+      打开一个文件用于读写。文件指针将会放在文件的开头
rb+     以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头
w       打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件
wb      以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件
w+      打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件
wb+     以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件
a       打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入
ab      以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入
a+      打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写
ab+     以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写
规律:
r   (无+情况下)只读,文件不存在时除了r都会创建
b   以二进制打开
+   读写
a   追加
w   会清空原有内容
"""

print("-----文件对象的方法-----")
"""
f=open("<文件>","<模式>")
f.read([size])     无size参数或为负数将读取所有内容,否则读取size数目的数据
f.readline()       从文件中读取单独的一行,换行符为'\n',如果返回一个空字符串,说明已经读到最后一行
f.readlines()      将返回该文件中包含的所有行,如果设置可选参数sizehint,则读取指定长度的字节,并且将这些字节按行分割
f.write(string)    将string写入到文件中,然后返回写入的字符数
f.tell()           返回文件对象当前所处的位置,它是从文件开头开始算起的字节数
f.seek()           改变文件当前所处的位置,0:开头,1:当前位置,2:文件结尾,默认为0
                      seek(x,0):从起始位置开始移动x个字符
                      seek(x,1):从当前位置开始移动x个字符
                      seek(-x,2):从末尾位置向前移动x个字符
f.close()
  当处理一个文件对象时,使用with关键字是非常好的方式,在结束后,他会帮助你正确的关闭文件,而且比try-finally语句简短
  >>>with open('foo.txt','r') as f :
        read_data=f.read()
  >>>f.closed
  True
  文件对象还有其它方法,如isatty()和trucate(),但通常比较少用
"""

print("-----pickle模块-----")
"""
(建议使用json操作实现表的序列化)
python的pickle模块实现了基本的数据列和反序列化
通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件夹中去,永久存储
通过pickle模块的反序列化操作,我们能够从文件中创建上一次程序保存的对象
基本接口:
  pickle,dump(obj,file,[,protocol])
序列化对象,将对象obj保存到文件file中去
参数protocol是序列化模式,默认是0(0:ASCII协议,表示以文本的形式进行序列化.1:老式二进制协议.2:新式二进制协议)
有了pickle这个对象,就能对file以读取的形式打开
  x=pickle.load(file)
反序列化对象,将文件中的数据解析为一个python对象
从file中读取一个字符串,并将它重构为原来的python对象
"""
print("序列化:")
import pickle

data1 = {'a': [1, 2.0, 3, 4 + 6j],
         'b': ('string', u'Unicode string'),
         'c': None}
selfref_list = [1, 2, 3]
# tem=[4,6,7]
# selfref_list.append(tem)
selfref_list.append(selfref_list)
print(selfref_list)  # 为什么是三个点?
output = open('data.pkl', 'wb')  # 以 .pkl 作为后缀的文件是python里面保存文件的一种格式,直接打开会显示一些序列化的东西

pickle.dump(data1, output)

pickle.dump(selfref_list, output, -1)

output.close()
print("反序列化:")
import pprint

# 使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

data3 = pickle.load(pkl_file)
pprint.pprint(data3)

pkl_file.close()
print("-----append-----")
"""
list不会因每次调用此函数而创建一个新变量,分配一个新地址
每当第一次传入参数以及未传入参数时分别创建一个变量以及分配一个地址
未传参数:不会清除list的元素
传参数:清除之前的元素,再执行方法体中的操作

是因为造成了自引用,无限循环
append()是浅拷贝,拷贝父对象
"""

def listPractice(list=[], a=1):
    a = a + 1
    print("list(in):", list, ",id:", id(list), ",a:", a)
    list.append('python')
    return list


print(listPractice())
print(listPractice([1, 2, 3]))
print(listPractice())
print(listPractice([1, 2, 3]))
print(listPractice())
print(listPractice([4, 5, 6]))
print(listPractice())
print(listPractice([4, 5, 6]))

list1 = ['a', 's', 'd']
# list2=['p','u','t']
# list1.append(list2)
list1.append(list1)
print(list1)
