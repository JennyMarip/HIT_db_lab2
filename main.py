import sys

from PyQt5.QtWidgets import QApplication

from window.MainWindow import MainWindow
from db_init import cursor, db

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w1 = MainWindow()
    w1.ui.show()
    app.exec()
    # 删除数据库初始化时创建的视图与索引
    try:
        sql = 'drop view s_book, t_book'
        cursor.execute(sql)
        sql = 'drop index sid_index on student'
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()


# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
