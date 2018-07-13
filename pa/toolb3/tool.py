#-*-coding:utf-8-*-
__author__ = 'zhonglingling'
import  sys,yaml
from toolb3.log import *
from PyQt5.QtWidgets import QWidget,QApplication,QDesktopWidget,QLabel,QLineEdit,QPushButton,QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from mysql import connector

#工具界面
class tool(QWidget):
    def __init__(self):
        super().__init__()
        self.num_edit = None
        self.str_edit = None
        self.initUI()
        self.fresh()

    def initUI(self):
        title = QLabel("配置")
        title2 = QLabel("配置")
        num = QLabel("设置数字")
        str = QLabel("设置字符串")

        self.num_edit = QLineEdit()
        self.str_edit = QLineEdit()
        save_btn = QPushButton("保存",self)
        fresh_btn = QPushButton("刷新",self)

        grid = QGridLayout()
        grid.setSpacing(1)

        # grid.addWidget(title,0,0,1,3)
        # grid.addWidget(title2,4,0,1,3)
        grid.addWidget(num,1,0)
        grid.addWidget(self.num_edit,1,1,1,2)
        grid.addWidget(str,2,0)
        grid.addWidget(self.str_edit,2,1,1,2)
        grid.addWidget(save_btn,3,1)
        grid.addWidget(fresh_btn,3,2)

        self.setLayout(grid)
        #事件
        save_btn.clicked.connect(self.save)
        fresh_btn.clicked.connect(self.fresh)

        self.resize(400,200)#大小位置
        self.setWindowTitle('配置工具')#标题
        self.setWindowIcon(QIcon("C:/Users/zhonglingling/Desktop/123.png"))#图标
        self.show()

    #窗口居中
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    @pyqtSlot()
    def save(self):
        conn_db = SQLCON()
        #print(self.num_edit.text())
        conn_db.update((self.num_edit.text(),self.str_edit.text()))

    @pyqtSlot()
    def fresh(self):
        conn_db = SQLCON()
        list = conn_db.get()
        self.num_edit.setText(str(list[1]))
        self.str_edit.setText(str(list[2]))
        #print(self.num_edit.text())

#数据库处理
class SQLCON():
    def __init__(self):
        self.db = getVal().val
        self.conn = None

    @property
    def connect(self):
        if self.conn == None and self.db:
            try:
                self.conn = connector.connect(**self.db)
                logger.info("db connect success")
                return self.conn
            except connector.Error as e:
                logger.error('db connect fail')

    def update(self,t):
        con = self.connect
        print("connect",con)
        cursor = con.cursor()
        sql = "update setting set num="+t[0]+",str='"+t[1]+"' where id = 1"
        try:
            cursor.execute(sql)
            con.commit()
        except connector.Error as e:
            print(e)
            logger.Error("update fail")
        finally:
            cursor.close()
            con.close()

    def get(self):
        con = self.connect
        print("connect",con)
        cursor = con.cursor()
        sql = 'select * from setting where id=1'
        try:
            cursor.execute(sql)
            list = cursor.fetchone()
            # print(list)
            return list
        except:
            logger.error("select setting fail")
        finally:
            cursor.close()
            con.close()

#配置文件处理
class getVal():
    def __init__(self):
        self.val_dict = {}

    @property
    def val(self):
        try:
            f = open('tool.yaml','r')
            y = yaml.load(f)
            db = y['db']
            self.val_dict['host'] = db['host']
            self.val_dict['port'] = db['port']
            self.val_dict['database'] = db['database']
            self.val_dict['user'] = db['user']
            self.val_dict['password'] = db['password']
            self.val_dict['charset'] = db['charset']
            return self.val_dict
        except:
            logger.error("get yaml fail")
            return False
        finally:
            f.close()

if __name__=="__main__":
    app = QApplication(sys.argv)
    t = tool()
    sys.exit(app.exec_())
