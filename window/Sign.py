from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget
from db_init import cursor, db


class SignWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('./ui/Sign.ui')
        self.label = self.ui.label
        # 输入栏
        self.name_line = self.ui.lineEdit_2
        self.id_line = self.ui.lineEdit
        self.age_line = self.ui.lineEdit_3
        self.sex_line = self.ui.lineEdit_4
        self.aid_line = self.ui.lineEdit_5
        self.pwd_line = self.ui.lineEdit_6
        # 按钮
        self.btn = self.ui.pushButton
        self.init_ui()

    def init_ui(self):
        # 设置首页图片的特征
        pix = QPixmap('./picture/HIT_picture(13).jpg')
        self.label.setPixmap(pix)
        self.label.setStyleSheet('border: 2px solid red')
        self.label.setScaledContents(True)
        # 设置按钮对应事件
        self.btn.clicked.connect(self.sign)

    # 清空输入框
    def my_clear(self):
        self.id_line.clear()
        self.name_line.clear()
        self.age_line.clear()
        self.sex_line.clear()
        self.aid_line.clear()
        self.pwd_line.clear()

    def sign(self):
        name = self.name_line.text()
        sid = self.id_line.text()
        age = self.age_line.text()
        sex = self.sex_line.text()
        aid = self.aid_line.text()
        pwd = self.pwd_line.text()
        # 判断输入是否全
        if name == '' or sid == '' or age == '' or sex == '' or aid == '' or pwd == '':
            self.my_clear()
            self.name_line.setText('任意一项不能为空!')
            return
        self.my_clear()
        # 判断输入的学号是有效
        if not sid.isdigit():
            self.my_clear()
            self.id_line.setText('输入的学号无效!')
            return
        self.my_clear()
        # 判断学号是否已经存在
        sql = 'select * from student where S_id = %s' % sid
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchall()
        print(res)
        if not len(res) == 0:
            self.my_clear()
            self.id_line.setText('该学号已经存在!')
            return
        self.my_clear()
        # 判断年龄是否有效
        if not age.isdigit() or int(age) < 1:
            self.my_clear()
            self.age_line.setText('输入的年龄无效!')
            return
        self.my_clear()
        # 判断性别是否有效
        if not sex == '男' and not sex == '女':
            self.my_clear()
            self.sex_line.setText('输入的性别无效!')
            return
        self.my_clear()
        # 判断学院号是否有效
        if not aid.isdigit():
            self.my_clear()
            self.aid_line.setText('输入的学院号无效!')
            return
        self.my_clear()
        # 判断学院是否存在
        sql = 'select * from academy where A_id = %s' % aid
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchall()
        if len(res) == 0:
            self.my_clear()
            self.aid_line.setText('输入的学院号不存在!')
            return
        self.my_clear()
        # 学生注册
        cid = randint(1, 5)
        try:
            sql = 'insert into class (C_num, C_academy_id) values (%s, %s)' % (str(cid), aid)
            cursor.execute(sql)
            sql = 'insert into student (S_name, S_id, S_age, S_sex, S_class_num, S_pwd) values (\'%s\', %s, \'%s\', \'%s\', %s, \'%s\')' % (
                name, sid, age, sex, str(cid), pwd)
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            db.rollback()
        self.name_line.setText('注册成功!')
