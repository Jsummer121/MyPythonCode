import sys,linecache
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QWidget,QDialog
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Zhuce(object):
    def setupUi(self, Zhuce):
        Zhuce.setObjectName("Zhuce")
        Zhuce.resize(474, 292)
        self.signin = QtWidgets.QPushButton(Zhuce)
        self.signin.setGeometry(QtCore.QRect(170, 230, 111, 31))
        self.signin.setObjectName("signin")
        self.zhuce_name = QtWidgets.QLabel(Zhuce)
        self.zhuce_name.setGeometry(QtCore.QRect(160, 10, 151, 31))
        self.zhuce_name.setObjectName("zhuce_name")
        self.widget = QtWidgets.QWidget(Zhuce)
        self.widget.setGeometry(QtCore.QRect(110, 60, 251, 141))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.user_label = QtWidgets.QLabel(self.widget)
        self.user_label.setObjectName("user_label")
        self.gridLayout.addWidget(self.user_label, 0, 0, 1, 1)
        self.user_line = QtWidgets.QLineEdit(self.widget)
        self.user_line.setClearButtonEnabled(True)
        self.user_line.setObjectName("user_line")
        self.gridLayout.addWidget(self.user_line, 0, 1, 1, 1)
        self.key1_label = QtWidgets.QLabel(self.widget)
        self.key1_label.setObjectName("key1_label")
        self.gridLayout.addWidget(self.key1_label, 1, 0, 1, 1)
        self.key1_line = QtWidgets.QLineEdit(self.widget)
        self.key1_line.setClearButtonEnabled(True)
        self.key1_line.setObjectName("key1_line")
        self.gridLayout.addWidget(self.key1_line, 1, 1, 1, 1)
        self.key2_lebel = QtWidgets.QLabel(self.widget)
        self.key2_lebel.setObjectName("key2_lebel")
        self.gridLayout.addWidget(self.key2_lebel, 2, 0, 1, 1)
        self.key2_line = QtWidgets.QLineEdit(self.widget)
        self.key2_line.setClearButtonEnabled(True)
        self.key2_line.setObjectName("key2_line")
        self.gridLayout.addWidget(self.key2_line, 2, 1, 1, 1)
        self.tishikuang = QtWidgets.QLabel(Zhuce)
        self.tishikuang.setGeometry(QtCore.QRect(130, 210, 191, 20))
        self.tishikuang.setText("")
        self.tishikuang.setObjectName("tishikuang")
        self.retranslateUi(Zhuce)
        self.signin.clicked.connect(self.check_userkey)
        QtCore.QMetaObject.connectSlotsByName(Zhuce)

    def retranslateUi(self, Zhuce):
        _translate = QtCore.QCoreApplication.translate
        Zhuce.setWindowTitle(_translate("Zhuce", "欢迎注册"))
        self.signin.setText(_translate("Zhuce", "注册"))
        self.zhuce_name.setText(_translate("Zhuce", "         欢迎注册"))
        self.user_label.setText(_translate("Zhuce", "用户名"))
        self.key1_label.setText(_translate("Zhuce", "输入密码"))
        self.key2_lebel.setText(_translate("Zhuce", "再次输入密码"))

    def check_userkey(self): #检查注册状态
        if self.key1_line.text() != self.key2_line.text():
            self.tishikuang.setText("      两次密码输入不一致")
            X12 = False
        elif self.key1_line.text() == self.key2_line.text():
            self.tishikuang.setText("           注册成功")
            X12 = True
        len1 = len(open("id.txt", "r").readlines())
        for e in range(1,len1+1,2): #判断用户名是否在文件中
            if self.user_line.text() == linecache.getline("id.txt", e).strip():
                self.tishikuang.setText("您输入的用户名已存在，请重新输入")
                X12 = False
        if X12:
            with open("id.txt", "a", encoding="UTF-8") as id:
                id.write(self.user_line.text() + "\n")
                id.write(self.key1_line.text() + "\n")
        self.user_line.clear()
        self.key1_line.clear()
        self.key2_line.clear()


