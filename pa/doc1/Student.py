#-*- encoding:utf-8 -*-
import time,os
import yaml
__author__ = 'zhonglingling'

filePath = os.path.dirname(__file__)

print(filePath)

print(os.path.split(os.path.realpath(__file__))[0])

print(os.path.join(os.path.split(os.path.realpath(__file__))[0],'config.yaml'))