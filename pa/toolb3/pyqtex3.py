#-*-coding:utf-8-*-
__author__ = 'zhonglingling'
from PyQt5.QtWidgets import QDialog, QSplitter, QListWidget, QApplication, QFrame, QStackedWidget, QPushButton, \
    QHBoxLayout, QVBoxLayout, QWidget, QLabel, QLineEdit, QComboBox, QTextEdit, QGridLayout, QLayout, QCheckBox
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,mysql.connector

# QTextCodec.setCodecForTr(QTextCodec.codecForName('utf8'))
class StockDialog(QDialog):
    def __init__(self,parent=None):
        super(StockDialog,self).__init__(parent)
        self.setWindowTitle(self.tr("综合布局实例"))
    #一级mainSplitter
        mainSplitter = QSplitter(Qt.Horizontal)
        mainSplitter.setOpaqueResize(True)
    #二级listWidget
        listWidget = QListWidget(mainSplitter)
        listWidget.insertItem(0,self.tr("个人基本资料"))
        listWidget.insertItem(1,self.tr("联系方式"))
        listWidget.insertItem(2,self.tr("详细信息"))
    #二级frame
        frame = QFrame(mainSplitter)
    #四级stack
        stack = QStackedWidget()
        stack.setFrameStyle(QFrame.Panel|QFrame.Raised)
        baseInfo = BaseInfo()
        contact = Contact()
        detail = Detail()
        stack.addWidget(baseInfo)
        stack.addWidget(contact)
        stack.addWidget(detail)
    #四级buttonLayout
        amendPushButton = QPushButton(self.tr("修改"))
        closePushButton = QPushButton(self.tr("关闭"))
        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch(1)
        buttonLayout.addWidget(amendPushButton)
        buttonLayout.addWidget(closePushButton)
    #三级mainLayout
        mainLayout = QVBoxLayout(frame)
        #mainLayout.setMargin(10)
        #mainLayout.setSpacing(6)
        mainLayout.addWidget(stack)
        mainLayout.addLayout(buttonLayout)
    #事件
        listWidget.currentRowChanged.connect(stack.setCurrentIndex)
        closePushButton.clicked.connect(self.close)
        amendPushButton.clicked.connect(self.output('a'))
        #amendPushButton.clicked.connect(self.write(baseInfo.userLineEdit.text(),baseInfo.nameLineEdit.text()))
    #零级layout
        layout=QHBoxLayout(self)
        layout.addWidget(mainSplitter)
        self.setLayout(layout)

    def write(self,a,b):
        c = MYSQLCON()
        c.save(a,b)

    def output(self,a):
        print(a)

class BaseInfo(QWidget):
    def __init__(self,parent=None):
        super(BaseInfo,self).__init__(parent)

        label1 = QLabel(self.tr("用户名："))
        label2 = QLabel(self.tr("姓名："))
        label3 = QLabel(self.tr("性别："))
        label4 = QLabel(self.tr("部门："))
        label5 = QLabel(self.tr("年龄："))
        otherLabel = QLabel(self.tr("备注："))
        otherLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.userLineEdit = QLineEdit()
        self.nameLineEdit = QLineEdit()
        sexComboBox = QComboBox()
        sexComboBox.insertItem(0,self.tr("男"))
        sexComboBox.insertItem(1,self.tr("女"))
        self.departmentTextEdit = QTextEdit()
        self.ageLineEdit = QLineEdit()

        labelCol = 0
        contentCol = 1
    #leftLayout
        leftLayout = QGridLayout()
        leftLayout.addWidget(label1,0,labelCol)
        leftLayout.addWidget(self.userLineEdit,0,contentCol)
        leftLayout.addWidget(label2,1,labelCol)
        leftLayout.addWidget(self.nameLineEdit,1,contentCol)
        leftLayout.addWidget(label3,2,labelCol)
        leftLayout.addWidget(sexComboBox,2,contentCol)
        leftLayout.addWidget(label4,3,labelCol)
        leftLayout.addWidget(self.departmentTextEdit,3,contentCol)
        leftLayout.addWidget(label5,4,labelCol)
        leftLayout.addWidget(self.ageLineEdit,4,contentCol)
        leftLayout.addWidget(otherLabel,5,labelCol,1,2)
        leftLayout.setColumnStretch(0,1)
        leftLayout.setColumnStretch(1,3)
    #hLayout
        label6 = QLabel(self.tr("头像："))
        iconLabel = QLabel()
        icon = QPixmap(r"C:\Users\zhonglingling\Desktop\123.png")
        iconLabel.setPixmap(icon)
        iconLabel.resize(icon.width(),icon.height())
        iconPushButton = QPushButton(self.tr("改变"))
        hLayout = QHBoxLayout()
        hLayout.setSpacing(20)
        hLayout.addWidget(label6)
        hLayout.addWidget(iconLabel)
        hLayout.addWidget(iconPushButton)
    #rightLayout
        label7 = QLabel(self.tr("个人说明："))
        descTextEdit = QTextEdit()
        rightLayout = QVBoxLayout()
        rightLayout.addLayout(hLayout)
        rightLayout.addWidget(label7)
        rightLayout.addWidget(descTextEdit)
    #mainLayout
        mainLayout = QGridLayout(self)
        mainLayout.addLayout(leftLayout,0,0)
        mainLayout.addLayout(rightLayout,0,1)
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

