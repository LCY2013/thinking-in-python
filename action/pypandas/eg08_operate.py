import pandas as pd

df = pd.DataFrame({"A": [5, 3, None, 4],
                   "B": [None, 2, 4, 3],
                   "C": [4, 3, 8, 5],
                   "D": [5, 4, 2, None]})

# 算数运算
# 两列之间的加减乘除
df['A'] * df['C']

# 任意一列加/减一个常数值，这一列中的所有值都加/减这个常数值
df['A'] + 5

# 比较运算
df['A'] > df['C']

# count非空值计数
df.count()

# 非空值每列求和
df.sum()
df['A'].sum()

# mean求均值
df['A'].mean()

# max求最大值
df['A'].max()

# min求最小值
df['A'].min()

# median求中位数
df['A'].min()

# mode求众数
df['A'].mode()

# var求方差
df['A'].var()

# std求标准差
df['A'].std()
