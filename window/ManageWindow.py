import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap
from window.SchChange import SchChangeWindow
from window.BuyBook import BuyBookWindow
from window.NewCourse import NewCourseWindow


class ManageWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('./ui/ManageWindow.ui')
        self.label = self.ui.label
        self.sch_change_btn = self.ui.pushButton_2
        self.buy_btn = self.ui.pushButton_3
        self.new_btn = self.ui.pushButton
        self.sch_change_win = SchChangeWindow()
        self.buy_win = BuyBookWindow()
        self.new_win = NewCourseWindow()
        self.init_ui()

    def init_ui(self):
        # 设置首页图片的特征
        pix = QPixmap('./picture/HIT_picture(5).jpg')
        self.label.setPixmap(pix)
        self.label.setStyleSheet('border: 2px solid red')
        self.label.setScaledContents(True)
        # 设置跳转事件
        self.sch_change_btn.clicked.connect(self.jump_sch_change)
        self.buy_btn.clicked.connect(self.jump_buy)
        self.new_btn.clicked.connect(self.jump_new)

    def jump_sch_change(self):
        self.sch_change_win.ui.show()

    def jump_buy(self):
        self.buy_win.ui.show()

    def jump_new(self):
        self.new_win.ui.show()
