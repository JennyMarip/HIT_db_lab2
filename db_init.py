import pymysql

db = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="zl304036",
    charset="utf8",
    database="db_lab2",
)  # 连接数据库
cursor = db.cursor()
# 创建视图
try:
    sql = 'create view s_book as (select * from book where B_BS_id = 1)'
    cursor.execute(sql)
    sql = 'create view t_book as (select * from book where B_BS_id = 2)'
    cursor.execute(sql)
    db.commit()
    # 创建索引
    sql = 'create index sid_index on student(S_id)'
    cursor.execute(sql)
    db.commit()
except Exception as e:
    db.rollback()
