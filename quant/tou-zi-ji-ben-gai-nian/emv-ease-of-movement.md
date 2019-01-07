# EMV - Ease of Movement

 简易波动指标（EMV），是为数不多的考虑价量关系的技术指标。它刻画了股价在下跌的过程当中，由于买气不断的萎靡退缩，致使成交量逐渐的减少，EMV 数值也因而尾随下降，直到股价下跌至某一个合理支撑区，捡便宜货的买单促使成交量再度活跃，EMV 数值于是作相对反应向上攀升，当EMV 数值由负值向上趋近于零时，表示部分信心坚定的资金，成功的扭转了股价的跌势，行情不断反转上扬，并且形成另一次的买进讯号。

计算方法：

第一步

![](https://wizardforcel.gitbooks.io/python-quant-uqer/content/img/20160730113450.jpg)

这里`TH` 为当天最高价，`TL` 为当天最低价，`YH`为前日最高价，`YL` 为前日最低价。`MID > 0`意味着今天的平均价高于昨天的平均价。

第二步

![](https://wizardforcel.gitbooks.io/python-quant-uqer/content/img/20160730113520.jpg)

其中`VOL`代表交易量，`H`、`L`代表同一天的最高价与最低价

第三步

![](https://wizardforcel.gitbooks.io/python-quant-uqer/content/img/20160730113539.jpg)

第四步

`EMV = EM`的N日简单移动平均

第五步

`MAEMV = EMV`的M日简单移动平均

{% embed url="https://wizardforcel.gitbooks.io/python-quant-uqer/content/85.html" %}

There are three parts to the EMV formula: distance moved, volume and the high-low range. First, the distance moved is calculated by comparing the current period's midpoint with the prior period's midpoint, which is the high plus the low divided by two. Distance moved is positive when the current midpoint is above the prior midpoint and negative when the current midpoint is below the prior midpoint. Distance moved is shown as the numerator in the formula below.

```text
Distance Moved = ((H + L)/2 - (Prior H + Prior L)/2) 
Box Ratio = ((V/100,000,000)/(H - L))
1-Period EMV = ((H + L)/2 - (Prior H + Prior L)/2) / ((V/100,000,000)/(H - L))
14-Period Ease of Movement = 14-Period simple moving average of 1-period EMV

```

{% embed url="https://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:ease\_of\_movement\_emv" %}

{% embed url="https://www.youtube.com/watch?v=ZtvLwOYViTw" %}

