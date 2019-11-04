# 伪(继承方式)重写内置方法
class Mystring(str):
    def swapcase(self):  #原有str的内置方法被重写
        return "ok"

str1=(Mystring)("qwe")
print(str1.swapcase())
print(str1.isalnum())  #未被重写的原有str的内置方法不受影响