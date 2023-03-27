from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget

from db_init import cursor, db


class TeacherWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('./ui/teachers.ui')
        self.label = self.ui.label_2
        # 按钮
        self.inquire_btn = self.ui.pushButton_2
        self.sign_btn = self.ui.pushButton
        # 输入栏
        self.name_line = self.ui.lineEdit
        self.id_line = self.ui.lineEdit_2
        self.age_line = self.ui.lineEdit_3
        self.sex_line = self.ui.lineEdit_4
        self.sch_line = self.ui.lineEdit_5
        self.tea_name_line = self.ui.lineEdit_6
        # 文本框
        self.browser = self.ui.textBrowser
        self.init_ui()

    def init_ui(self):
        # 设置首页图片的特征
        pix = QPixmap('./picture/HIT_picture(9).jpg')
        self.label.setPixmap(pix)
        self.label.setStyleSheet('border: 2px solid red')
        self.label.setScaledContents(True)
        # 设置按钮事件
        self.sign_btn.clicked.connect(self.tea_sign)
        self.inquire_btn.clicked.connect(self.inquire)

    def tea_sign(self):
        # 获取教师注册信息
        name = self.name_line.text()
        tea_id = self.id_line.text()
        age = self.age_line.text()
        sex = self.sex_line.text()
        sch = self.sch_line.text()
        # 判断输入是否全
        if name == '' or tea_id == '' or age == '' or sex == '' or sch == '':
            self.browser.setText('注册信息不全!')
            return
        self.browser.clear()
        # 判断教师id是否存在
        sql = 'select * from teacher where T_id = %s' % tea_id
        cursor.execute(sql)
        db.commit()
        if len(cursor.fetchall()) != 0:
            self.browser.setText('教师id已经存在!')
            return
        self.browser.clear()
        # 判断年龄是否有效
        if not age.isdigit() or int(age) < 1:
            self.browser.setText('输入的年龄无效!')
            return
        self.browser.clear()
        # 判断性别是否有效
        if not sex == '男' and not sex == '女':
            self.browser.setText('输入的性别无效!')
            return
        self.browser.clear()
        # 判断输入的学院是否有效
        sql = 'select * from academy where A_name = \'%s\'' % sch
        cursor.execute(sql)
        db.commit()
        if len(cursor.fetchall()) == 0:
            self.browser.setText('输入的学院名无效!(计算机学院/机电学院)')
            return
        self.browser.clear()
        # 教师信息注册
        sql = 'select A_id from academy where A_name = \'%s\'' % sch
        cursor.execute(sql)
        db.commit()
        sch_id = cursor.fetchone()
        sql = 'insert into teacher (T_name, T_id, T_age, T_sex, T_academy_id) values (\'%s\', %s, \'%s\', \'%s\', %s)' % (
            name, str(tea_id), age, sex, str(sch_id[0]),)
        cursor.execute(sql)
        db.commit()
        self.name_line.clear()
        self.id_line.clear()
        self.age_line.clear()
        self.sex_line.clear()
        self.sch_line.clear()
        self.browser.setText('教师信息注册成功!')

    def inquire(self):
        tea_name = self.tea_name_line.text()
        # 判断查询是否为空
        if tea_name == '':
            self.browser.setText('查询的教师姓名不能为空!')
            return
        self.browser.clear()
        # 开始查询
        sql = 'select * from teacher where T_name = \'%s\'' % tea_name
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchall()
        if len(res) == 0:
            self.browser.setText('不存在该教师!')
            return
        res = res[0]
        self.browser.setText('姓名 : ' + res[0] + '\n')
        self.browser.append('年龄 : ' + res[2] + '\n')
        self.browser.append('性别 : ' + res[3] + '\n')
        sql = 'select A_name from academy where A_id = %s' % res[4]
        cursor.execute(sql)
        db.commit()
        self.browser.append('学院 : ' + cursor.fetchone()[0] + '\n')
