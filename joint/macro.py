import os
from jqdatasdk import *

auth(os.environ['JOINT_QUANT_USERNAME'],os.environ['JOINT_QUANT_PWD'])


# 查询分地区农林牧渔业总产值表(季度累计) 的前10条数据
q = query(macro.MAC_INDUSTRY_AREA_AGR_OUTPUT_VALUE_QUARTER
    ).limit(10)
df = macro.run_query(q)

df.to_csv('./output/quarter.csv')

# 查询2014年的分地区农林牧渔业总产值表(年度)
q = query(macro.MAC_INDUSTRY_AREA_AGR_OUTPUT_VALUE_YEAR
        ).filter(macro.MAC_INDUSTRY_AREA_AGR_OUTPUT_VALUE_YEAR.stat_year=='2014')
df = macro.run_query(q)
df.to_csv('./output/year_from_2014.csv')

