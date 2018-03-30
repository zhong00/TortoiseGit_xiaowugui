__author__ = 'zhonglingling'

def sum1(a,b):
    return a+b

def sum2(a,b):
    return sum3(a,b)

def sum3(a,b):
    return a+b
print(sum1(3,5))
print(sum2(3,4))