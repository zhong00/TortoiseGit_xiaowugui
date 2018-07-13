#-*-coding:utf-8-*-
__author__ = 'zhonglingling'


def log(level):
    def wrapper(func):
        def wrap(*args):
            if level==1:
                print("info----------"+func.__name__+"----------")
            elif level==2:
                print("notice----------"+func.__name__+"----------")
            elif level==3:
                print("important----------"+func.__name__+"----------")
            return func(*args)
        return wrap
    return wrapper
