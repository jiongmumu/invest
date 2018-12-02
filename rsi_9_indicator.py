
from jqdatasdk import *
import datetime
import os
from td import strategy

import talib


auth(os.environ['JOINT_QUANT_USERNAME'],os.environ['JOINT_QUANT_PWD'])

stocks = get_index_stocks('000001.XSHG')
#stocks = get_industry_stocks('C14')

#stocks = get_concept_stocks('')
today = datetime.datetime.now().strftime("%Y-%m-%d")
start_date = (datetime.datetime.now() - datetime.timedelta(40))

for stock in stocks:
    prices = get_price(security=stock, frequency='1d', start_date=start_date, end_date=today)
    #print(prices)
    td = strategy(stock=stock, prices = prices,start_date=start_date)
    dataclose = prices['close']
    slow_rsi = talib.RSI(dataclose, 6)
    quick_rsi = talib.RSI(dataclose, 12)
    for k in range(28,len(dataclose)):
        date = prices.index[k]
        #print(prices.index[k])
        # whether rsi is strong
        rsi_buy = (slow_rsi[date] < 30 and quick_rsi[date] < 30 and (abs(slow_rsi[date]-quick_rsi[date]) < 3))
        td.next(dataclose=dataclose, k=k, time=date, rsi_buy = rsi_buy)
