import sys
import os

# 两个同名 class ，前者为隐式
class add(object):
    def __init__(self,num1,num2):
        print("no!!!!!!")
        self.num1=num1
        self.num2=num2
        self.count=num1-num2
    def printf(self):
        print("{} - {} = {}".format(self.num1,self.num2,self.count))

class add(object):
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        self.count=num1+num2
    def printf(self):
        print("{} + {} = {}".format(self.num1,self.num2,self.count))
    def say():
        print("12344567")
        
def print_hi():
    print('package: package190904A')
    print('py: test4A_1')
    print('(def)name: print_hi ')
    
str='This is package190904A\'s test4A_1!'