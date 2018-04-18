import time
__author__ = 'zhonglingling'
class Student(object):
    def __init__(self,name):
        self.name = name

    def printName(self):
        print(self.name)
def log(para):
    def logout(fun):
        def printlog(*args):
            if para=="func1":
                print("start"+fun.__name__)
                fun(*args)
                print("end"+fun.__name__)
            if para == "func2":
                print("func2,start"+fun.__name__)
        return printlog
    return logout

@log(para="func1")
def sum(a,b):
    print(a+b)

@log(para="func2")
def getNum(a):
    print("getnum"+a)

sum(34,1)
getNum("jjj")