from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from db_init import cursor, db
from random import *


class StuPlatWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('./ui/StuPlat.ui')
        # 按钮
        self.info_btn = self.ui.pushButton
        self.course_btn = self.ui.pushButton_2
        self.select_btn = self.ui.pushButton_3
        self.inquire_btn = self.ui.pushButton_4
        # 输入栏
        self.cid_line1 = self.ui.lineEdit
        self.cid_line2 = self.ui.lineEdit_2
        # 文本框
        self.browser = self.ui.textBrowser
        self.init_ui()

    def init_ui(self):
        # 设置按钮对应的事件
        self.info_btn.clicked.connect(self.info)
        self.course_btn.clicked.connect(self.list)
        self.select_btn.clicked.connect(self.select)
        self.inquire_btn.clicked.connect(self.inquire)

    def info(self):
        self.browser.setText('-----------\n')
        sql = 'select * from student where S_id = %s' % self.sid
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchall()
        self.browser.append('姓名 : ' + res[0][0] + '\n')
        self.browser.append('学号 : ' + str(res[0][1]) + '\n')
        self.browser.append('年龄 : ' + res[0][2] + '\n')
        self.browser.append('性别 : ' + res[0][3] + '\n')
        self.browser.append('班号 : ' + str(res[0][4]) + '\n')
        sql = 'select avg(grade) from grade group by S_id having S_id = %s' % self.sid
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchone()
        self.browser.append('平均成绩 : ' + str(res[0]) + '\n')
        sql = 'select D_name from dean where D_id in (select A_dean_id from academy where A_id in (select C_academy_id from class where C_num in (select S_class_num from student where S_id = %s)))' % self.sid
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchone()
        self.browser.append('院长名 : ' + res[0] + '\n')

    def list(self):
        self.browser.setText('-----------\n')
        sql = 'select * from course'
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchall()
        for i in range(len(res)):
            self.browser.append(str(res[i][1]) + ':' + res[i][0] + '\n')

    def select(self):
        cid = self.cid_line1.text()
        # 判断课程代码是否有效
        if cid == '' or not cid.isdigit():
            self.cid_line1.setText('输入的课程代码无效!')
            return
        # 判断课程代码是否存在
        sql = 'select * from course where C_id = %s' % cid
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchall()
        if len(res) == 0:
            self.cid_line1.setText('输入的课程代码不存在!')
            return
        # 判断学生是否已经选了这门课
        sql = 'select * from grade where S_id = %s and C_id = %s' % (self.sid, cid)
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchall()
        if not len(res) == 0:
            self.cid_line1.setText('你已经选过这门课!')
            return
        # 选课操作
        sql = 'insert into grade (S_id, C_id, grade) values (%s, %s, \'%s\')' % (self.sid, cid, str(randint(50, 100)))
        cursor.execute(sql)
        db.commit()
        self.browser.setText('选课成功!')
        self.cid_line1.clear()

    def inquire(self):
        cid = self.cid_line2.text()
        # 判断课程代码是否有效
        if cid == '' or not cid.isdigit():
            self.cid_line2.setText('输入的课程代码无效!')
            return
        # 判断课程代码是否存在
        sql = 'select * from course where C_id = %s' % cid
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchall()
        if len(res) == 0:
            self.cid_line2.setText('输入的课程代码不存在!')
            return
        # 判断学生是否已经选了这门课
        sql = 'select * from grade where S_id = %s and C_id = %s' % (self.sid, cid)
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchall()
        if len(res) == 0:
            self.cid_line2.setText('你没有选过这门课!')
            return
        self.browser.setText(res[0][2])
        self.cid_line2.clear()
