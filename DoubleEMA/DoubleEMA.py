from typing import List

import numpy as np
import pandas as pd

from Algorithm import Algorithm, Order

"""
Texas Capital Collective Double EMA Algorithm
@authors: Clint Wang
@date-created: 03/2024
@last-modified: 03/2024
"""


def expMovAvg(prices: List[float], length: int, weighting_factor=2) -> float:
    """
    Calculates Exponential Moving Average
    :param prices: list of past close prices
    :param length: period to calculate for
    :param weighting_factor: smoothening factor
    :return: exponential moving average
    """
    ema = np.zeros(len(prices))
    sma = np.mean(prices[:length])
    ema[length - 1] = sma
    alpha = weighting_factor / (length + 1)
    for i in range(length, len(prices)):
        ema[i] = (prices[i] * alpha) + (ema[i - 1] * (1 - alpha))
    return ema


class DoubleEMA(Algorithm):

    def __init__(self, fastLength=9, slowLength=20, breakOutDist=3, orderAmt=10):
        """
        Initializes Double EMA
        :param fastLength: period of fast EMA
        :param slowLength: period of slow EMA
        :param breakOutDist: threshold for break out
        :param orderAmt: fixed amount to buy or sell
        """
        Algorithm.__init__(self)
        self.fastLength = fastLength
        self.slowLength = slowLength
        self.breakOutDist = breakOutDist
        self.orderAmt = orderAmt

        self.__reset__()

    def __reset__(self):
        self.crossOverLongHigh = -1
        self.stopLoss = -1
        self.buy = False
        self.plotShapeBuy = False
        self.plotShapeSell = False
        self.plotConsideration = False

    def run(self, histData: pd.DataFrame, **kwargs) -> Order:
        """
        Runs for one iteration using a strategy based on two Exponential Moving Averages
        """
        fast_average = expMovAvg(histData.Close[-self.fastLength:], self.fastLength)
        slow_average = expMovAvg(histData.Close[-self.slowLength:], self.slowLength)
        close = histData.Close[-1]
        profit_target = 2.002 * self.crossOverLongHigh - self.stopLoss
        if fast_average > slow_average:
            if fast_average > close > slow_average and not self.plotConsideration:
                self.crossOverLongHigh = histData.High[-1]
                self.stopLoss = slow_average
                self.plotConsideration = True
            else:
                if close > self.crossOverLongHigh + self.breakOutDist and not self.buy:
                    self.plotShapeBuy = True
                    self.buy = True
                    return Order(self.orderAmt, 0)
                elif (close < self.stopLoss or close > profit_target) and self.buy:
                    self.plotShapeSell = True
                    self.buy = False
                    self.plotConsideration = False
                    return Order(0, self.orderAmt)
