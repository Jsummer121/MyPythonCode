# -*- coding: utf-8 -*-

# 正常的操作（详情看简书的操作）
# 第一步：在根目录下创建ui文件，然后选择点击pyuic，他会自动生成py文件。
# 第二部：开始复制代码，然后重新创建一个新的py文件，导入sys，进行窗口的正常创建。如果不想要出现第一个黑屏幕的，就把.py的后缀名改成.pyw。
self.user_line.setPlaceholderText('Please enter your username')  # 添加提示字符
self.key_line.setPlaceholderText('Please enter your password')

#提示消息框
# from PyQt5.QtWidgets import QPushButton , QApplication , QWidget , QMessageBox
# import sys
#
# app = QApplication([])
# widget = QWidget()
#
# def showMsg():
#     QMessageBox.information(widget,"信息提示框","OK,弹出测试信息")
#
# btn = QPushButton("测试点击按钮", widget)
#
# btn.clicked.connect(showMsg)
#
# widget.show()
# sys.exit(app.exec_())


#实现两个窗口的链接
# class parentWindow(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)
#         self.main_ui = Ui_wuliaobank()
#         self.main_ui.setupUi(self)
#
# class childWindow(QDialog):
#     def __init__(self):
#         QDialog.__init__(self)
#         self.child = Ui_Zhuce()
#         self.child.setupUi(self)
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     # myWin = MyWindow()
#     window = parentWindow()
#     child = childWindow()
#
#     #通过toolBurron将两个窗口并联
#     btn = window.main_ui.sign_in
#     btn.clicked.connect(child.show)
#
#     window.show()
#     sys.exit(app.exec_())



#正常的最后一行
# class MyWindow(QMainWindow, Ui_wuliaobank):
#     def __init__(self,parent=None):
#         super(MyWindow,self).__init__(parent)
#         self.setupUi(self)
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     myWin = MyWindow()
#     myWin.show()
#     sys.exit(app.exec_())

#按钮进行编写
# self.zhuce_bt.setStyleSheet("QPushButton{color:rgb(166, 166, 166)}"
#                             "QPushButton{border:0px}"
#                             "QPushButton:hover{color:black}"
#                             )

#密码设置不可见
# self.key_line.setEchoMode(QLineEdit.Password)  # 密码设置为不可见