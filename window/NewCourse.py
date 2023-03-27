from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget
from db_init import cursor, db


class NewCourseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('./ui/NewCourse.ui')
        self.label = self.ui.label
        # 输入框
        self.name_line = self.ui.lineEdit_3
        self.id_line = self.ui.lineEdit_2
        self.tid_line = self.ui.lineEdit
        # 按钮
        self.btn = self.ui.pushButton
        self.init_ui()

    def init_ui(self):
        # 设置首页图片的特征
        pix = QPixmap('./picture/HIT_picture(12).jpg')
        self.label.setPixmap(pix)
        self.label.setStyleSheet('border: 2px solid red')
        self.label.setScaledContents(True)
        # 设置按钮对应事件
        self.btn.clicked.connect(self.new_course)

    def my_clear(self):
        self.name_line.clear()
        self.id_line.clear()
        self.tid_line.clear()

    def new_course(self):
        name = self.name_line.text()
        cid = self.id_line.text()
        tid = self.tid_line.text()
        # 判断课程名是否空
        if name == '':
            self.my_clear()
            self.name_line.setText('课程名为空!')
            return
        self.my_clear()
        # 判断课程代码是否有效
        if cid == '' or not cid.isdigit():
            self.my_clear()
            self.id_line.setText('课程代码无效!')
            return
        self.my_clear()
        # 判断讲授教师号是否有效
        if tid == '' or not tid.isdigit():
            self.my_clear()
            self.tid_line.setText('教师号无效!')
            return
        self.my_clear()
        # 判断课程代码是否已经存在
        sql = 'select * from course where C_id = %s' % cid
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchall()
        if not len(res) == 0:
            self.my_clear()
            self.id_line.setText('该课程代码已经存在!')
            return
        self.my_clear()
        # 判断教师号是否存在
        sql = 'select * from teacher where T_id = %s' % tid
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchall()
        if len(res) == 0:
            self.my_clear()
            self.tid_line.setText('输入的教师号不存在!')
            return
        self.my_clear()
        # 开设课程(事务处理)
        try:
            sql = 'insert into course (C_name, C_id) values (\'%s\', %s)' % (name, cid)
            cursor.execute(sql)
            sql = 'insert into teach (T_id, C_id) values (%s, %s)' % (tid, cid)
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            db.rollback()
        self.name_line.setText('操作成功!')