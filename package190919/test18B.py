# from test18A import funA
import test18A
class funB():
    def goB():
        test18A.funA.printA(67)
        # funA.printA(67)
    def printB(num):
        print("this is funB's print,the num is: %d"%(num))
        funB.goB()