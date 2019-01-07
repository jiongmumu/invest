# python基本

## 保存文件到本地

```python
import base64
from IPython.display import HTML

# 下载文件到本地，创建链接！牛逼！
def create_download_link( df, title = "Download CSV file", filename = "data.csv"):
    csv = df.to_csv()
    b64 = base64.b64encode(csv.encode())
    payload = b64.decode()
    html = '<a download="{filename}" href="data:text/csv;base64,{payload}" target="_blank">{title}</a>'
    html = html.format(payload=payload,title=title,filename=filename)
    return HTML(html)
```

## 获取当前时间

```python
import datetime
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```



## seaborn画图

```python
import seaborn as sns
stock_id = '000001.XSHE'
df = get_price(stock_id, count = 30, end_date='2018-11-02', frequency='daily')
sns.regplot(x="close", y="volume", data=df)
sns.lmplot(x="close", y="volume",data=df)
```

![](../.gitbook/assets/image%20%282%29.png)



