# -*- encoding:utf-8 -*-
__author__ = 'Lilian'

import sys
from PyQt5.QtWidgets import QApplication,QGridLayout,QLineEdit,QWidget,QHBoxLayout,QVBoxLayout,QLabel,QToolTip,QTextEdit,QPushButton,QDesktopWidget,QMainWindow,QAction,QMessageBox,qApp
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import QCoreApplication

class Example(QWidget,QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    #消息
    def closeEvent(self, event):
        reply = QMessageBox.question(self,"消息框","确定退出吗？",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if reply ==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    #窗口居中
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):
        #设置中心区域
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        #绝对定位
        # lb11 = QLabel("You",textEdit)
        # lb11.move(15,10)
        #
        # lb12 = QLabel("are",textEdit)
        # lb12.move(35,44)
        #
        # lb13 =QLabel("best",textEdit)
        # lb13.move(55,70)

        #网格布局
        title = QLabel("标题")
        author = QLabel("作者")
        review = QLabel("评论")

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title,1,0)
        grid.addWidget(titleEdit,1,1)
        grid.addWidget(author,2,0)
        grid.addWidget(authorEdit,2,1)
        grid.addWidget(review,3,0)
        grid.addWidget(reviewEdit,3,1,5,1)

        self.setLayout(grid)

        #提示
        QToolTip.setFont(QFont("SansSerif",20))#提示字体
        self.setToolTip("窗口提示")

        okButton = QPushButton("OK")
        cancelButton = QPushButton("cancle")
        print("#1")
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        print("#2")
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        print("#3")
        self.setLayout(vbox)
        #按钮
        btn = QPushButton("Button",self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.setToolTip("按钮提示")
        btn.resize(btn.sizeHint())
        btn.move(50,100)

        #菜单栏
        exitAction = QAction(QIcon(u"C:/Users/Lilian/Desktop/123.png"),"&Exit",self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit application")
        exitAction.triggered.connect(qApp.quit)
        # menubar = self.menuBar()
        # fileMenu = menubar.addMenu("&File")
        # fileMenu.addAction(exitAction)

        # self.statusBar()
        #self.statusBar().showMessage("Ready")#？？不显示

        #工具栏
        # self.toolbar = self.addToolBar("Exit")
        # self.toolbar.addAction(exitAction)
        #
        # self.resize(250,150)#大小位置
        # self.setWindowTitle('窗口标题')#标题
        # self.setWindowIcon(QIcon("C:/Users/Lilian/Desktop/123.png"))#图标
        self.show()

if __name__=="__main__":
    app =QApplication(sys.argv)#每个PyQt5应用程序都需要创建一个application对象。sys.argv是从命令行传入的参数列表。Python脚本可以从shell中运行。这是一种控制脚本启动的方式。
    ex = Example()
    sys.exit(app.exec_())