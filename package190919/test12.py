# 模块(类)导入(异包同级*主动)
import sys
sys.path.append("package190904A")
from test10A_1 import add
num=add().reduce(4,5)
print(num)