class Ui_wuliaobank(object):
    def setupUi(self, wuliaobank):
        wuliaobank.setObjectName("wuliaobank")
        wuliaobank.resize(500, 350)
        wuliaobank.setMinimumSize(QtCore.QSize(500, 350))
        wuliaobank.setMaximumSize(QtCore.QSize(500, 350))
        wuliaobank.setIconSize(QtCore.QSize(30, 30))
        self.body = QtWidgets.QWidget(wuliaobank)  #创建控制窗口
        self.body.setObjectName("body")    #名称
        self.log_in = QtWidgets.QPushButton(self.body)  #在控制窗口（body）创建登录按钮
        self.log_in.setGeometry(QtCore.QRect(270, 230, 91, 31)) #xy长宽
        self.log_in.setObjectName("log_in")  #名称
        self.sign_in = QtWidgets.QPushButton(self.body) #在控制窗口（body）创建注册按钮
        self.sign_in.setGeometry(QtCore.QRect(140, 230, 81, 31)) #xy长宽
        self.sign_in.setObjectName("sign_in")  #名称
        self.user_label = QtWidgets.QLabel(self.body) #在控制窗口创建一个标签
        self.user_label.setGeometry(QtCore.QRect(80, 90, 61, 21)) #xy长宽
        self.user_label.setObjectName("user_label")  #名称
        self.key_labal = QtWidgets.QLabel(self.body)
        self.key_labal.setGeometry(QtCore.QRect(80, 150, 51, 21))
        self.key_labal.setObjectName("key_labal")
        self.key_remember = QtWidgets.QCheckBox(self.body)   #在控制窗口创建一个单选框按钮
        self.key_remember.setGeometry(QtCore.QRect(160, 200, 71, 16))   #xy长宽
        self.key_remember.setObjectName("key_remember") #名称
        self.auto_go = QtWidgets.QCheckBox(self.body)  #在控制窗口创建一个单选框按钮
        self.auto_go.setGeometry(QtCore.QRect(260, 200, 71, 16))  #xy长宽
        self.auto_go.setObjectName("auto_go") #名称
        self.user_line = QtWidgets.QLineEdit(self.body)  #在控制窗口创建一个输入文本框
        self.user_line.setEnabled(True)  #设置文本框是可以用的
        self.user_line.setGeometry(QtCore.QRect(140, 90, 211, 31)) #xy长宽
        self.user_line.setText("") #预先在文本框输入“”内的东西
        self.user_line.setPlaceholderText('Please enter your username')  # 添加提示字符（自己会消失）
        self.user_line.setClearButtonEnabled(True)
        self.user_line.setObjectName("user_line") #名称
        self.key_line = QtWidgets.QLineEdit(self.body)
        self.key_line.setGeometry(QtCore.QRect(140, 150, 211, 31))
        self.key_line.setMouseTracking(True)
        self.key_line.setAutoFillBackground(False)
        self.key_line.setText("")
        self.key_line.setPlaceholderText('Please enter your password') #添加提示字符（消失）
        self.key_line.setClearButtonEnabled(True)
        self.key_line.setObjectName("key_line")#名称
        self.tishikuang = QtWidgets.QLabel(self.body)
        self.tishikuang.setGeometry(QtCore.QRect(120, 270, 221, 20))
        self.tishikuang.setText("")
        self.tishikuang.setObjectName("tishikuang")
        wuliaobank.setCentralWidget(self.body) #创建菜单栏
        self.head = QtWidgets.QMenuBar(wuliaobank)
        self.head.setGeometry(QtCore.QRect(0, 0, 500, 23))
        self.head.setObjectName("head")
        self.vip = QtWidgets.QMenu(self.head)
        self.vip.setObjectName("vip")
        self.nocard = QtWidgets.QMenu(self.head)
        self.nocard.setObjectName("nocard")
        self.helppeople = QtWidgets.QMenu(self.head)
        self.helppeople.setObjectName("helppeople")
        self.menu = QtWidgets.QMenu(self.head)
        self.menu.setObjectName("menu")
        wuliaobank.setMenuBar(self.head)
        self.last = QtWidgets.QStatusBar(wuliaobank)
        self.last.setSizeGripEnabled(True)
        self.last.setObjectName("last")
        wuliaobank.setStatusBar(self.last)
        self.actionwuliaoyinhang = QtWidgets.QAction(wuliaobank)
        self.actionwuliaoyinhang.setObjectName("actionwuliaoyinhang")
        self.actionzhuce = QtWidgets.QAction(wuliaobank)
        self.actionzhuce.setObjectName("actionzhuce")
        self.join = QtWidgets.QAction(wuliaobank)
        self.join.setObjectName("join")
        self.zhuanzhang = QtWidgets.QAction(wuliaobank)
        self.zhuanzhang.setObjectName("zhuanzhang")
        self.lilv = QtWidgets.QAction(wuliaobank)
        self.lilv.setObjectName("lilv")
        self.more = QtWidgets.QAction(wuliaobank)
        self.more.setObjectName("more")
        self.nocard_find = QtWidgets.QAction(wuliaobank)
        self.nocard_find.setObjectName("nocard_find")
        self.fileOpenAction = QtWidgets.QAction(wuliaobank)
        self.fileOpenAction.setObjectName("fileOpenAction")
        self.fileNewAction = QtWidgets.QAction(wuliaobank)
        self.fileNewAction.setObjectName("fileNewAction")
        self.fileCloseAction = QtWidgets.QAction(wuliaobank)
        self.fileCloseAction.setObjectName("fileCloseAction")
        self.vip.addSeparator() #创建子菜单栏
        self.vip.addAction(self.join)
        self.vip.addSeparator()
        self.vip.addAction(self.more)
        self.vip.addSeparator()
        self.nocard.addSeparator()
        self.nocard.addAction(self.zhuanzhang)
        self.nocard.addSeparator()
        self.nocard.addAction(self.nocard_find)
        self.helppeople.addSeparator()
        self.helppeople.addAction(self.lilv)
        self.helppeople.addSeparator()
        self.menu.addAction(self.fileOpenAction)
        self.menu.addAction(self.fileNewAction)
        self.menu.addAction(self.fileCloseAction)
        self.head.addAction(self.vip.menuAction())
        self.head.addAction(self.nocard.menuAction())
        self.head.addAction(self.helppeople.menuAction())
        self.head.addAction(self.menu.menuAction())
        self.retranslateUi(wuliaobank)
        self.log_in.clicked.connect(self.check_denglu)#登录检查
        QtCore.QMetaObject.connectSlotsByName(wuliaobank)
        wuliaobank.setTabOrder(self.log_in, self.sign_in)
        wuliaobank.setTabOrder(self.sign_in, self.key_remember)
        wuliaobank.setTabOrder(self.key_remember, self.auto_go)

    def check_denglu(self): #查看登录状态
        len1 = len(open("id.txt", "r").readlines())
        for e in range(1, len1 + 1, 2):  # 判断用户名是否在文件中，并且查看密码是否相同
            if self.user_line.text() == linecache.getline("id.txt", e).strip():
                if self.key_line.text() == linecache.getline("id.txt", e + 1).strip():
                    self.tishikuang.setText("               登陆成功")
                else:
                    self.tishikuang.setText("您输入的用户名或者密码错误，请重试。")
        self.key_line.clear()
        self.user_line.clear()

    def retranslateUi(self, wuliaobank):
        _translate = QtCore.QCoreApplication.translate
        wuliaobank.setWindowTitle(_translate("wuliaobank", "无聊bank"))
        self.log_in.setText(_translate("wuliaobank", "登录"))
        self.sign_in.setText(_translate("wuliaobank", "注册"))
        self.user_label.setText(_translate("wuliaobank", "用户名："))
        self.key_labal.setText(_translate("wuliaobank", "密码："))
        self.key_remember.setText(_translate("wuliaobank", "记住密码"))
        self.auto_go.setText(_translate("wuliaobank", "自动登录"))
        self.vip.setTitle(_translate("wuliaobank", "会员服务"))
        self.nocard.setTitle(_translate("wuliaobank", "无卡服务"))
        self.helppeople.setTitle(_translate("wuliaobank", "便民服务"))
        self.menu.setTitle(_translate("wuliaobank", "文件"))
        self.actionwuliaoyinhang.setText(_translate("wuliaobank", "denglu"))
        self.actionzhuce.setText(_translate("wuliaobank", "zhuce"))
        self.join.setText(_translate("wuliaobank", "加入我们"))
        self.zhuanzhang.setText(_translate("wuliaobank", "无卡转账"))
        self.lilv.setText(_translate("wuliaobank", "利率查看"))
        self.more.setText(_translate("wuliaobank", "更多信息"))
        self.nocard_find.setText(_translate("wuliaobank", "无卡查询"))
        self.fileOpenAction.setText(_translate("wuliaobank", "打开"))
        self.fileNewAction.setText(_translate("wuliaobank", "新建"))
        self.fileCloseAction.setText(_translate("wuliaobank", "关闭"))


class parentWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_wuliaobank()
        self.main_ui.setupUi(self)

class childWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_Zhuce()
        self.child.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # myWin = MyWindow()
    window = parentWindow()
    child = childWindow()

    #通过sign_in将两个窗口并联
    btn = window.main_ui.sign_in #后面的sign_in 是主对象中需要按的东西，来实现两个窗口的连接
    btn.clicked.connect(child.show)

    window.show()
    sys.exit(app.exec_())