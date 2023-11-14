import pandas as pd
import numpy as np

group = ['x', 'y', 'z']

#   group  age
# 0     y   41
# 1     y   31
# 2     y   25
# 3     y   44
# 4     y   42
# 5     x   36
# 6     z   22
# 7     x   27
# 8     z   23
# 9     x   47
data1 = pd.DataFrame({
    "group": [group[x] for x in np.random.randint(0, len(group), 10)],
    "age": np.random.randint(15, 50, 10)
})

#   group  salary
# 0     z      22
# 1     z      38
# 2     z      13
# 3     x      41
# 4     z      23
# 5     z      28
# 6     y       8
# 7     x      15
# 8     x      33
# 9     x       7
data2 = pd.DataFrame({
    "group": [group[x] for x in np.random.randint(0, len(group), 10)],
    "salary": np.random.randint(5, 50, 10),
})

#   group  age  salary
# 0     x   47      37
# 1     z   37      14
# 2     y   43      40
# 3     y   32      15
# 4     x   31      43
# 5     x   28      23
# 6     x   40      49
# 7     y   47      36
# 8     z   31      38
# 9     y   26      44
data3 = pd.DataFrame({
    "group": [group[x] for x in np.random.randint(0, len(group), 10)],
    "age": np.random.randint(15, 50, 10),
    "salary": np.random.randint(5, 50, 10),
})

# 一对一
pd.merge(data1, data2)
#   group  age  salary
# 0      y   41       8
# 1      y   31       8
# 2      y   25       8
# 3      y   44       8
# 4      y   42       8
# 5      x   36      41
# 6      x   36      15
# 7      x   36      33
# 8      x   36       7
# 9      x   27      41
# 10     x   27      15
# 11     x   27      33
# 12     x   27       7
# 13     x   47      41
# 14     x   47      15
# 15     x   47      33
# 16     x   47       7
# 17     z   22      22
# 18     z   22      38
# 19     z   22      13
# 20     z   22      23
# 21     z   22      28
# 22     z   23      22
# 23     z   23      38
# 24     z   23      13
# 25     z   23      23
# 26     z   23      28

# 多对一
pd.merge(data3, data2, on='group')
#   group  age  salary_x  salary_y
# 0      x   47        37        41
# 1      x   47        37        15
# 2      x   47        37        33
# 3      x   47        37         7
# 4      x   31        43        41
# 5      x   31        43        15
# 6      x   31        43        33
# 7      x   31        43         7
# 8      x   28        23        41
# 9      x   28        23        15
# 10     x   28        23        33
# 11     x   28        23         7
# 12     x   40        49        41
# 13     x   40        49        15
# 14     x   40        49        33
# 15     x   40        49         7
# 16     z   37        14        22
# 17     z   37        14        38
# 18     z   37        14        13
# 19     z   37        14        23
# 20     z   37        14        28
# 21     z   31        38        22
# 22     z   31        38        38
# 23     z   31        38        13
# 24     z   31        38        23
# 25     z   31        38        28
# 26     y   43        40         8
# 27     y   32        15         8
# 28     y   47        36         8
# 29     y   26        44         8

# 多对多
pd.merge(data3, data2)
#   group  age  salary
# 0     z   31      38

# 连接键类型，解决没有公共列问题
pd.merge(data3, data2, left_on='age', right_on='salary')
#   group_x  age  salary_x group_y  salary_y
# 0       x   28        23       z        28

# 连接方式
# 内连接，不指明连接方式，默认都是内连接
pd.merge(data3, data2, on='group', how='inner')
# 左连接 left
# 右连接 right
# 外连接 outer
#    group  age  salary_x  salary_y
# 0      x   47        37        41
# 1      x   47        37        15
# 2      x   47        37        33
# 3      x   47        37         7
# 4      x   31        43        41
# 5      x   31        43        15
# 6      x   31        43        33
# 7      x   31        43         7
# 8      x   28        23        41
# 9      x   28        23        15
# 10     x   28        23        33
# 11     x   28        23         7
# 12     x   40        49        41
# 13     x   40        49        15
# 14     x   40        49        33
# 15     x   40        49         7
# 16     z   37        14        22
# 17     z   37        14        38
# 18     z   37        14        13
# 19     z   37        14        23
# 20     z   37        14        28
# 21     z   31        38        22
# 22     z   31        38        38
# 23     z   31        38        13
# 24     z   31        38        23
# 25     z   31        38        28
# 26     y   43        40         8
# 27     y   32        15         8
# 28     y   47        36         8
# 29     y   26        44         8

# 纵向拼接
pd.concat([data1, data2])
#  group   age  salary
# 0     y  41.0     NaN
# 1     y  31.0     NaN
# 2     y  25.0     NaN
# 3     y  44.0     NaN
# 4     y  42.0     NaN
# 5     x  36.0     NaN
# 6     z  22.0     NaN
# 7     x  27.0     NaN
# 8     z  23.0     NaN
# 9     x  47.0     NaN
# 0     z   NaN    22.0
# 1     z   NaN    38.0
# 2     z   NaN    13.0
# 3     x   NaN    41.0
# 4     z   NaN    23.0
# 5     z   NaN    28.0
# 6     y   NaN     8.0
# 7     x   NaN    15.0
# 8     x   NaN    33.0
# 9     x   NaN     7.0
