#-*-coding:utf-8-*-
__author__ = 'zhonglingling'

import os,re,yaml
import Gui.createlog

def getYamlValue():
    f = open('rmlog.yaml','r')
    config = yaml.load(f)
    Gui.createlog.logger.info("load config")
    try:
        dirname = config['dirname']
        return dirname
    except Exception as e:
        return None

configVal = getYamlValue()
if not configVal:
    Gui.createlog.logger.info("here is no dirname in yaml")
else:
    #os.chdir('E:/TortoiseGit_xiaowugui/pa/autotest')
    list = os.getcwd().split('\\')
    dirName = list[len(list)-1]
    if re.search('netbus$',configVal):
        Gui.createlog.logger.info("this is svc_netbus")
        files = os.listdir(os.curdir)
        Gui.createlog.logger.info(files)
        for i in files:
            if re.search('\d$',i) and os.path.isfile(i):
                Gui.createlog.logger.info('remove file')
                os.remove(i)