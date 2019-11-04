# 多个变量赋值、标准数据类型以及判断(isinstance与type)、True与False
print("*****多个变量赋值*****")
num1=num2=num3=6
print(num1,num2,num3)

print("*****标准数据类型以及判断(isinstance与type)*****")
'''
python3中有6个标准的数据类型:
  Number(数字)          不可变数据
  String(字符串)        不可变数据
  List(列表)            可变数据
  Tuple(元组)           不可变数据
  Set(集合)             可变数据
  Dictionary(字典)      可变数据
'''
num4,float1,bool1,complex1=1,6.4,True,4+3j
print(type(num4),type(float1),type(bool1),type(complex1))
print("-----isinstance与type-----")
'''
isinstance 和 type 的区别在于：
  type()不会认为子类是一种父类类型。
  isinstance()会认为子类是一种父类类型。
'''
class A:
    pass
class B(A):
    pass
print("isinstance(A(),A):",isinstance(A(),A))
print("type(A())==A:",type(A())==A)
print("isinstance(B(),A):",isinstance(B(),A))
print("type(B())==A:",type(B())==A)

print("*****True与False*****")
'''
python2中没有布尔型的，它用数字0表示False，用1表示True
python3中把True和False定义成了关键字，但值依旧是1和0，可以相加
'''
print("True+False:",True+False)