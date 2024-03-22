import Chart

import numpy as np
import datetime
import yfinance as yf

import unittest
from unittest.mock import patch
import pandas as pd
import matplotlib.pyplot as plt

testChart = Chart.Chart


"""
Texas Capital Collective Charting Script Unit Tester
@author: Alex Xu
@date-created: 03/2024
@last-modified: 03/2024
"""

class TestChart(unittest.TestCase):
    @patch('yfinance.Ticker.history')
    @patch('matplotlib.pyplot.show')
    def test_plot_candlestick(self, mock_show, mock_history):
        # Define test data
        start_date = datetime.datetime(2022, 1, 3)
        end_date = datetime.datetime(2022, 1, 7)
        test_ticker = "AAPL"

        # Mock yfinance.Ticker.history() to return test data
        mock_data = {
            'Open': [177.830002, 182.630005, 179.610001, 172.699997, 172.889999],
            'High': [182.880005, 182.940002, 180.169998, 175.300003, 174.139999],
            'Low': [177.710007, 179.119995, 174.639999, 171.639999, 171.029999],
            'Close': [182.009995, 179.699997, 174.919998, 172, 172.169998]
        }
        mock_history.return_value = pd.DataFrame(mock_data)

        # Call the plotCandlestick method
        candlestick_plot_num = testChart.plotCandlestick('aapl', start_date, end_date, '1d')

        # Get the current figure
        fig = plt.figure(candlestick_plot_num)

        # Extract bar objects
        bar_containers = fig.get_axes()[0].patches

        # Check candlestick properties
        for i, container in enumerate(bar_containers):
            # Each group of 3 bar containers represents a single candlestick (open, high, low)

            if i % 3 == 0:
                open_price = container.get_height() + container.get_y()
                high_container = bar_containers[i + 1]
                high_price = high_container.get_height() + high_container.get_y()
                low_container = bar_containers[i + 2]
                low_price = low_container.get_y()  # The low price is the bottom of the low container
                close_price = open_price  # Close price is same as open price in a single candlestick
                self.assertAlmostEqual(open_price, mock_data['Open'][i // 3])
                self.assertAlmostEqual(high_price, mock_data['High'][i // 3])
                self.assertAlmostEqual(low_price, mock_data['Low'][i // 3])
                # Check close price by comparing with next candlestick's open price if not last candlestick
                if i // 3 < len(mock_data['Close']) - 1:
                    next_open_price = bar_containers[i + 3].get_height() + bar_containers[i + 3].get_y()
                    self.assertAlmostEqual(close_price, next_open_price)

        # Assert that plt.show() was called
        mock_show.assert_called()


if __name__ == '__main__':
    unittest.main()
