import pandas as pd
import numpy as np

# 聚合
sales = [{'account': 'Jones LLC', 'type': 'a', 'Jan': 150, 'Feb': 200, 'Mar': 140},
         {'account': 'Alpha Co', 'type': 'b', 'Jan': 200, 'Feb': 210, 'Mar': 215},
         {'account': 'Blue Inc', 'type': 'a', 'Jan': 50, 'Feb': 90, 'Mar': 95}]

df2 = pd.DataFrame(sales)

df2.groupby('type').groups

for k, v in df2.groupby('type'):
    print(k)
    print(v)

# 聚合后再计算
df2.groupby('type').count()
df2.groupby('Jan').sum()

# 各类型产品的销售数量和销售总额
df2.groupby('type').aggregate({'type': 'count', 'Feb': 'sum'})

group = ['x', 'y', 'z']
data = pd.DataFrame({
    'group': [group[x] for x in np.random.randint(0, len(group), 10)],
    'salary': np.random.randint(5, 50, 10),
    'age': np.random.randint(15, 60, 10)
})

data.groupby('group').agg('mean')
data.groupby('group').mean().to_dict()
data.groupby('group').transform('mean')

# 数据透视表
pd.pivot_table(
    data,
    values='salary',
    columns='group',
    index='age',
    aggfunc='count',
    margins=True
).reset_index()
# group  age    x    y    z  All
# 0       16  1.0  NaN  NaN    1
# 1       17  1.0  NaN  NaN    1
# 2       19  1.0  NaN  NaN    1
# 3       20  1.0  NaN  NaN    1
# 4       30  1.0  NaN  1.0    2
# 5       44  NaN  2.0  NaN    2
# 6       48  1.0  NaN  NaN    1
# 7       58  NaN  1.0  NaN    1
# 8      All  6.0  3.0  1.0   10

pd.pivot_table(
    data,
    values='salary',
    columns='group',
    index='age',
    aggfunc='count',
    margins=False
).reset_index()
# group  age    x    y    z
# 0       16  1.0  NaN  NaN
# 1       17  1.0  NaN  NaN
# 2       19  1.0  NaN  NaN
# 3       20  1.0  NaN  NaN
# 4       30  1.0  NaN  1.0
# 5       44  NaN  2.0  NaN
# 6       48  1.0  NaN  NaN
# 7       58  NaN  1.0  NaN

