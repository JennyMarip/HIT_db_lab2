import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap
from window.CS import CSWindow
from window.ME import MEWindow


class CsMeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('./ui/CsMeWindow.ui')
        self.label = self.ui.label
        self.cs_btn = self.ui.pushButton
        self.me_btn = self.ui.pushButton_2
        self.me_win = MEWindow()
        self.cs_win = CSWindow()
        self.init_ui()

    def init_ui(self):
        # 设置首页图片的特征
        pix = QPixmap('./picture/HIT_picture(6).jpg')
        self.label.setPixmap(pix)
        self.label.setStyleSheet('border: 2px solid red')
        self.label.setScaledContents(True)
        # 设置跳转事件
        self.cs_btn.clicked.connect(self.jump_cs)
        self.me_btn.clicked.connect(self.jump_me)

    def jump_cs(self):
        self.cs_win.ui.show()

    def jump_me(self):
        self.me_win.ui.show()
