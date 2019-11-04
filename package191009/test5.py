# sys.path
"""
 sys.path 是 python 的搜索模块的路径集，是一个 list
可以在 python 环境下使用 sys.path.append(path) 添加相关路径
但在退出 python 环境后会被清除
想要永久有效的话就修改 computer 的环境变量吧
"""
import sys
print(sys.path)