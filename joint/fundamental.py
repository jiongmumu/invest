import os
from jqdatasdk import *

auth(os.environ['JOINT_QUANT_USERNAME'],os.environ['JOINT_QUANT_PWD'])


q = query(valuation.turnover_ratio,
              valuation.market_cap,
              indicator.eps
            ).filter(valuation.code.in_(['000001.XSHE', '600000.XSHG']))

panel = get_fundamentals_continuously(q, count=1000)

#panel.to_hdf('./output/fundamentals.h5', 'key')

panel.minor_xs('600000.XSHG').to_csv('./output/fundamental_6000.csv')

