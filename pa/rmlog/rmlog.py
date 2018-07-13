#-*-coding:utf-8-*-
__author__ = 'zhonglingling'
import yaml,logging,os,re

def createlog():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    fh = logging.FileHandler('rmlog.log',mode='a')
    fh.setLevel(logging.INFO)

    formate = logging.Formatter('%(asctime)s-%(filename)s-[line%(lineno)d]-%(levelname)s:%(message)s')
    fh.setFormatter(formate)
    logger.addHandler(fh)
    return logger

class Yaml:
    def __init__(self):
        self.config = self.getYaml()
        if self.config:
            self.filepath = self.getYamlValue('filepath')
            self.filename = self.getYamlValue('filename')

    def getYaml(self):
        try:
            f = open('init.yaml','r')
            c = yaml.load(f)
            f.close()
            return c
        except:
            return None

    def getYamlValue(self,key):
        try:
            return self.config[key]
        except:
            return None

logger = createlog()
yaml1=Yaml()

if not (yaml1.config and yaml1.filename and yaml1.filepath):
    logger.info("there is something wrong in yaml")
else:
    os.chdir(yaml1.filepath)
    pathList = os.getcwd().split('\\')
    print(pathList[len(pathList)-1],yaml1.filename)
    if pathList[len(pathList)-1]!=yaml1.filename:
        logger.info("filepath is wrong")
    else:
        logger.info("filepath is correct")
        fileList = os.listdir(os.curdir)
        print(fileList)
        for i in fileList:
            if os.path.isfile(i) and re.search('\d$',i):
                os.remove(i)
                logger.info("remove file")