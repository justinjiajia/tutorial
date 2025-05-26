import streamlit as st
import pandas as pd
import yfinance as yf

ticker = yf.Ticker("AAPL")
 


# ticker.info.get('longName')
# ticker.info.get('sector')
# ticker.info.get('marketCap')

symbol_list = ['AAPL', 'ABBV', 'ABT', 'ACN', 'ADBE', 'AIG', 'AMD', 'AMGN', 'AMT', 'AMZN', 'AVGO', 'AXP', 'BA', 'BAC', 'BK', 'BKNG', 'BLK', 'BMY', 'BRK-B',
               'C', 'CAT', 'CHTR', 'CL', 'CMCSA', 'COF', 'COP', 'COST', 'CRM', 'CSCO', 'CVS', 'CVX', 'DE', 'DHR', 'DIS', 'DUK', 'EMR', 'FDX', 'GD', 'GE', 'GILD', 'GM', 'GOOG', 'GOOGL', 'GS',
               'HD', 'HON', 'IBM', 'INTC', 'INTU', 'ISRG', 'JNJ', 'JPM', 'KO', 'LIN', 'LLY', 'LMT', 'LOW', 'MA', 'MCD', 'MDLZ', 'MDT', 'MET', 'META', 'MMM', 'MO', 'MRK', 'MS', 'MSFT',
               'NEE', 'NFLX', 'NKE', 'NOW', 'NVDA', 'ORCL', 'PEP', 'PFE', 'PG', 'PLTR', 'PM', 'PYPL', 'QCOM', 'RTX', 'SBUX', 'SCHW', 'SO', 'SPG', 'T', 'TGT', 'TMO', 'TMUS', 'TSLA', 'TXN',
               'UNH', 'UNP', 'UPS', 'USB', 'V', 'VZ', 'WFC', 'WMT', 'XOM']



name_list = []
sector_list = []
market_cap_list = []

# Fill in the code below
for ticker in symbol_list:
    stock = yf.Ticker(ticker)
    info = stock.info

    name_list.append(info.get('longName'))
    sector_list.append(info.get('sector'))
    market_cap = info.get('marketCap')
    market_cap_bn = round(market_cap / 1e9, 2)
    market_cap_list.append(market_cap_bn)


ticker_info_df = pd.DataFrame({'Ticker': symbol_list, 'Company':name_list, 'Sector':sector_list, 'Market Cap (B)': market_cap_list})
ticker_info_df.to_csv('ticker_info.csv')    


start_date = "2020-01-01"
end_date = "2025-05-06"  # Update to today's date or use date.today()

# Download OHLC data (Open, High, Low, Close, Volume, etc.)
stock_data = yf.download(
    symbol_list,
    start=start_date,
    end=end_date,
)

# This transformation converts stock data from a wide format (where each ticker is a column) into a long format (where each ticker's data is in separate rows).
long_stock_data = (stock_data.stack(level='Ticker')  # Stack the ticker level; stock_data has a MultiIndex (hierarchical index) where one of the levels is 'Ticker'. stack() pivots the specified level ('Ticker') from columns into rows, making the DataFrame longer (more rows, fewer columns).
             .reset_index()        # After stacking, the DataFrame has a new index structure. reset_index() converts all index levels into regular columns, making it easier to work with the data.
             .rename(columns={'level_1': 'Ticker'}))  # When stacking and resetting, the stacked column might get a default name like 'level_1'. This renames that column back to 'Ticker' for clarity.

st.write(long_stock_data)