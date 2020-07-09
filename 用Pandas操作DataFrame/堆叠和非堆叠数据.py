# 1处理多标签索引 2level:未堆叠索引的位置 3swap level:改变内外层索引位置
from pivot函数 import df1
import pandas as pd

df2 = df1.set_index(["treatment", "gender"])
print(df2)  # 堆叠数据

# level 决定索引
print(df2.unstack(level=0))
print(df2.unstack(level=1))

# 改变内外层索引位置
df3 = df2.swaplevel(0, 1)
print(df3)
