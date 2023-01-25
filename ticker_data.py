import yfinance as yf
from pandas_datareader import data as pdr



# just seeing what its about
def run_protocol():
    companies = 0
    with open('stonks.txt', 'r') as f:
        companies = f.readlines()
        
    for x in companies:
        # get ticker data
        tick = yf.Ticker(x)
        ticker_history = tick.history(start="2021-01-01", end="2021-12-31", interval='1h', actions=False)
        print(ticker_history)
        
         
         





if __name__ == '__main__':
    
    run_protocol()


