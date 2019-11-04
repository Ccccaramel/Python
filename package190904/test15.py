# 函数(*+**+匿名函数)
print("*****(*)*****")

#不定参数
def printinfo1(arg1,*vartuple):
    print("*vartuple:")
    for var in vartuple:
        print(var)
    return
printinfo1(10)
printinfo1(50,60,70,80)

# *后的变量必须用 name=value 形式传入
def fun1(a,b,*,c,d):
    return a+b+c+d

print("fun1(1,2,3):",fun1(1,2,d=6,c=3))

print("*****(**)*****")
def printinfo2(arg1,**vardict):  #必须是一个常量
    print("输出:")
    print(arg1)
    print(vardict)
printinfo2(1,a=2,b=3)

print("*****匿名函数*****")
"""
lambda只是一个表达式,而不是代码块
"""
sum=lambda num1,num2:print(num1+num2)
sum(4,6)