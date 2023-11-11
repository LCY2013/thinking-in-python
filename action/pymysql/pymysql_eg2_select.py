import pymysql
import datetime

TABLE_NAME = 't'
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    db='test',
    charset='utf8mb4')

# 获取cursor游标对象
con1 = conn.cursor()

# 操作的行数
count = con1.execute(format(f'select * from {TABLE_NAME}'))
print(f'查询导 {count} 条记录')

# 获取到一条查询结果
result = con1.fetchone()
print(f'查询导一条记录 {result}')

# 获取所有的查询结果
print(f'查询所有的记录 {con1.fetchall()}')

# 执行批量插入
# values = [(id, id, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),) for id in range(5, 6)]
# try:
#     row = con1.executemany('INSERT INTO ' + TABLE_NAME + '(`id`, `a`, `t_modified`) values(%s,%s,%s)', values)
#     print(row)
#     conn.commit()
# except Exception as e:
#     print(e)

# 关闭游标连接
con1.close()
conn.close()
