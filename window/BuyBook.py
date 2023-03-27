from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget

from db_init import cursor, db


class BuyBookWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('./ui/BuyBook.ui')
        self.label = self.ui.label
        # 输入栏
        self.name_line = self.ui.lineEdit_2
        self.id_line = self.ui.lineEdit_3
        self.sid_line = self.ui.lineEdit
        # 按钮
        self.btn = self.ui.pushButton
        self.init_ui()

    def init_ui(self):
        # 设置首页图片的特征
        pix = QPixmap('./picture/HIT_picture(11).jpg')
        self.label.setPixmap(pix)
        self.label.setStyleSheet('border: 2px solid red')
        self.label.setScaledContents(True)
        # 设置按钮对应事件
        self.btn.clicked.connect(self.buy)

    def buy(self):
        name = self.name_line.text()
        bid = self.id_line.text()
        sid = self.sid_line.text()
        if name == '':
            self.id_line.clear()
            self.sid_line.clear()
            self.name_line.setText('书籍名称不能为空!')
            return
        if bid == '' or not bid.isdigit():
            self.name_line.clear()
            self.sid_line.clear()
            self.id_line.setText('无效的书籍代码!')
            return
        if sid == '' or not sid.isdigit():
            self.id_line.clear()
            self.name_line.clear()
            self.sid_line.setText('无效的书架号!')
            return
        # 判断书籍代码是否重复
        sql = 'select * from book where B_id = %s' % bid
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchall()
        if not len(res) == 0:
            self.name_line.clear()
            self.sid_line.clear()
            self.id_line.setText('该书籍代码已经存在!')
            return
        self.id_line.clear()
        # 判断书架号是否存在
        sql = 'select * from bookshelf where BS_id = %s' % sid
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchall()
        if len(res) == 0:
            self.name_line.clear()
            self.id_line.clear()
            self.sid_line.setText('该书架号不存在!')
            return
        self.sid_line.clear()
        sql = 'insert into book (B_id, B_name, B_BS_id) values(%s, \'%s\', %s)' % (bid, name, sid)
        cursor.execute(sql)
        db.commit()
        self.name_line.setText('购买成功!')
