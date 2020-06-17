import requests
import pandas as pd
from pprint import pprint
from django.shortcuts import render
from .dataCollect import getDailyDataFrameData

from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from math import pi
import datetime


def stockData(request):
    # We use get_data method from utils
    source = getDailyDataFrameData('LTM.SN', '5min')

    increasing = source.close > source.open
    decreasing = source.open > source.close
    w = 12 * 60 * 60 * 1000
    print(source)
    TOOLS = "pan, wheel_zoom, box_zoom, reset, save"

    title = 'LTM daily chart'

    p = figure(x_axis_type="datetime", tools=TOOLS,
               plot_width=700, plot_height=500, title=title)

    p.line(source.date, source.high)

    script, div = components(p)

    return render(request, 'stockData/stockData.html', {'script': script, 'div': div})
