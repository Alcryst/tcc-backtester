import pandas as pd

"""
Texas Capital Collective In-House Backtester Parent Algorithm
@authors: Jeffery Xu, Clint Wang
@date-created: 03/2024
@last-modified: 03/2024
"""


class Order:
    """
    A class for placing orders in the backtester
    """
    def __init__(self, buyAmt: int, sellAmt: int):
        self.buyAmt = buyAmt
        self.sellAmt = sellAmt

    def delta(self):
        """
        :return: difference in buy amt and sell amt
        """
        return self.buyAmt - self.sellAmt


class Algorithm:
    """
    A parent algorithm class for child algorithms
    """
    def __init__(self):
        return

    def run(self, histData: pd.DataFrame, **kwargs) -> Order:
        """
        :param histData: a dataframe of historical trading data from YFinance
        :param kwargs: more keyword arguments if necessary
        :return: an order
        """
        raise NotImplementedError("implement the run method")

    def cache(self, args):
        pass
