import os
from jqdatasdk import *
import pandas as pd

auth(os.environ['JOINT_QUANT_USERNAME'],os.environ['JOINT_QUANT_PWD'])

#查询贵州茅台2015年之后公布的业绩预告信息，限定返回条数为10条
#
whine_stocks = get_industry_stocks('C15')

# 获取多只股票在某一日期的市值, 利润
df = get_fundamentals(query(
        valuation.market_cap, valuation.pe_ratio, valuation.pb_ratio,
    valuation.code
    ).filter(
        # 这里不能使用 in 操作, 要使用in_()函数
        valuation.code.in_(whine_stocks)
    ), date='2018-12-7')

df.to_csv('./output/finance_fundamental.csv')
df.index = df['code']

#forecast
#df_forecast_list=[]
pub_date = '2017-12-30'
for stock in whine_stocks:
    q=query(finance.STK_FIN_FORCAST).filter(finance.STK_FIN_FORCAST.code==stock,finance.STK_FIN_FORCAST.pub_date>=pub_date)
    df_forecast=finance.run_query(q).sort_values('pub_date', ascending=False)
    if df_forecast.empty:
        continue
    # print('df_forecast:',df_forecast)
    # print('df_forecast.pub_date[0]:', df_forecast.pub_date[0])
    df.loc[stock, 'forecast_pub'] = df_forecast.pub_date[0]
    df.loc[stock, 'f_type'] = df_forecast.type[0]
    df.loc[stock, 'name'] = df_forecast.name[0]
    #df_forecast_list.append(df0.iloc[0:1])

df.to_csv('./output/finance_fundamental_forecast.csv')
#df=pd.concat(df_forecast_list, join='inner')
#df.index = df['code']

#df.to_csv('./output/finance_forecast_whine.csv')

# income statement
df_income_list = []
for stock in whine_stocks:
    q=query(finance.STK_INCOME_STATEMENT.company_name,
            finance.STK_INCOME_STATEMENT.code,
            finance.STK_INCOME_STATEMENT.pub_date,
            finance.STK_INCOME_STATEMENT.start_date,
            finance.STK_INCOME_STATEMENT.end_date,
            finance.STK_INCOME_STATEMENT.total_operating_revenue,
    finance.STK_INCOME_STATEMENT.np_parent_company_owners).filter(finance.STK_INCOME_STATEMENT.code==stock,finance.STK_INCOME_STATEMENT.pub_date>=pub_date,finance.STK_INCOME_STATEMENT.report_type==0)
    df_income=finance.run_query(q).sort_values('pub_date')
    df.loc[stock, 'total_operating_revenue'] =df_income.total_operating_revenue[0]

#df.sort_values('profit_ratio_min', ascending=False).to_csv('./output/finance_whine.csv')

df.to_csv('./output/finance_whine_profit.csv')