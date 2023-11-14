import pandas as pd
import numpy as np

df = pd.DataFrame({"A": [5, 3, None, 4],
                   "B": [None, 2, 4, 3],
                   "C": [4, 3, 8, 5],
                   "D": [5, 4, 2, None]})
# 导出为.xlsx文件
df.to_excel(excel_writer=r'file.xlsx')

# 设置Sheet名称
df.to_excel(excel_writer=r'file.xlsx', sheet_name='sheet1')

# 设置索引,设置参数index=False就可以在导出时把这种索引去掉
df.to_excel(excel_writer=r'file.xlsx', sheet_name='sheet1', index=False)

# 设置要导出的列
df.to_excel(excel_writer=r'file.xlsx', sheet_name='sheet1',
            index=False, columns=['A', 'B'])

# 设置编码格式
encoding = 'utf-8'

# 缺失值处理
na_rep = 0  # 缺失值填充为0

# 无穷值处理
inf_rep = 0

# 导出为.csv文件
df.to_csv('./file.csv')

# 性能
df.to_pickle('xx.pkl')

# df.agg(sum)  # 快 The provided callable <built-in function sum> is currently using DataFrame.sum.
df.agg('sum')  # 快
df.agg(lambda x: x.sum())  # 慢
