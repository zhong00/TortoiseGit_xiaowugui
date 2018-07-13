#-*-coding:utf-8-*-
__author__ = 'zhonglingling'
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

fh = logging.FileHandler('tool.log','a')
sh = logging.StreamHandler()

fh.setLevel(logging.INFO)
sh.setLevel(logging.INFO)

format = logging.Formatter("%(asctime)s-%(filename)s-line%(lineno)s[%(levelname)s]:%(message)s")
fh.setFormatter(format)
sh.setFormatter(format)

logger.addHandler(fh)
logger.addHandler(sh)

