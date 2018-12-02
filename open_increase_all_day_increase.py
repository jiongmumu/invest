# whether if open increase all day will increase??
from jqdatasdk import *
import datetime

import talib

import os
auth(os.environ['JOINT_QUANT_USERNAME'],os.environ['JOINT_QUANT_PWD'])


df = get_price('000001.XSHE', start_date='2018-11-01 9:30:00', end_date='2018-11-30 14:00:00', frequency='5m')

df.to_csv('get_price_001.csv')

# for index, row in df.iterrows():
#    print(index, row['open'], row['close'])

close = df['close']
r = talib.MACD(close , fastperiod=12, slowperiod=26, signalperiod=9)

print('r', r)
