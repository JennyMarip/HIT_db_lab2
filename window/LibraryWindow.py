import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap
from db_init import cursor, db


class LibraryWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('./ui/LibraryWindow.ui')
        self.label = self.ui.label
        # 按钮
        self.s_btn = self.ui.pushButton_2
        self.t_btn = self.ui.pushButton
        self.b_btn = self.ui.pushButton_3
        # 文本框
        self.browser = self.ui.textBrowser
        # 输入框
        self.sid_line = self.ui.lineEdit
        self.bid_line = self.ui.lineEdit_2
        self.init_ui()

    def init_ui(self):
        # 设置首页图片的特征
        pix = QPixmap('./picture/HIT_picture(3).jpg')
        self.label.setPixmap(pix)
        self.label.setStyleSheet('border: 2px solid red')
        self.label.setScaledContents(True)
        # 设置按钮对应的事件
        self.s_btn.clicked.connect(self.inquire_s)
        self.t_btn.clicked.connect(self.inquire_t)
        self.b_btn.clicked.connect(self.borrow)

    def inquire_s(self):
        sql = 'select B_id, B_name from s_book'
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchall()
        self.browser.setText('------------')
        for i in range(len(res)):
            self.browser.append(str(res[i][0]) + ':' + res[i][1] + '\n')

    def inquire_t(self):
        sql = 'select B_id, B_name from t_book'
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchall()
        self.browser.setText('------------')
        for i in range(len(res)):
            self.browser.append(str(res[i][0]) + ':' + res[i][1] + '\n')

    def borrow(self):
        sid = self.sid_line.text()
        bid = self.bid_line.text()
        # 判断是否全
        if sid == '' or not sid.isdigit():
            self.sid_line.setText('学号无效!')
            self.bid_line.clear()
            return
        self.sid_line.clear()
        if bid == '' or not bid.isdigit():
            self.bid_line.setText('书籍代码无效!')
            self.sid_line.clear()
            return
        self.bid_line.clear()
        # 判断学号是否存在
        sql = 'select * from student where S_id = %s' % sid
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchall()
        if len(res) == 0:
            self.sid_line.setText('输入的学号不存在!')
            self.bid_line.clear()
            return
        self.sid_line.clear()
        # 判断书籍代码是否存在
        sql = 'select * from book where B_id = %s' % bid
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchall()
        if len(res) == 0:
            self.bid_line.setText('输入的书籍代码不存在!')
            self.sid_line.clear()
            return
        self.bid_line.clear()
        # 增加借阅记录
        sql = 'insert into borrow (S_id, B_id) values (%s, %s)' % (sid, bid)
        cursor.execute(sql)
        db.commit()
        self.sid_line.setText('借阅成功!')
