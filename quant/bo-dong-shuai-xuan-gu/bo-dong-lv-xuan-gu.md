# 波动率选股

* 较低涨幅品种指股票年化收益率与无风险利率之差除以基准收益率与无风险利率之差小于0.5的股票。
* 本策略无风险利率特指：0.035



* [ ] 为什么要选择波动率小的呢？

```python
import pandas as pd
import datetime
from jqfactor import get_factor_values
from jqlib.alpha191 import *
from jqlib.technical_analysis import *


stocks = get_index_stocks('000030.XSHG')
#today = context.current_dt

benchmark_stock = '000300.XSHG'
stocks.append(benchmark_stock)

print("stocks len:", len(stocks))

today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 获取universe中股票的过去20天(不包含今天)的每天的平均价
hist = history(20, security_list = stocks, field='close')

# 移除重复列
hist = hist.loc[:,~hist.columns.duplicated()]

#hist.loc[:,benchmark_stock]

#print(hist.loc[:,benchmark_stock].iloc[-1])
#print(hist.loc[:,benchmark_stock].iloc[0])
#print(hist[benchmark_stock])
#print(np.roll(hist[benchmark_stock], 1))
#hist.loc[:,benchmark_stock].iloc[-1]/hist.loc[:,benchmark_stock].iloc[0]
rts = hist[benchmark_stock]/np.roll(hist[benchmark_stock], 1) - 1
#print(rts)
```

```python
# 基准收益率
bm_return = hist.loc[:,benchmark_stock].iloc[-1]/hist.loc[:,benchmark_stock].iloc[0]

# 无风险利率
rf_return = 0.035


changes = []
vols   = []
returns = []


for stock in stocks:
    # 计算股票的收益和收益波动率
    rt=hist.loc[:,stock].iloc[-1]/hist.loc[:,stock].iloc[0]
    rts = hist[stock]/np.roll(hist[stock], 1) - 1
    vol = np.std(rts[1:])

    changes.append(((rt-rf_return)/(bm_return-rf_return)))
    vols.append(vol)
    returns.append(rt)

print(len(stocks), len(vols), len(returns))

df = pd.DataFrame({'stocks':stocks, 
                   'changes':changes, 
                   'vols':vols, 'returns':returns})
# 筛选符合条件的股票
signal_stocks = list(df[df.vols<0.2].stocks.values)

create_download_link(df.sort_values('returns', ascending=[False]))

```

{% embed url="https://wizardforcel.gitbooks.io/python-quant-uqer/content/194.html" %}

