from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget

from window.Sign import SignWindow
from window.StuPlat import StuPlatWindow
from db_init import cursor, db


class StuLogWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('./ui/StudentLogin.ui')
        self.label = self.ui.label
        # 按钮
        self.sign_btn = self.ui.pushButton
        self.log_btn = self.ui.pushButton_2
        # 子窗口
        self.sign_win = SignWindow()
        self.log_win = StuPlatWindow()
        # 输入栏
        self.id_line = self.ui.lineEdit_2
        self.pwd_line = self.ui.lineEdit
        self.init_ui()

    def init_ui(self):
        # 设置首页图片的特征
        pix = QPixmap('./picture/HIT_picture(4).jpg')
        self.label.setPixmap(pix)
        self.label.setStyleSheet('border: 2px solid red')
        self.label.setScaledContents(True)
        # 设置界面跳转事件
        self.sign_btn.clicked.connect(self.jump_sign)
        self.log_btn.clicked.connect(self.jump_log)

    def jump_sign(self):
        self.sign_win.ui.show()

    def jump_log(self):
        sid = self.id_line.text()
        pwd = self.pwd_line.text()
        # 判断学号是否有效
        if sid == '' or not sid.isdigit():
            self.pwd_line.clear()
            self.id_line.setText('输入的学号无效!')
            return
        self.id_line.clear()
        # 判断密码是否为空
        if pwd == '':
            self.id_line.clear()
            self.pwd_line.setText('密码为空!')
            return
        self.pwd_line.clear()
        # 判断学号是否存在
        sql = 'select * from student where S_id = %s' % sid
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchall()
        if len(res) == 0:
            self.pwd_line.clear()
            self.id_line.setText('输入的学号不存在!')
            return
        self.id_line.clear()
        # 判断密码是否正确
        sql = 'select * from student where S_id = %s and S_pwd = \'%s\'' % (sid, pwd)
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchall()
        if len(res) == 0:
            self.pwd_line.setText('输入的密码不正确!')
            return
        self.pwd_line.clear()
        self.log_win.sid = sid
        self.log_win.ui.show()
