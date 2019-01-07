# 术语和指标

| VWAP | value weighted average price |
| :--- | :--- |
| DTM | 如果开盘价≤昨日开盘价，DTM=0 如果开盘价＞昨日开盘价，DTM=\(最高价-开盘价\)和\(开盘价-昨日开盘价\)的较大值 |
| ADTM | 　　1.如果开盘价≤昨日开盘价，DTM=0  　　如果开盘价＞昨日开盘价，DTM=\(最高价-开盘价\)和\(开盘价-昨日开盘价\)的较大值  　　2.如果开盘价≥昨日开盘价，DBM=0  　　如果开盘价＜昨日开盘价，DBM=\(开盘价-最低价\)  　　3.STM=DTM在N日内的和  　　4.SBM=DBM在N日内的和  　　5.如果STM&gt;SBM,ADTM=\(STM-SBM\)/STM  　　如果STM&lt;SBM,ADTM=\(STM-SBM\)/SBM  　　如果STM=SBM,ADTM=0  　　6.ADTMMA=ADTM的M日简单移动平均  　　7.参数N设置为23日，参数M设置为8日 |