class Contact(QWidget):
    def __init__(self,parent=None):
        super(Contact,self).__init__(parent)
        label1 = QLabel(self.tr("电子邮件："))
        label2 = QLabel(self.tr("联系地址："))
        label3 = QLabel(self.tr("邮政编码："))
        label4 = QLabel(self.tr("移动电话："))
        label5 = QLabel(self.tr("办公电话："))

        mailLineEdit = QLineEdit()
        addressLineEdit = QLineEdit()
        codeLineEdit = QLineEdit()
        mpLineEdit = QLineEdit()
        phoneLineEdit = QLineEdit()
        receiveCheckBox = QCheckBox(self.tr("接收留言"))

        layout = QGridLayout(self)
        layout.addWidget(label1,0,0)
        layout.addWidget(mailLineEdit,0,1)
        layout.addWidget(label2,1,0)
        layout.addWidget(addressLineEdit,1,1)
        layout.addWidget(label3,2,0)
        layout.addWidget(codeLineEdit,2,1)
        layout.addWidget(label4,3,0)
        layout.addWidget(mpLineEdit,3,1)
        layout.addWidget(receiveCheckBox,3,2)
        layout.addWidget(label5,4,0)
        layout.addWidget(phoneLineEdit,4,1)
class Detail(QWidget):
    def __init__(self,parent=None):
        super(Detail,self).__init__(parent)
        label1 = QLabel(self.tr("国家/地区："))
        label2 = QLabel(self.tr("省份："))
        label3 = QLabel(self.tr("城市："))
        label4 = QLabel(self.tr("个人说明："))

        countryComboBox = QComboBox()
        countryComboBox.addItem(self.tr("中华人民共和国"))
        countryComboBox.addItem(self.tr("香港"))
        countryComboBox.addItem(self.tr("台湾"))
        countryComboBox.addItem(self.tr("澳门"))
        provinceComboBox = QComboBox()
        provinceComboBox.addItem(self.tr("安徽省"))
        provinceComboBox.addItem(self.tr("上海市"))
        provinceComboBox.addItem(self.tr("江苏省"))
        cityLineEdit = QLineEdit()
        remarkTextEdit = QTextEdit()

        layout = QGridLayout(self)
        layout.addWidget(label1,0,0)
        layout.addWidget(countryComboBox,0,1)
        layout.addWidget(label2,1,0)
        layout.addWidget(provinceComboBox,1,1)
        layout.addWidget(label3,2,0)
        layout.addWidget(cityLineEdit,2,1)
        layout.addWidget(label4,3,0)
        layout.addWidget(remarkTextEdit,3,1)

class MYSQLCON():
    def __init__(self):
        self.conn = None

    @property
    def connect(self):
        self.conn = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='rdb',
            user='root',
            password='',
            charset = 'utf8'
        )
        return self.conn

    def save(self,a,b):
        con = self.connect
        cursor = con.cursor()
        sql = "update users set username='"+a+"', name='"+b+"' where id=1"
        try:
            cursor.execute(sql)
            con.commit()
        except mysql.connector.Error as e:
            print(e)
        cursor.close()
        con.close()


app=QApplication(sys.argv)
main=StockDialog()
main.show()
app.exec_()