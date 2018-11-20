
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


from math import pi

import pandas as pd

from bokeh.plotting import figure, show, output_file

from bokeh.io import output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Rect, HoverTool, Range1d, \
    LinearAxis, WheelZoomTool, PanTool, ResetTool


def create_data_source(data_frame):
    '''
    Reference here: https://github.com/bokeh/bokeh/issues/1239
    '''
    return ColumnDataSource(
        data=dict(
            date=[x.strftime("%Y-%m-%d") for x in data_frame['date']],
            open=data_frame['open'],
            close=data_frame['close'],
            high=data_frame['high'],
            low=data_frame['low'],
        )
    )


def candlestick_volume_plot(input_df, plot_title=None):
    '''
    Copyright Shawn Gu, 2016
    The code below is modified based on the snippet from http://bokeh.pydata.org/en/0.11.1/docs/gallery/candlestick.html.
    '''
    px_mids = (input_df['open'] + input_df['close']) / 2.0
    px_spans = abs(input_df['close'] - input_df['open'])

    vol_mids = input_df['volume'] / 2.0
    vol_spans = input_df['volume']
    max_vol = max(input_df['volume'])

    #input_df['date'] = input_df.index
    inc = input_df['close'] >= input_df['open']
    dec = input_df['open'] > input_df['close']

    inc_color = 'red'
    dec_color = 'green'

    width = 12 * 60 * 60 * 1000 * 1.2  # in ms

    #     ht = HoverTool(
    #     tooltips=[
    #             ("date", "@date"),
    #             ("open", "@open"),
    #             ("close", "@close"),
    #             ("high", "@high"),
    #             ("low", "@low"),
    #         ]
    #     )
    # TOOLS = [WheelZoomTool(dimensions=['width']),  ResetTool(),
    #          PanTool(dimensions=['width']), 
    #          # ,ht
    #          ]

    max_px = max(input_df['high'])
    min_px = min(input_df['low'])

    px_range = max_px - min_px

    primary_y_range = (min_px - px_range / 2.0, max_px + px_range * 0.1)
    # print("primary_y_range:", primary_y_range)

    p = figure(x_axis_type="datetime", tools='', plot_height=800, plot_width=850,
               toolbar_location="above", y_range=primary_y_range)

    if plot_title:
        p.title = plot_title

    p.xaxis.major_label_orientation = pi / 4
    p.grid.grid_line_alpha = 0.3
    p.background_fill_color = "black"

    p.extra_y_ranges = {"volume": Range1d(start=0, end=max_vol * 5)}
    p.add_layout(LinearAxis(y_range_name="volume"), 'right')

    px_rect_inc_src = create_data_source(input_df[inc])
    px_rect_dec_src = create_data_source(input_df[dec])

    p.segment(input_df.date[inc], input_df.high[inc], input_df.date[inc], input_df.low[inc], color=inc_color)
    p.segment(input_df.date[dec], input_df.high[dec], input_df.date[dec], input_df.low[dec], color=dec_color)
    p.rect(input_df.date[inc], px_mids[inc], width, px_spans[inc], color=inc_color)
    p.rect(input_df.date[dec], px_mids[dec], width, px_spans[dec], color=dec_color)

    p.rect(input_df.date[inc], vol_mids[inc], width, vol_spans[inc], color=inc_color, y_range_name="volume")
    p.rect(input_df.date[dec], vol_mids[dec], width, vol_spans[dec], color=dec_color, y_range_name="volume")

    # alpha line
    alpha_y_range = (min(input_df.alpha), max(input_df.alpha))
    p2 = figure(x_axis_type="datetime", tools='', plot_height=200, plot_width=800,
               toolbar_location="above", y_range=alpha_y_range)
    input_df = input_df.fillna(0)
    p2.line(input_df.date, input_df.alpha, line_width=2)

    #output_notebook()
    output_file("candlestick.html", title="candlestick.py example")

    show(p2)
    show(p)

df = pd.read_csv('/Users/xiali/Downloads/data.csv')
df["date"] = pd.to_datetime(df.date)
candlestick_volume_plot(df)