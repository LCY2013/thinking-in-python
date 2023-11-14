import pandas as pd
import numpy as np

dates = pd.date_range('20230101', periods=12)
df = pd.DataFrame(np.random.randn(12, 4), index=dates, columns=list('ABCD'))
df

#                    A         B         C         D
# 2023-01-01  1.394429 -0.145605 -0.679593  1.038626
# 2023-01-02  0.205037  0.841557  1.688312  0.903825
# 2023-01-03  0.986291  0.645884 -0.044986 -0.758404
# 2023-01-04  0.438311 -1.423042  0.558908 -1.182800
# 2023-01-05  0.727669 -0.053435  0.802891 -1.191524
# 2023-01-06  1.340068 -1.210336  1.785784 -1.879041
# 2023-01-07  0.646770  0.387732 -0.951078  0.622928
# 2023-01-08  0.315607  0.800321 -0.298577  0.798607
# 2023-01-09 -0.890742 -0.776203  1.915300 -1.523693
# 2023-01-10  0.529310  1.554780 -0.103440 -1.199149
# 2023-01-11  0.629836 -0.971270  0.066829  0.218465
# 2023-01-12 -0.631015 -1.174791  0.756272  0.396126

import matplotlib.pyplot as plt

plt.plot(df.index, df['A'], )
plt.show()

plt.plot(df.index, df['A'],
         color='#FFAA00',  # 颜色
         linestyle='--',  # 线条样式
         linewidth=3,  # 线条宽度
         marker='D')  # 点标记

plt.show()

# seaborn其实是在matplotlib的基础上进行了更高级的API封装，从而使绘图更容易、更美观
import seaborn as sns

# 绘制散点图
plt.scatter(df.index, df['A'])
plt.show()

# 美化plt
sns.set_style('darkgrid')
plt.scatter(df.index, df['A'])
plt.show()
