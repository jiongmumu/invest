# 随机森林

## 创建数据集合

```python
import talib
from jqdata import *

test_stock = '399300.XSHE'
start_date = datetime.date(2018, 1,8)
end_date = datetime.date(2018, 11, 23)

trading_days = list(get_all_trade_days())
start_date_index = trading_days.index(start_date)
end_date_index = trading_days.index(end_date)

x_all = []
y_all = []

for index in range(start_date_index, end_date_index):
    # 得到计算指标的所有数据
    start_day = trading_days[index - 30]
    end_day = trading_days[index]
    stock_data = get_price(test_stock, start_date=start_day, end_date=end_day, frequency='daily', fields=['close'])
    close_prices = stock_data['close'].values
    
    #通过数据计算指标
    # -2是保证获取的数据是昨天的，-1就是通过今天的数据计算出来的指标
    sma_data = talib.SMA(close_prices)[-2] 
    wma_data = talib.WMA(close_prices)[-2]
    mom_data = talib.MOM(close_prices)[-2]
    
    features = []
    features.append(sma_data)
    features.append(wma_data)
    features.append(mom_data)
    
    label = False
    if close_prices[-1] > close_prices[-2]:
        label = True
    x_all.append(features)
    y_all.append(label)

# 准备算法需要用到的数据
x_train = x_all[: -1]
y_train = y_all[: -1]
x_test = x_all[-1]
y_test = y_all[-1]
print('data done')

```

## 预测

```python
from sklearn.ensemble import RandomForestClassifier

#开始利用机器学习算法计算，括号里面的n_estimators就是森林中包含的树的数目啦
clf = RandomForestClassifier(n_estimators=10)
#训练的代码
clf.fit(x_train, y_train)
#得到测试结果的代码
prediction = clf.predict(x_test)

# 看看预测对了没
#print(prediction == y_test)
#print('all done')

print(prediction)
print(y_test)
```

## 绘图 某个estimator

```python

# Extract single tree
estimator = clf.estimators_[5]

from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
import pydotplus
from IPython.display import Image, display

#建立缓存变量f
f = StringIO()

#把决策树clf的图形结果输出，仍进缓存f中
export_graphviz(estimator, out_file=f)

# Convert to png using system command (requires Graphviz)
# from subprocess import call
# call(['dot', '-Tpng', 'tree.dot', '-o', 'tree.png', '-Gdpi=600'])


# 取出缓存，画图
graph = pydotplus.graph_from_dot_data(f.getvalue())
# 将图片保存进本地文件中
#graph.write_png("dtree.png")
#画出决策树，也可以用标注的代码画出保存在本地的png图片
#display(Image(filename="dtree2.png"))
display(Image(graph.create_png()))
```

![&#x968F;&#x673A;&#x68EE;&#x6797;&#x67D0;&#x4E2A;&#x6570;&#x7684;&#x5206;&#x7C7B;&#x56FE;](../.gitbook/assets/image%20%281%29.png)

  


{% embed url="https://www.joinquant.com/post/1571?f=study&m=math" %}

