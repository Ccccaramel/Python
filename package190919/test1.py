# 异常处理
# 一个except子句可以同时处理多个异常，这些异常将被放在括号里成为一个元组
import sys
try:
    num = int(input("please enter an integer："))
    result = 8 / num
    print(result)
except ValueError:
    print("Please enter the correct integer")
except ZeroDivisionError:
    print("Divide by 0 error")
    
# 最后一个except子句可以忽略异常的名称，它将被当作通配符使用
try:
    f=open('runoob.txt')
    s=f.readline()
    i=int(s.strip())
except OSError as err:
    print("OS error:{0}",format(err))
except ValueError:
    print("Could not convent data to an integer.")
except:
    print("Unexpected error:",sys.exc_info()[0])
    raise