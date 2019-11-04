# 关键字(end)
print("-----end-----")
# 关键字end可以用于将结果输出到同一行,或者在输出的末尾添加不同的字符
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b


# 异包调用通过继承的方式重写内置模块的方法
# import sys
# sys.path.append("package190904A")
# from stringR import string
# s1=string("yes")
# print("s1" ,s1.capitalize())
# print("s1" ,s1.isalpha())