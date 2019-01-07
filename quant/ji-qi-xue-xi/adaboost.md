---
description: 参考聚宽的boosting的介绍的文章，构建数据集合，试图绘制mesh查看分类状况。但是把聚宽的1G内存搞爆了== TODO(windows到了再测测)
---

# adaboost

## 构建RSI和5日均线-10日均线的特征数据

```python
import talib
from jqdata import *
import pandas as pd

test_stock = '399300.XSHE'
start_date = datetime.date(2018, 1,8)
end_date = datetime.date(2018, 11, 23)

trading_days = list(get_all_trade_days())
start_date_index = trading_days.index(start_date)
end_date_index = trading_days.index(end_date)

X = []
Y = []

for index in range(start_date_index, end_date_index):
    # 得到计算指标的所有数据
    start_day = trading_days[index - 15]
    end_day = trading_days[index]
    stock_data = get_price(test_stock, start_date=start_day, end_date=end_day, frequency='daily', fields=['close'])
    close_prices = stock_data['close'].values
    
    #通过数据计算指标
    # -2是保证获取的数据是昨天的，-1就是通过今天的数据计算出来的指标
    # talib.RSI(close_prices) 返回的是array,因为用14天的窗口移动计算RSI
    # 算法的效率未来可以提高
    rsi_data = talib.RSI(close_prices)[-2] 
    sma5 = talib.SMA(close_prices,5)[-2]
    sma10 = talib.SMA(close_prices,10)[-2]
    
    features = []
    features.append(rsi_data)
    features.append(sma5-sma10)
    
    label = False
    if close_prices[-1] > close_prices[-2]:
        label = True
    X.append(features)
    Y.append(label)
# X is nested array, need to access like X[1][2].
# will throw: TypeError: list indices must be integers or slices, not tuple
# so need to convert it
X=np.array(X)
Y=np.array(Y)
```

## 创建分类器

```python
import numpy as np
import matplotlib.pyplot as plt

from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_gaussian_quantiles

# Create and fit an AdaBoosted decision tree
bdt = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1),
                         algorithm="SAMME",
                         n_estimators=200)

bdt.fit(X, Y)
```

```python
AdaBoostClassifier(algorithm='SAMME',
          base_estimator=DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=1,
            max_features=None, max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.0, presort=False, random_state=None,
            splitter='best'),
          learning_rate=1.0, n_estimators=200, random_state=None)
```

## 画图

```python
plot_colors = "br"
plot_step = 0.02
class_names = "AB"
plt.figure(figsize=(10, 5))

# Plot the decision boundaries
plt.subplot(121)
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
                     np.arange(y_min, y_max, plot_step))

Z = bdt.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
cs = plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)
plt.axis("tight")

# Plot the training points
for i, n, c in zip(range(2), class_names, plot_colors):
    idx = np.where(y == i)
    plt.scatter(X[idx, 0], X[idx, 1],
                c=c, cmap=plt.cm.Paired,
                s=20, edgecolor='k',
                label="Class %s" % n)
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.legend(loc='upper right')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Decision Boundary')
```

{% embed url="https://www.joinquant.com/post/10626" %}

{% embed url="https://stackoverflow.com/questions/15884527/how-can-i-prevent-the-typeerror-list-indices-must-be-integers-not-tuple-when-c" %}

