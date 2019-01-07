# 历史总是相似 牛市还在延续- 现在熊市会延续多久呢

不知道现在的熊市会延续多久，看这个股票涨成这样= =不知道现在市场到底算是什么状况。改一下原来的程序对比一下形状，但好像现在跌的还没有那么厉害？

![](../.gitbook/assets/image%20%2813%29.png)

```python
import datetime as dt
import numpy as np
import seaborn as sns
sns.set_style('white')
from matplotlib import pyplot as plt

#CAL是通联的一个金融计算库、但是import不进来
#from CAL.PyCAL import *
#font.set_size(20)

index = '000300.XSHG'
data = get_price(security = index, start_date='2007-01-01', end_date='2007-12-01')
data.axes

#data.index = data.tradeDate.apply(lambda x: dt.datetime.strptime(x, '%Y-%m-%d'))

data2 = get_price(security =index, start_date='2014-08-30', end_date='2015-06-28')
#data2.index = data2.tradeDate.apply(lambda x: dt.datetime.strptime(x, '%Y-%m-%d'))

data3 = get_price(security =index, start_date='2018-01-01', end_date='2018-11-18')

data['2006 - 2008'] = data['close']
data = data[['2006 - 2008']]
data['2014 - 2015'] = np.nan
data['2014 - 2015'][:len(data2.close.values)] = data2.close.values

data['2018 - '] = np.nan
data['2018 - '][:len(data3.close.values)] = data3.close.values

data = data[['2006 - 2008', '2014 - 2015', '2018 - ']]
data.plot(figsize=(8,4), grid = False)
plt.legend([u'2007 bull', u'2015 bull', u'2018 bear'], loc = 'best')
sns.despine()

```

![](../.gitbook/assets/image%20%283%29.png)



{% embed url="https://wizardforcel.gitbooks.io/python-quant-uqer/content/57.html" %}

这个文章的事件驱动的其余部分都需要uqer的api，所以就不能实现了= =算了。

