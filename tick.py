from jqdatasdk import *

import os
auth(os.environ['JOINT_QUANT_USERNAME'],os.environ['JOINT_QUANT_PWD'])

d = get_ticks("000001.XSHE",start_dt=None, end_dt="2018-11-30", count=100)

#print(d)

d.to_csv('~/Documents/invest/output/tick_000001.csv')