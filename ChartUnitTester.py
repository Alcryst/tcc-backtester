import Chart

import numpy as np
import datetime
import yfinance as yf

testChart = Chart.Chart

ssrm_start = datetime.datetime(2024, 2, 14, 12, 0, 0, 0, None)
ssrm_end   = datetime.datetime(2024, 3, 14, 12, 0, 0, 0, None)
testChart.plotCandlestick('ssrm', ssrm_start, ssrm_end, '1h')

aapl_start = datetime.datetime(2024, 3, 21, 9 , 00, 0, 0, None)
aapl_end   = datetime.datetime(2024, 3, 21, 16, 00, 0, 0, None)
testChart.plotCandlestick('aapl', aapl_start, aapl_end, '1d')
