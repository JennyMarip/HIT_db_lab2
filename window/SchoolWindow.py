import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap
from window.CsMeWindow import CsMeWindow
from window.teachers import TeacherWindow


class SchoolWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('./ui/SchoolWindow.ui')
        self.label = self.ui.label
        self.cm_win = CsMeWindow()
        self.tea_win = TeacherWindow()
        self.cm_btn = self.ui.pushButton
        self.tea_btn = self.ui.pushButton_2
        self.init_ui()

    def init_ui(self):
        # 设置首页图片的特征
        pix = QPixmap('./picture/HIT_picture(2).jpg')
        self.label.setPixmap(pix)
        self.label.setGeometry(0, 0, 200, 150)
        self.label.setStyleSheet('border: 2px solid red')
        self.label.setScaledContents(True)
        # 设置页面跳转事件
        self.cm_btn.clicked.connect(self.jump_cm)
        self.tea_btn.clicked.connect(self.jump_tea)
        # 设置返回事件
        self.cm_win.ui.pushButton_3.clicked.connect(self.cm_back)
        self.tea_win.ui.pushButton_3.clicked.connect(self.tea_back)

    # 跳转函数
    def jump_cm(self):
        self.ui.hide()
        self.cm_win.ui.show()

    def jump_tea(self):
        self.ui.hide()
        self.tea_win.ui.show()

    # 返回函数
    def cm_back(self):
        self.cm_win.ui.hide()
        self.ui.show()

    def tea_back(self):
        self.tea_win.ui.hide()
        self.ui.show()
