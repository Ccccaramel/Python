# 注释、保留字、多行语句

# 单行注释

'''
多行注释
'''

"""
多行注释
"""

"""
python3.7.4的关键字
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
'return', 'try', 'while', 'with', 'yield']
"""

print("*****多行语句*****")
str1="Ding"
str2="Tan"
str3="Hua"
total=str1+\
    str2+\
    str3
print(total)

# 文本文件的读写
# fo=open("runoob.txt","r+")
# print("文件名:",fo.name)

# str="6:www.runoob.com"

# fo.seek(0,2)
# line=fo.write(str)

# fo.seek(0,0)
# for index in range(6):
#     line = next(fo)
#     print("文件行号 %d - %s" % (index,line))
# fo.close()

