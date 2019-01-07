# 如何使用JoinQuant编写策略

## **如何使用JoinQuant取数据**

\(1\)取行情数据  
详见：[股票行情数据](https://www.joinquant.com/post/495)  
\(2\)取财务数据  
详见：[基本面数据](https://www.joinquant.com/post/509)

## 设置股票池

```python
stocks = get_index_stocks('000300.XSHG')  
set_universe(stocks)
```

## RSI

```python
def calRSI(stocks):
    rsi = []
    for stock in stocks:
        # 获取股票的收盘价数据,talib参数取14，前14天的rsi无法计算，所以取15天的数据
        prices = attribute_history(stock, 15, '1d', ('close'))
        # 创建RSI买卖信号，包括参数timeperiod
        # 注意：RSI函数使用的price必须是narray
        rsi += [talib.RSI(prices['close'].values, timeperiod=14)[-1]]

    return rsi
```

{% embed url="https://www.joinquant.com/post/1023?f=2016newyearsum" caption="" %}

