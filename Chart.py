import numpy as np
import datetime
import matplotlib.pyplot as plt
import yfinance as yf

class Chart:

    def plotPerformance(self, arr: np.ndarray, ticker: str, start: datetime.datetime,
                        end: datetime.datetime, step: str):
        candlePlotNum = self.plotCandlestick(ticker=ticker, start=start, end=end, step=step)
        plt.figure(candlePlotNum)
        #now we have the candle stick plot.time to plot the gains
        #is arr the net gains and losses per time step?
        y_vals = np.cumsum(arr)
        plt.plot(y_vals, color='blue')
        return

    @staticmethod
    def plotCandlestick(ticker: str, start: datetime.datetime,
                        end: datetime.datetime, step: str):
        # check input
        if end <= start:
            raise ValueError('Not enough time between start and end date')
        step = step.lower()
        valid_steps = ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo']
        if not (step in valid_steps):
            raise ValueError('Invalid Step Interval')

        data = yf.Ticker(ticker).history(interval=step, start=start, end=end)
        print(data) #for when i test
        plt.figure()
        up = data[data['Close'] >= data['Open']]
        down = data[data['Close'] < data['Open']]
        upColor = 'Green'
        downColor = 'Red'
        # Setting width of candlestick elements
        width = .3
        width2 = .03

        # Plotting up prices of the stock
        plt.bar(up.index, up['Close'] - up['Open'], width, bottom=up['Open'], color=upColor)
        plt.bar(up.index, up['High'] - up['Close'], width2, bottom=up['Close'], color=upColor)
        plt.bar(up.index, up['Low'] - up['Open'], width2, bottom=up['Open'], color=upColor)

        # Plotting down prices of the stock
        plt.bar(down.index, down['Close'] - down['Open'], width, bottom=down['Open'], color=downColor)
        plt.bar(down.index, down['High'] - down['Open'], width2, bottom=down['Open'], color=downColor)
        plt.bar(down.index, down['Low'] - down['Close'], width2, bottom=down['Close'], color=downColor)
        plt.title("Jeffery's epic graph")
        plt.show()
        return plt.gcf().number
