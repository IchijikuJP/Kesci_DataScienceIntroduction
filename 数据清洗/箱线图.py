# 箱线图:box plot
# 可视化基本的统计数据，如离群值、最小/最大值，四分位值等
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../Pokemon.csv")

pd.set_option('display.max_columns', None)  # 给最大列设置为10列
pd.set_option('display.max_rows', None)  # 设置最大可见100行
pd.set_option('display.width', 1000)
data.boxplot(column=['Attack', 'Defense'])
plt.show()

# 加入分类数据列'Legendary'
data.boxplot(column='Attack',by='Legendary')
plt.show()
