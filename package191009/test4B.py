E = 2.71


def main():
    print("E:{}".format(E-2))


if __name__ == "__main__":
    main()
else:
    print("__main__ of test4B.py:", __name__)
"""
通过 if __name__=='__main__' 模拟程序入口
这是一种编码习惯而非规定
防止引用时不需要的部分代码被执行

__name__ 是一个内置变量，用于反映一个包的结构
直接运行本模块时，没有包结构，即模块名为 __main__
"""
print(__name__)
