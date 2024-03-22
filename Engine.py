from Algorithm import Algorithm
from Algorithm import Order
import Constants

from datetime import datetime
from datetime import timedelta

import yfinance as yf
import numpy as np

"""
Texas Capital Collective In-House Backtesting Engine
@authors: Saahir Narang, Clint Wang
@date-created: 03/2024
@last-modified: 03/2024
"""


class Engine:

    def __init__(self, startingValue: int, histDataLen: int):
        self.startingValue = startingValue
        self.histDataLen = histDataLen
        self.stock_info = []
        self.algo_result = []

    def __reset__(self):
        self.algo_result = []
        self.stock_info = []

    def run(self,
            ticker: str,
            algo: Algorithm,
            start: datetime = None,
            end: datetime = None,
            step: str = "1d",
            histLength: int = 0) -> np.ndarray:
        """
        runs a trading cycle from start to end dates specified over the time interval step using specified algo
        :param ticker: stock ticker in the form of a string (i.e. TSLA)
        :param algo: a child algorithm to test
        :param start: start date
        :param end: end date
        :param step: time interval step
        :param histLength: the required length of historical data for algorithm
               (i.e. if you need a pricing history of 12 days even at start date)
        """
        self.__reset__()

        # check input
        if (end - start).days < self.histDataLen:
            raise Constants.INVALID_TIME_INTERVAL
        step = step.lower()
        valid_steps = list(Constants.INTERVALS.keys())
        if not (step in valid_steps):
            raise Constants.INVALID_STEP_INTERVAL

        """
        @TODO add different pricing types and optimize
              making a hundred API calls to yahoo finance is suboptimal
        """
        for _iter in (end - start).days * Constants.INTERVALS[step]:
            # get stock info from yahoo finance and run algorithm on it
            iter_start = start + timedelta(days=_iter)
            data_start = start - timedelta(days=Constants.INTERVALS[step] * histLength)
            self.stock_info.append(yf.Ticker(ticker).history(interval=step, start=data_start, end=end))
            self.algo_result.append(algo.run(self.stock_info))
        return self.algo_result

    def getNetGainsAndLosses(self):

        # make sure this method can be called
        if self.stock_info is None or self.algo_result is None:
            raise RuntimeError("No stock has been run by the engine")

        net_change = 0
        for prices, result in zip(self.stock_info, self.algo_result):
            # calculate the gain/loss at each individual step
            net_change += np.dot(prices.Close, result.delta())

        return net_change
