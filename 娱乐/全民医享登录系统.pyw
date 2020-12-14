import sys,linecache
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QDialog,QLabel,QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Ui_yixiang(object):
    def setupUi(self, yixiang):
        yixiang.setObjectName("yixiang")
        yixiang.resize(410, 300)
        yixiang.setMinimumSize(QtCore.QSize(430, 330))
        yixiang.setMaximumSize(QtCore.QSize(430, 330))
        yixiang.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.body = QtWidgets.QWidget(yixiang)
        self.body.setObjectName("body")
        self.denglu = QtWidgets.QPushButton(self.body)
        self.denglu.setGeometry(QtCore.QRect(100, 260, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.denglu.setFont(font)
        self.denglu.setAutoFillBackground(True)
        self.denglu.setStyleSheet("QPushButton{background-color:rgb(002, 184, 250)}"
                                  "QPushButton{color:rgb(225, 225, 225)}"
                                  "QPushButton{border:0px}"
                                  "QPushButton{border-radius:5px}"
                                  "QPushButton:hover{color:black}"
                                    )
        self.denglu.setObjectName("denglu")
        self.user_line = QtWidgets.QLineEdit(self.body)
        self.user_line.setGeometry(QtCore.QRect(130, 150, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.user_line.setFont(font)
        self.user_line.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.user_line.setTabletTracking(False)
        self.user_line.setAutoFillBackground(False)
        self.user_line.setText("")
        self.user_line.setClearButtonEnabled(True)
        self.user_line.setStyleSheet("QLineEdit{border:0px}"
                                     "QLineEdit{background-color:rgb( 240, 240, 240)}"
                                    )
        self.user_line.setPlaceholderText('请输入您的账号')
        self.user_line.setObjectName("user_line")
        # self.name = QtWidgets.QLabel(self.body)
        # self.name.setGeometry(QtCore.QRect(130, 20, 121, 81))
        # self.name.setSizeIncrement(QtCore.QSize(0, 0))
        # self.name.setLayoutDirection(QtCore.Qt.LeftToRight)
        # self.name.setLineWidth(3)
        # self.name.setTextFormat(QtCore.Qt.AutoText)
        # self.name.setScaledContents(False)
        # self.name.setObjectName("name")
        # self.name.setStyleSheet("QLabel{background-image:url(图片/图片/logo.PNG)}"#第一种加入图片方法
        #                         )
        # self.name.setPixmap(QPixmap("图片/logo.PNG"))#第二种加入图片方法
        self.line = QtWidgets.QFrame(self.body)
        self.line.setGeometry(QtCore.QRect(100, 170, 231, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.body)
        self.line_2.setGeometry(QtCore.QRect(100, 210, 231, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.key_line = QtWidgets.QLineEdit(self.body)
        self.key_line.setGeometry(QtCore.QRect(130, 188, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.key_line.setFont(font)
        self.key_line.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.key_line.setTabletTracking(False)
        self.key_line.setClearButtonEnabled(True)
        self.key_line.setObjectName("key_line")
        self.key_line.setStyleSheet("QLineEdit{border:0px}"
                                    "QLineEdit{background-color:rgb( 240, 240, 240)}"
                                    )
        self.key_line.setPlaceholderText('请输入密码')
        self.key_line.setEchoMode(QLineEdit.Password)#密码设置为不可见
        self.auto_login = QtWidgets.QCheckBox(self.body)
        self.auto_login.setGeometry(QtCore.QRect(100, 230, 71, 16))
        self.auto_login.setObjectName("auto_login")
        self.remember_key = QtWidgets.QCheckBox(self.body)
        self.remember_key.setGeometry(QtCore.QRect(180, 230, 71, 16))
        self.remember_key.setObjectName("remember_key")
        self.zhuce_bt = QtWidgets.QPushButton(self.body)
        self.zhuce_bt.setGeometry(QtCore.QRect(0, 300, 75, 23))
        self.zhuce_bt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.zhuce_bt.setStyleSheet("QPushButton{color:rgb(166, 166, 166)}"
                                  "QPushButton{border:0px}"
                                  "QPushButton:hover{color:black}"
                                  )
        self.zhuce_bt.setObjectName("zhuce_bt")
        self.find_key = QtWidgets.QPushButton(self.body)
        self.find_key.setGeometry(QtCore.QRect(270, 230, 71, 16))
        self.find_key.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.find_key.setStyleSheet("QPushButton{color:rgb(166, 166, 166)}"
                                    "QPushButton{border:0px}"
                                    "QPushButton:hover{color:black}"
                                    )
        self.find_key.setObjectName("find_key")
        yixiang.setCentralWidget(self.body)
        self.close_win = QtWidgets.QPushButton(self.body)
        self.close_win.setGeometry(QtCore.QRect(400, 0, 31, 31))
        self.close_win.setStyleSheet("QPushButton{color:rgb(000, 000, 000)}"
                                    "QPushButton{border:0px}"
                                    "QPushButton:hover{background-color:red}"
                                    )
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.close_win.setFont(font)
        self.close_win.setObjectName("close_win")
        self.min_win = QtWidgets.QPushButton(self.body)
        self.min_win.setGeometry(QtCore.QRect(370, 0, 31, 31))
        self.min_win.setStyleSheet("QPushButton{color:rgb(000, 000, 000)}"
                                     "QPushButton{border:0px}"
                                     "QPushButton:hover{background-color:rgb(220, 220, 220)}"
                                     )
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.min_win.setFont(font)
        self.min_win.setObjectName("min_win")
        self.tishikuang = QtWidgets.QLabel(self.body)
        self.tishikuang.setGeometry(QtCore.QRect(90, 300, 241, 16))
        self.tishikuang.setObjectName("tishikuang")
#以上为各种组件的搭建地
        self.retranslateUi(yixiang)
        self.initUI()  #第三种加入图片方法
        self.denglu.clicked.connect(self.check_denglu)
        self.close_win.clicked.connect(yixiang.close)
        self.min_win.clicked.connect(yixiang.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(yixiang)
#单击事件的存放地
#以下为各种函数的聚集地
    def initUI(self): #第三种加入图片方法
        pix = QPixmap('图片/logo.PNG')
        lb = QLabel(self)
        lb.setGeometry(150, 40, 121, 100)
        lb.setPixmap(pix)
        lb.setScaledContents(True)
        self.show()

    def check_denglu(self): #查看登录状态
        len1 = len(open("id.txt", "r").readlines())
        for e in range(1, len1 + 1, 2):  # 判断用户名是否在文件中，并且查看密码是否相同
            if self.user_line.text() == linecache.getline("id.txt", e).strip():
                if self.key_line.text() == linecache.getline("id.txt", e + 1).strip():
                    self.tishikuang.setText("                登陆成功")
                else:
                    self.tishikuang.setText("  您输入的用户名或者密码错误，请重试。")
        self.key_line.clear()
        self.user_line.clear()

    def retranslateUi(self, yixiang):
        _translate = QtCore.QCoreApplication.translate
        yixiang.setWindowTitle(_translate("yixiang", "全民医享"))
        self.denglu.setText(_translate("yixiang", "登录"))
        self.auto_login.setText(_translate("yixiang", "自动登录"))
        self.remember_key.setText(_translate("yixiang", "记住密码"))
        self.close_win.setText(_translate("yixiang", "×"))
        self.min_win.setText(_translate("yixiang", "-"))
        self.zhuce_bt.setText(_translate("yixiang", "注册账号"))
        self.find_key.setText(_translate("yixiang", "找回密码"))

    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None



class MyWindow(QMainWindow, Ui_yixiang):
    def __init__(self,parent=None):
        super(MyWindow,self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowOpacity(0.85) #调整透明度
        # self.setAttribute(Qt.WA_TranslucentBackground)# 设置背景透明


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())