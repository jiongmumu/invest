import talib
from jqdatasdk import *
import os
import datetime

import plotly.offline as pyoff
from plotly import tools
import plotly.graph_objs as go

from plotly.offline import init_notebook_mode

auth(os.environ['JOINT_QUANT_USERNAME'],os.environ['JOINT_QUANT_PWD'])

stocks = get_index_stocks('000001.XSHG')

today = datetime.datetime.now().strftime("%Y-%m-%d")
start_date = (datetime.datetime.now() - datetime.timedelta(100))

#init_notebook_mode(connected=True)


def draw_candle_stick_macd(prices):
    candle = go.Candlestick(x=prices.index,
                           open=prices['open'],
                           high=prices['high'],
                           low=prices['low'],
                           close=prices['close'])

    #crows = talib.CDL2CROWS(prices['open'], prices['high'], prices['low'], prices['close'])

    #talib_result = talib.CORREL(prices['high'], prices['low'], timeperiod=5)
    talib_result = talib.TRIMA(prices['close'])

    # shared_xaxes used to control multiple axes zoom at the same time!
    #fig = tools.make_subplots(rows=2, cols=1, shared_xaxes=True,subplot_titles=(str(stock),'2CRWOS'))
    fig = tools.make_subplots(rows=1, cols=1)

    #print('macd:', macd[27:])
    talib_result_line = go.Scatter(x=prices.index,y=talib_result, line = dict(color = ('rgb(255,0,0)')),name='talib_result')
    fig.append_trace(candle, 1, 1)
    fig.append_trace(talib_result_line, 2, 1)

    pyoff.plot(fig)  # 离线方式绘图

def print_not_zero(x):
    if x!=0:
        print(x.index, x)

for stock in stocks:
    prices = get_price(security=stock, frequency='1d', start_date=start_date, end_date=today)
    prices.index = prices.index.strftime("%Y-%m-%d")
    draw_candle_stick_macd(prices)

    # using crows
    # crows = talib.CDL3BLACKCROWS(prices['open'], prices['high'], prices['low'], prices['close'])
    # print(stock)
    # if crows.sum() != 0:
    #     #iterrows for dataframe
    #     #iteritems for series
    #     for index, row in crows.iteritems():
    #         if row!=0:
    #             print(stock, index, row)

    # for k in range(28,len(prices['close'])):
    #     break
    break
