# 对于缺失的数据 :
# 使用dropna()函数删除 或用 fillna()函数填充缺失值 或用平均值之类的统计数据填充缺失值
# assert语句: 用来判断语句的真假, 如果为假的话出发AssertionError错误
import pandas as pd

data = pd.read_csv("../Pokemon.csv")

pd.set_option('display.max_columns', None)  # 给最大列设置为10列
pd.set_option('display.max_rows', None)  # 设置最大可见100行
pd.set_option('display.width', 1000)

print(data['Type 2'].head(6))
# 查看Pokemon全体数据集是否有NaN值
# 可以看到共有800个条目，但Type2有414个非空对象，即有386个空对象。
print(data.info())
print(data["Type 2"].value_counts(dropna=False))
print(data["Type 2"].value_counts(dropna=True))

# 查看一下Type2中的缺失值情况
print(data.head(6))
# 使用dropna()删除缺失值
data1 = data  # 待会使用数据来填充缺失值, 所以先将他分配到data1变量
data1["Type 2"].dropna(inplace=True)
# inplace = True表示不创建新的对象 直接对原始对象进行修改
# inplace = False表示对数据进行修改 创建并返回新的对象承载其修改结果
# 默认为False(原对象不变)
# 可以看到原来的nan值都没随机填充上了Flying Dragon等属性
print(data1.dropna().head(6))
print(data['Type 2'].head(6))

# assert语句的用法
assert 1 == 1  # 在False时触发异常
# 是True所以什么都不返回

# 使用notnull()函数判断数据是否缺失 返回bool型数据 这里返回True
# 使用all()函数判断notnull()返回的值是否都为True 是则返回True
# 使用assert断言 语句为真
assert data1['Type 2'].notnull().all()  # 因为已经删除了nan值，所以什么也不返回

# 使用fillna()可以填充缺失值
data["Type 2"].fillna('empty', inplace=True)
assert data['Type 2'].notnull().all()  # 因为无NaN值，所以没有返回值

# 通过assert语句我们可以检查很多东西
# assert data.columns[1] == 'Name'
# assert data.Speed.dtypes == np.int
