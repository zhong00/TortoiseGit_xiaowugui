#-*-coding:utf-8-*-
__author__ = 'zhonglingling'
import yaml,os

class GetYamlValue:
    def __init__(self):
        self._value = None
        s = yaml.load(open(self.GetYamlPath))
        for i in s.items():
            print(i)

    @property
    def GetYamlPath(self):
        return os.path.join(os.path.split(os.path.realpath(__file__))[0],"config.yaml")



    @property
    def value(self):
        return self._value

if __name__ == "__main__":
    print(GetYamlValue().GetYamlPath)
