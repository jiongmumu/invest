# pandas基本

## [去除重复的列](https://stackoverflow.com/questions/14984119/python-pandas-remove-duplicate-columns)

```python
hist = hist.loc[:,~hist.columns.duplicated()]
```

## 排序

```text
#按照某列值排序
df.sort_values('open', ascending=[False])

#按照列排序,只是按照列名排序
df.sort_index(axis=1)
```

## series和dataframe的用法

```text
stocks = get_index_stocks('000009.XSHG')
hist = history(20, security_list = stocks, field='close')
#hist是DataFrame,通过iloc用索引获取series,at获取
hist.iloc[-1].at['000300.XSHG'][0]
```

## 获取DataFrame信息

```python
df.describe()

#形状
print(df.shape)

#查看前后5条
print(df.head())
print(df.tail())

#获取某行某列
print(df.iloc[1:4][:])

#获取跌了的日期
print(df[df.open > df.close])

print(df[df['open'].isin([9.80])])

#选取列向量
print(df.iloc('2018-10-23'))
print(df[:1])

#还可以通过bool_vec选取,长度要匹配
#bool_vec = [True,False,True,False,True]
#print(df[bool_vec])

#value_counts()统计频数
df['close'].value_counts()

#按照列排序,只是按照列名排序
df.sort_index(axis=1)

#增加一新行
df['close-open']=df.close-df.open

df['close-open'].plot()

```

