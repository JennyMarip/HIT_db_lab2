from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget
from db_init import cursor, db


class SchChangeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('./ui/SchChange.ui')
        self.label = self.ui.label
        # 输入栏
        self.sid_line = self.ui.lineEdit_2
        self.sch_line = self.ui.lineEdit_3
        self.cid_line = self.ui.lineEdit
        # 按钮
        self.btn = self.ui.pushButton
        self.init_ui()

    def init_ui(self):
        # 设置首页图片的特征
        pix = QPixmap('./picture/HIT_picture(10).jpg')
        self.label.setPixmap(pix)
        self.label.setStyleSheet('border: 2px solid red')
        self.label.setScaledContents(True)
        # 设置按钮相应的事件
        self.btn.clicked.connect(self.change)

    def my_clear(self):
        self.cid_line.clear()
        self.sid_line.clear()
        self.sch_line.clear()

    def change(self):
        sid = self.sid_line.text()
        a_name = self.sch_line.text()
        cid = self.cid_line.text()
        # 判断学号是否有效
        if sid == '' or not sid.isdigit():
            self.my_clear()
            self.sid_line.setText('输入的学号无效!')
            return
        self.my_clear()
        # 判断学院名是否有效
        if a_name == '':
            self.my_clear()
            self.sch_line.setText('输入的学院名为空!')
            return
        self.my_clear()
        # 判断班号是否有效
        if cid == '' or not cid.isdigit():
            self.my_clear()
            self.cid_line.setText('输入的班号无效!')
            return
        self.my_clear()
        # 判断学号是否存在
        sql = 'select * from student where S_id = %s' % sid
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchall()
        if len(res) == 0:
            self.my_clear()
            self.sid_line.setText('输入的学号不存在!')
            return
        self.my_clear()
        # 若学号存在,则找到旧班号
        sql = 'select S_class_num from student where S_id = %s' % sid
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchone()
        old_cid = res[0]
        # 判断学院是否存在
        sql = 'select * from academy where A_name = \'%s\'' % a_name
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchall()
        if len(res) == 0:
            self.my_clear()
            self.sch_line.setText('输入的学院不存在!')
            return
        aid = res[0][1]
        self.my_clear()
        # 判断输入的班级是否存在
        sql = 'select C_num from class where C_academy_id = %s' % aid
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchall()
        flag = 0
        for i in range(len(res)):
            if str(res[i][0]) == str(cid):
                flag = 1
        self.my_clear()
        if flag == 0:  # 如果班级不存在那么就增设班级
            sql = 'insert into class (C_num, C_academy_id) values (%s, %s)' % (cid, aid)
            cursor.execute(sql)
            db.commit()
        sql = 'update student set S_class_num = %s' % cid
        cursor.execute(sql)
        db.commit()
        self.sid_line.setText('操作成功!')
        # 如果一个班级没有学生了，那么删除这个班级(需要检查旧的班号)
        sql = 'select * from student where S_class_num = %s' % old_cid
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchall()
        if len(res) == 0:
            sql = 'delete from class where C_num = %s' % old_cid
            cursor.execute(sql)
            db.commit()
            # 删除这个班级的操作
