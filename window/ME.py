from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget

from db_init import cursor, db


class MEWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.A_id = 2
        self.ui = uic.loadUi('./ui/ME.ui')
        self.label = self.ui.label
        # 按钮
        self.tea_btn = self.ui.pushButton
        self.dean_btn = self.ui.pushButton_2
        # 文本框
        self.browser1 = self.ui.textBrowser
        self.browser2 = self.ui.textBrowser_2
        self.init_ui()

    def init_ui(self):
        # 设置首页图片的特征
        pix = QPixmap('./picture/HIT_picture(8).jpg')
        self.label.setPixmap(pix)
        self.label.setStyleSheet('border: 2px solid red')
        self.label.setScaledContents(True)
        # 设置按钮事件
        self.dean_btn.clicked.connect(self.InquireDean)
        self.tea_btn.clicked.connect(self.InquireTea)

    def InquireDean(self):
        sql = 'select D_name, D_id, D_age, D_sex from academy, dean where A_dean_id  = D_id and A_id = %s' % str(
            self.A_id)
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchone()
        self.browser2.setText('姓名 : ' + res[0] + '\n')
        self.browser2.append('年龄 : ' + res[2] + '\n')
        self.browser2.append('性别 : ' + res[3] + '\n')

    def InquireTea(self):
        sql = 'select T_name, T_age, T_sex from teacher where T_academy_id = %s' % self.A_id
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchall()
        self.browser1.setText('------------')
        for i in range(len(res)):
            self.browser1.append('姓名:' + res[i][0] + ' 年龄:' + res[i][1] + ' 性别:' + res[i][2] + '\n')