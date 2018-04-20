__author__ = 'zhonglingling'

def log(func):
    def wrap(*args):
        print("******************************")
        print("**********"+func.__name__+"**********")
        return func(*args)
    return wrap

def printInfo(name,content):
    print("~~~~~~~~~~")
    print("~~~~~~~~~~")
    print("~~~~~~~~~~")
    print(name,content)