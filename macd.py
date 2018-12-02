import talib
from jqdatasdk import *
import os
import datetime

import plotly.offline as pyoff
from plotly import tools
import plotly.graph_objs as go

#import plotly.plotly as py
import plotly.graph_objs as go

from plotly.offline import init_notebook_mode

import matplotlib.pyplot as plt

# 使用MACD需要设置长短均线和macd平均线的参数
SHORTPERIOD = 12
LONGPERIOD = 26
SMOOTHPERIOD = 9
OBSERVATION = 50

# 1 buy
# -1 sell
# 0 nothing
BUY = 1
SELL = -1
NOTHING = 0

auth(os.environ['JOINT_QUANT_USERNAME'],os.environ['JOINT_QUANT_PWD'])

stocks = get_index_stocks('000001.XSHG')
#stocks = get_industry_stocks('C14')

#stocks = get_concept_stocks('')
today = datetime.datetime.now().strftime("%Y-%m-%d")
start_date = (datetime.datetime.now() - datetime.timedelta(200))

init_notebook_mode(connected=True)

for stock in stocks:
    prices = get_price(security=stock, frequency='1d', start_date=start_date, end_date=today)

    candle = go.Candlestick(x=prices.index,
                           open=prices['open'],
                           high=prices['high'],
                           low=prices['low'],
                           close=prices['close'])

    #diff is difference between 12 days and 26 days
    #macd if average of 9 days of diff
    # hist is difference between diff and macd
    diff, macd, hist = talib.MACD(prices['close'].values, SHORTPERIOD,
                                    LONGPERIOD, SMOOTHPERIOD)

    # 在线方式生成图片，会存到plotly的服务器
    #pyoff.iplot([trace], filename='simple_candlestick')

    # shared_xaxes used to control multiple axes zoom at the same time!
    fig = tools.make_subplots(rows=2, cols=1, shared_xaxes=True)

    #print('macd:', macd[27:])
    hist_bar = go.Bar(x=prices.index,y=hist, name = 'HIST')  # 条形图
    macd_line = go.Scatter(x=prices.index,y=macd, line = dict(color = ('rgb(255,0,0)')), name='MACD')
    diff_line = go.Scatter(x=prices.index,y=diff, line = dict(color = ('rgb(0,0,255)')),name='DIFF')
    fig.append_trace(candle, 1, 1)
    fig.append_trace(hist_bar, 2, 1)
    fig.append_trace(macd_line, 2, 1)
    fig.append_trace(diff_line, 2, 1)

    pyoff.plot(fig)  # 离线方式绘图

    break


    close = prices['close'].values

    plt.figure(1)
    plt.subplot2grid((8, 1), (6, 0))

    ### prices

    plt.subplot2grid((8, 1), (0, 0), rowspan=4)
    plt.plot(close, 'k', lw=1)

    ## MACD

    plt.subplot2grid((8, 1), (6, 0))

    plt.plot(diff, 'red', lw=1)
    plt.plot(macd, 'blue', lw=1)

    plt.subplot2grid((8, 1), (7, 0))

    plt.plot(hist, 'k', lw=2)
    plt.axhline(y=0, color='b', linestyle='-')

    plt.show()

    #print('len prices:{}, len macd:{}', len(prices['close']), len(macd))
    for k in range(28,len(prices['close'])):
        # macd 是长短均线的差值，signal是macd的均线，如果短均线从下往上突破长均线，为入场信号，进行买入开仓操作
        if diff[k] - macd[k] > 0 and diff[k-1] - macd[k-1] < 0 and abs(diff[k]) < 0.2:
            print('buy', prices.index[k], stock,' price: ' ,prices['close'][k], diff[k-1] ,macd[k-1], diff[k] ,macd[k])

        # if diff[k-1] - macd[k-1] < 0 and diff[k-2] - macd[k-2] > 0:
        #     print('{} sell {}', prices.index[k], stock)
    break


