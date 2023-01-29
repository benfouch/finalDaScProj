import yfinance as yf


def pull(ticker_name, save_folder='./Data'):
    try:
        ticker = ticker_name
        ticker_obj = yf.Ticker(ticker)
        data = ticker_obj.history(start='2021-01-01', end='2021-12-31')
        data['delta'] = (data['Close'] - data['Open'] )/data['Open']
        data['mean'] = (data['Close'] + data['Open'] )/2
        data.reset_index(inplace=True, drop=False)
        data.to_csv(save_folder + '/' + ticker_name + '.csv')
        print(f'Success for ticker {ticker_name}')
    except Exception as e:
        print(f'Failed to load ticker {ticker_name} with exception{e}')

pull('MSFT', './Data')