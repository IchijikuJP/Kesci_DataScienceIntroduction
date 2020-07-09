from pivot函数 import df1
import pandas as pd

print(df1)
print(pd.melt(df1, id_vars="treatment",
              value_vars=["age", "response"])
      )
