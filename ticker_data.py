import yfinance as yf
from pandas_datareader import data as pdr
import json
import pandas as pd



# just seeing what its about
def run_protocol():
    companies = 0
    with open('stonks.json', 'r') as f:
        companies = json.load(f)
    df_list = []   
    for x in companies:
        # get ticker data
        tick = yf.Ticker(x)
        ticker_history = tick.history(start="2021-01-01", end="2021-12-31", interval='1d', actions=False)
        data = pd.DataFrame(ticker_history)
        data[f'{x}'] = (data['Close'] - data['Open'] )/data['Open']
        # data['mean'] = (data['Close'] + data['Open'] )/2
        data.drop(['High','Open', 'Low', 'Close', 'Volume'], inplace=True, axis=1)
        df_list.append(data)
    
    return df_list
        


def put_datasets_together(df_list):
    df = df_list[0]
    for i in range(1, len(df_list)):
        df = df.merge(df_list[i], on='Date', how='outer')
        
    return df         



if __name__ == '__main__':
    
    df_list = run_protocol()
    full_df = put_datasets_together(df_list)
    full_df.to_csv('ticker_data.csv')
    


