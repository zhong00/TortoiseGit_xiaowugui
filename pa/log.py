import time
__author__ = 'zhonglingling'
def printLog(level):
    def log(func):
        def output(*args):
            if level==1:
                print("function "+func.__name__+" is starting.....")
                func(*args)
                print("function "+func.__name__+" end")
            if level==2:
                print("level2 function is running "+func.__name__)
                func(*args)
        return output
    return log
@printLog(level=1)
def sum(a,b):
    print(a+b)

sum(3,2)