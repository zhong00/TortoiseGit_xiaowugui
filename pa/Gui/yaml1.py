#-*-coding:utf-8-*-
__author__ = 'zhonglingling'

import yaml

f = open("yaml1.yaml",'r',encoding='utf-8')

x = yaml.load(f)
print(type(x))
f.close()
print(x)
# print(x['info'])
# print(type(x['info']))
#print(x['info']['height'])
try :
    s = x['spouse1']['name']
except Exception as e:
    print(e)