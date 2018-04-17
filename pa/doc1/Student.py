__author__ = 'zhonglingling'
class Student(object):
    def __init__(self,name):
        self.name = name

    def printName(self):
        print(self.name)

def printLog(fuc):
    print(fuc.__name__)

def add(num1,num2):
    print(num1+num2)

printLog(add)
add(3,5)

def log(fun):
    print(fun.__name__)
    #https://blog.csdn.net/callinglove/article/details/45483097