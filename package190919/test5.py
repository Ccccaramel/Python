# 模块导入(同包同级*被动)
"""
调用同目录下其他模块
自动执行模块内的全部代码
"""
import os
#建议在根目录下执行，即选择第二种方式
# os.system("python test4.py")    #在当前目录下执行
os.system("python package190919/test4.py")  #在父父级目录下执行