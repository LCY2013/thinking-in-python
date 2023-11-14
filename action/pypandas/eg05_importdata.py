# pip install xlrd
# 导入excel文件
import pandas as pd

excel1 = pd.read_excel(r'action/pypandas/0-num.xlsx')
excel1

# 指定导入哪个Sheet
pd.read_excel(r'action/pypandas/0-num.xlsx', sheet_name=0)

# 支持其他常见的类型
pd.read_csv(r'action/pypandas/2-demo.csv', sep=' ', nrows=10, encoding='utf-8')

pd.read_table(r'action/pypandas/3-demo.txt', sep=' ')

import pymysql

sql = 'SELECT *  FROM t'
conn = pymysql.connect('ip', 'name', 'pass', 'dbname', 'charset=utf8')
df = pd.read_sql(sql, conn)

# 熟悉数据
# 显示前几行
excel1.head(3)

# 行列数量
excel1.shape()

# 详细信息
excel1.info()
excel1.describe()
