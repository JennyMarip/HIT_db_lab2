from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap
from window.SchoolWindow import SchoolWindow
from window.LibraryWindow import LibraryWindow
from window.StuLogWindow import StuLogWindow
from window.ManageWindow import ManageWindow


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('./ui/MainWindow.ui')
        # 主页面的按钮
        self.sch_btn = self.ui.pushButton_2
        self.lib_btn = self.ui.pushButton
        self.ma_btn = self.ui.pushButton_3
        self.stu_btn = self.ui.pushButton_4
        # 主页面的图片
        self.label = self.ui.label
        # 主页面下的一级页面
        self.sch_win = SchoolWindow()
        self.lib_win = LibraryWindow()
        self.SL_win = StuLogWindow()
        self.Ma_win = ManageWindow()
        self.init_ui()

    def init_ui(self):
        # 设置首页图片的特征
        pix = QPixmap('./picture/HIT_picture(1).jpg')
        self.label.setPixmap(pix)
        self.label.setGeometry(220, 50, 150, 200)
        self.label.setStyleSheet('border: 2px solid red')
        self.label.setScaledContents(True)
        # 设置页面跳转事件
        self.sch_btn.clicked.connect(self.jump_sch)
        self.lib_btn.clicked.connect(self.jump_lib)
        self.stu_btn.clicked.connect(self.jump_sl)
        self.ma_btn.clicked.connect(self.jump_ma)
        # 设置返回按钮的事件
        self.sch_win.ui.pushButton_3.clicked.connect(self.sch_back)
        self.lib_win.ui.pushButton_4.clicked.connect(self.lib_back)
        self.Ma_win.ui.pushButton_4.clicked.connect(self.ma_back)
        self.SL_win.ui.pushButton_3.clicked.connect(self.sl_back)

    # 跳转函数
    def jump_sch(self):
        self.ui.hide()
        self.sch_win.ui.show()

    def jump_lib(self):
        self.ui.hide()
        self.lib_win.ui.show()

    def jump_sl(self):
        self.ui.hide()
        self.SL_win.ui.show()

    def jump_ma(self):
        self.ui.hide()
        self.Ma_win.ui.show()

    # 返回函数
    def sch_back(self):
        self.sch_win.ui.hide()
        self.ui.show()

    def lib_back(self):
        self.lib_win.ui.hide()
        self.ui.show()

    def ma_back(self):
        self.Ma_win.ui.hide()
        self.ui.show()

    def sl_back(self):
        self.SL_win.ui.hide()
        self.ui.show()
