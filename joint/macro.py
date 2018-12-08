import os
from jqdatasdk import *


# 查询分地区农林牧渔业总产值表(季度累计) 的前10条数据
q = query(macro.MAC_INDUSTRY_AREA_AGR_OUTPUT_VALUE_QUARTER
    ).limit(10)
df = macro.run_query(q)

