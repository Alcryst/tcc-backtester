import datetime
import Algorithm
import yfinance as yf 

class Engine:
        
    def __init__(self, startingValue: int, histDataLen: int):
        self.startingValue = startingValue
        self.histDataLen = histDataLen
        
    def run(self, ticker: str, algo: Algorithm, start : datetime = None, end : datetime = None, step : str = "1d"):    
        
        # check input 
        if (end - start).days < self.histDataLen: 
            raise ValueError('Not enough time between start and end date')
        step = step.lower()
        valid_steps = ['1m', '2m', '5m' '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo']
        if not(step in valid_steps):
            raise ValueError('Invalid Step Interval')
        
        # get stock info from yahoo finance and run algorithm on it
        stock_info = yf.Ticker(ticker)
        print(stock_info.history)
        