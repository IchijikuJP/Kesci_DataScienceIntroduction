import pandas as pd

dic = {"treatment": ["A", "A", "B", "B"],
       "gender": ["F", "M", "F", "M"],
       "response": [10, 45, 5, 9],
       "age": [15, 4, 72, 65]
       }
df1 = pd.DataFrame(dic)
# print(df1)

# 重塑
# print(df1.pivot(index="treatment", columns="gender", values="response"))

