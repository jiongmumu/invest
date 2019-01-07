# TD sequential

```python
# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)


import datetime
import time

'''
TD Sequential-Style indicator

// S = Sell Signal
// B = Buy Signal
// A = Sell (above bar) or Buy (below bar) Signal that is 'not ideal' - meaning the signal bar's or the previous bar's high or low is not higer or lower than one of the previous 2 bars.
// - This could indicate that waiting another bar will deliver a 'true' signal. (Useful at the beginning of the trend reversal signal, not so much at the end)
//
// Indicator and Rules based on indicator as seen on CoinSheet.org

    Entry:
    There are three methods of entry:
    (a) Enter on the close of the day on which the countdown is completed;
    (b) Long Trades: Enter on the close if Close[i] > Close[i - 4];
        Short Trades: Enter on the close if Close[i] < Close[i - 4];
    (c) Long Trades: Enter on the close if Close[i] > High[i - 2];
        Short Trades: Enter on the close if Close[i] < Low[i - 2]. Index: i ~ Current Bar. In this test we apply the 2nd method.

    Exit:
    Pattern Exit: The current position is liquidated once the new setup is complete and price fails to exceed the furthest price recorded by the recent inactive setup.
    Stop Loss Exit: 
    Long Trades: The difference between the close at the entry bar and the low of the lowest day of the pattern is subtracted from the low of the lowest day. Short Trades: The difference between the high of the highest day of the pattern and the close at the entry bar is added to the high of the highest day.                
    Note: In order to activate a stop loss, the close must exceed the calculated levels.

'''


class strategy:

    ''' Logging function for strategy '''

    def log(self, txt, dt):
        #dt = (self.start_date + datetime.timedelta(k))
        print('%s, %s' % (dt.strftime("%Y-%m-%d %H:%M:%S"), txt))

    '''Initialization '''

    def __init__(self, stock, prices, start_date):
        self.candles_past_to_compare = 4
        self.start_date = start_date
        self.stock = stock
        # Keep a reference to the primary data feed
        self.dataprimary = prices
        # Keep a reference to the "close" line in the primary dataseries
        dataclose = self.dataprimary.close
        # Control vars
        self.live = True
        self.order = None

        self.bearishFlip = False
        self.bullishFlip = False

        self.tdsl = 0  # TD sequence long
        self.tdss = 0  # TD sequence short
        self.buySetup = False  # TD buy setup
        self.sellSetup = False  # TD sell setup
        self.buyCountdown = 0  # TD buy countdown
        self.sellCountdown = 0  # TD sell countdown
        self.buyVal = 0  # buy value at intersection
        self.sellVal = 0  # sell value at intersection

        self.buySig = False
        self.idealBuySig = False
        self.sellSig = False
        self.idealSellSig = False

        # print('-' * 80)
        # print('Strategy Created')
        # print('-' * 80)

    def next(self, dataclose, k, time, rsi_buy):
        self.buySig = False
        self.sellSig = False
        self.idealBuySig = False
        self.idealSellSig = False

        # Calculate td sequential values if enough bars
        #if len(dataclose)-k > self.candles_past_to_compare:

        # begin of sequence, bullish or bearish flip
        if dataclose[k] < dataclose[k-self.candles_past_to_compare] and dataclose[k-1] > \
                dataclose[k-(self.candles_past_to_compare + 1)]:
            self.bearishFlip = True
            self.bullishFlip = False
            self.tdsl = 0
            self.tdss = 0
            self.sellSetup = False
            self.sellCountdown = 0
        elif dataclose[k] > dataclose[k-self.candles_past_to_compare] and dataclose[k-1] < \
                dataclose[k-(self.candles_past_to_compare + 1)]:
            self.bullishFlip = True
            self.bearishFlip = False
            self.tdss = 0
            self.tdsl = 0
            self.buySetup = False
            self.buyCountdown = 0

        # sequence start
        if dataclose[k] < dataclose[k-self.candles_past_to_compare] and self.bearishFlip:
            self.tdsl += 1
        elif dataclose[k] > dataclose[k-self.candles_past_to_compare] and self.bullishFlip:
            self.tdss += 1

        # sequence intersection
        if self.tdsl == 9:
            self.buySig = (self.dataprimary.low[k] < self.dataprimary.low[k-3] and self.dataprimary.low[k] <
                           self.dataprimary.low[k-2]) or (
                                      self.dataprimary.low[k-1] < self.dataprimary.low[k-2] and self.dataprimary.low[
                                  -1] < self.dataprimary.low[k-3])
            self.bearishFlip = False
            self.tdsl = 0
            self.buySetup = True
            self.buyCountdown = 0
        elif self.tdss == 9:
            self.sellSig = (self.dataprimary.high[0] > self.dataprimary.high[-2] and self.dataprimary.high[0] >
                            self.dataprimary.high[-3]) or (self.dataprimary.high[-1] > self.dataprimary.high[-3] and
                                                           self.dataprimary.high[-1] > self.dataprimary.high[-2])
            self.bullishFlip = False
            self.tdss = 0
            self.sellSetup = True
            self.sellCountdown = 0

        # sequence countdown
        if self.buySetup:
            if self.dataprimary.close[0] <= self.dataprimary.low[k-2]:
                self.buyCountdown += 1
            if self.buyCountdown == 8:
                self.buyVal = dataclose[k]
            elif self.buyCountdown == 13:
                if self.dataprimary.low[k] <= self.buyVal:
                    self.idealBuySig = True
                self.buySetup = False
                self.buyCountdown = 0

        elif self.sellSetup:
            if self.dataprimary.close[0] >= self.dataprimary.high[-2]:
                self.sellCountdown += 1
            if self.sellCountdown == 8:
                self.sellVal = dataclose[k]
            elif self.sellCountdown == 13:
                if self.dataprimary.high[0] >= self.sellVal:
                    self.idealSellSig = True
                self.sellSetup = False
                self.sellCountdown = 0

        if (self.buySig or self.idealBuySig):
            #print('Buy ', k, '\t', self.stock)
        #if self.tdsl >= 8:
            self.log(
                "RSI {} Buy {}:Close {} TD SeqShort {} TD SeqLong {} TD CDBuy {} TD CDSell {}".format(rsi_buy,self.stock,dataclose[k], self.tdss,
                                                                                    self.tdsl, self.buyCountdown,
                                                                                    self.sellCountdown), dt=time)

```

```python

from jqdatasdk import *
import datetime
from td import strategy

import talib


auth('username','pwd')

stocks = get_index_stocks('000001.XSHG')

today = datetime.datetime.now().strftime("%Y-%m-%d")
start_date = (datetime.datetime.now() - datetime.timedelta(60))

for stock in stocks:
    prices = get_price(security=stock, frequency='1d', start_date=start_date, end_date=today)
    #print(prices)
    td = strategy(stock=stock, prices = prices,start_date=start_date)
    dataclose = prices['close']
    slow_rsi = talib.RSI(dataclose, 6)
    quick_rsi = talib.RSI(dataclose, 12)
    for k in range(15,len(dataclose)):
        date = prices.index[k]
        #print(prices.index[k])
        # whether rsi is strong
        rsi_buy = (slow_rsi[date] < 30 and quick_rsi[date] < 30 and (abs(slow_rsi[date]-quick_rsi[date]) < 3))
        td.next(dataclose=dataclose, k=k, time=date, rsi_buy = rsi_buy)

```

