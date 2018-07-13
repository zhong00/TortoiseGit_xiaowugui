#-*-coding:utf-8-*-
from PyQt5.QtWidgets import QPushButton, QApplication

__author__ = 'zhonglingling'
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

app=QApplication(sys.argv)
b=QPushButton("Hello Kitty!")
b.show()
b.clicked.connect(app.quit)  #事件
app.exec_()