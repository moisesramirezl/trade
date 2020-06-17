import requests
import pandas as pd
import numpy as np
from pprint import pprint
from django.shortcuts import render
from .dataCollect import getDailyDataFrameData

# plot lib
from bokeh.plotting import figure
from bokeh.embed import components
import datetime

# other plot lib
import matplotlib.pyplot as plt
import matplotlib


def stockPriceBasicStats(request):
    nemo = "LTM.SN"
    dataFrame = getDailyDataFrameData(nemo, '5min')
    print(dataFrame)
    colors = ['r', 'b', 'g', 'y', 'c', 'm']

    stat = 'close'

    statMin = min(dataFrame[stat])
    statMax = max(dataFrame[stat])
    statAvg = np.mean(dataFrame[stat])

    print(dataFrame[dataFrame[stat] == statMin])

    dateStatMin = dataFrame[dataFrame[stat] == statMin]['date']
    dateStatMin = dateStatMin[dateStatMin.index[0]].date()
    dateStatMax = dataFrame[dataFrame[stat] == statMax]['date']
    dateStatMax = dateStatMax[dateStatMax.index[0]].date()

    plt.style.use('fivethirtyeight')
    plt.plot(dataFrame['date'], dataFrame[stat],
             color='r', linewidth=3, label=stat, alpha=0.8)
    plt.xlabel('date')
    plt.ylabel('CLP $')
    plt.title('%s Resumen Diario' % nemo)
    plt.legend(prop={'size': 10})
    plt.grid(color='k', alpha=0.4)

    return render(request, 'stockData/stockPriceBasicStats.html', {'info': plt.show()})


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
