from datetime import datetime
import Algorithm
import yfinance as yf 
import numpy as np 

class Engine:
                
    def __init__(self, startingValue: int, histDataLen: int):
        self.startingValue = startingValue
        self.histDataLen = histDataLen
        self.stock_info = None
        self.algo_result = None 
        
    def run(self, ticker: str, algo: Algorithm, start : datetime = None, end : datetime = None, step : str = "1d"):    
        
        # check input 
        if (end - start).days < self.histDataLen: 
            raise ValueError('Not enough time between start and end date')
        step = step.lower()
        valid_steps = ['1m', '2m', '5m' '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo']
        if not(step in valid_steps):
            raise ValueError('Invalid Step Interval')
        
        # get stock info from yahoo finance and run algorithm on it
        self.stock_info = yf.Ticker(ticker).history(interval=step, start=start, end=end)
        self.algo_result = algo.run(np.stack((self.stock_info.Open, self.stock_info.Close, self.stock_info.High, self.stock_info.Low)))
        return self.algo_result 
        
    def getNetGainsAndLosses(self):
        
        # make sure this method can be called 
        if self.stock_info == None or self.algo_result == None:
            raise RuntimeError("No stock has been run by the engine")
        
        # calculate the gain/loss at each individual step
        individual_change = np.dot(self.stock_info, self.algo_result)
        
        # get net gain/loss at each step 
        net_change = np.add.accumulate(individual_change)
        return net_change