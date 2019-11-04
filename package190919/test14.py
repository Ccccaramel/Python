# 类内的方法之间的调用
"""
需要先创建一个实例才可调用
"""
class student(object):
    def eat(self):
        self.buy()  #<1> 两种方式均可，建议 <1> 方式
        # student().buy()  #<2>
        print("eat foot")
    def buy(self):
        print("buy foot")
s=student()
s.eat()
# student.eat()