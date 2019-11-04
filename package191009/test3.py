# 为已创建完成的对象添加新的属性和方法并调用
class animal:
    # age=0
    # weight=0
    def __init__(self,age,weight):
        self.age=age
        self.weight=weight
    def out(self):
        print("this animal weight is {} kg,and age is {} years.".format(self.weight,self.age))
    def newout(self):
        print("this animal weight is {} kg,hight is {} m,and age is {} years.".format(self.weight,self.hight,self.age))

a1=animal(6,180)
# a1.newout()  #报错

setattr(a1,"hight",2)
print("hight:%d"%a1.hight)
a1.newout()

# 通过·setattr() 既可以添加属性也可以添加方法
setattr(a1,"add",lambda a,b:a+b)
print("a1.add(3,5):%d"%a1.add(3,5))
add=getattr(a1,"add")
print("the two numbers add count is:%d"%add(3,7))

# 此方式看似简短，但一点儿也不花里胡哨
def say(s):
    print("ok,{}".format(s))
a1.s=say
a1.s("good")