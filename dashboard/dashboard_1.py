import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime, date
import sys

sys.path.append('..')

from utils import load_to_df

# ticker = yf.Ticker("AAPL")

# ticker.info.get('longName')
# ticker.info.get('sector')
# ticker.info.get('marketCap')

symbol_list = ['AAPL', 'ABBV', 'ABT', 'ACN', 'ADBE', 'AIG', 'AMD', 'AMGN', 'AMT', 'AMZN', 'AVGO', 'AXP', 'BA', 'BAC', 'BK', 'BKNG', 'BLK', 'BMY', 'BRK-B',
               'C', 'CAT', 'CHTR', 'CL', 'CMCSA', 'COF', 'COP', 'COST', 'CRM', 'CSCO', 'CVS', 'CVX', 'DE', 'DHR', 'DIS', 'DUK', 'EMR', 'FDX', 'GD', 'GE', 'GILD', 'GM', 'GOOG', 'GOOGL', 'GS',
               'HD', 'HON', 'IBM', 'INTC', 'INTU', 'ISRG', 'JNJ', 'JPM', 'KO', 'LIN', 'LLY', 'LMT', 'LOW', 'MA', 'MCD', 'MDLZ', 'MDT', 'MET', 'META', 'MMM', 'MO', 'MRK', 'MS', 'MSFT',
               'NEE', 'NFLX', 'NKE', 'NOW', 'NVDA', 'ORCL', 'PEP', 'PFE', 'PG', 'PLTR', 'PM', 'PYPL', 'QCOM', 'RTX', 'SBUX', 'SCHW', 'SO', 'SPG', 'T', 'TGT', 'TMO', 'TMUS', 'TSLA', 'TXN',
               'UNH', 'UNP', 'UPS', 'USB', 'V', 'VZ', 'WFC', 'WMT', 'XOM']


# name_list = []
# sector_list = []
# market_cap_list = []
 
# for ticker in symbol_list:
#    stock = yf.Ticker(ticker)
#    info = stock.info

#    name_list.append(info.get('longName'))
#    sector_list.append(info.get('sector'))
#    market_cap = info.get('marketCap')
#    market_cap_bn = round(market_cap / 1e9, 2)
#    market_cap_list.append(market_cap_bn)

# ticker_info_df = pd.DataFrame({'Ticker': symbol_list, 'Company':name_list, 'Sector':sector_list, 'Market Cap (B)': market_cap_list})
# ticker_info_df.to_csv('ticker_info.csv', index=False)   

url = "https://raw.githubusercontent.com/justinjiajia/datafiles/refs/heads/main/ticker_info.csv"

ticker_info = load_to_df(url)
 
@st.cache_data(show_spinner=False)
def yf_download(symbol_list, start_date="2020-01-01", end_date=f"{date.today().year}-12-31"):
    return yf.download(symbol_list, start=start_date, end=end_date)


# Download OHLC data (Open, High, Low, Close, Volume, etc.)
stock_data = yf_download(symbol_list)


# This transformation converts stock data from a wide format (where each ticker is a column) into a long format (where each ticker's data is in separate rows).
long_stock_data = (stock_data.stack(level='Ticker')  # Stack the ticker level; stock_data has a MultiIndex (hierarchical index) where one of the levels is 'Ticker'. stack() pivots the specified level ('Ticker') from columns into rows, making the DataFrame longer (more rows, fewer columns).
             .reset_index()        # After stacking, the DataFrame has a new index structure. reset_index() converts all index levels into regular columns, making it easier to work with the data.
             .rename(columns={'level_1': 'Ticker'}))  # When stacking and resetting, the stacked column might get a default name like 'level_1'. This renames that column back to 'Ticker' for clarity.


# extract S&P 100 tickers from ticker_info
tickers_100 = ticker_info.Ticker.unique()

# set page title
st.title("S&P 100 Stock Dashboard 📊")  



# Sidebar controls
with st.sidebar:

    show_sector = st.checkbox("Show Market Cap by Sector", True)

    selected_tickers = st.multiselect(
        "Select Companies",
        options=tickers_100,
        default=['TSLA', 'NVDA', 'AAPL']
    )

    # Year range slider
    selected_years = st.slider(
        "Select Year Range",
        min_value=2020,
        max_value=2025,
        value=(2024, 2025)
    )

if show_sector:
    st.header("Market Cap by Sector")
    st.bar_chart(ticker_info, x="Sector", y="Market Cap (B)", color="Ticker", horizontal=True,
            width=720, height=500)

if selected_tickers:

    chart_data = long_stock_data.query(f"Date <= '{selected_years[1]}-12-31' and Date >= '{selected_years[0]}-01-01' and Ticker in {selected_tickers}")


    st.header(f"Stock Trend Analysis ({selected_years[0]} - {selected_years[1]})")
    
    # Closing Prices
    st.subheader("Closing Prices")
    st.line_chart(chart_data, x="Date", y="Close", color="Ticker",
                  width=720, height=500)

    
    # Volume Analysis
    st.subheader("Trading Volume")
    st.bar_chart(chart_data, x="Date", y="Volume", color="Ticker", 
                  width=720, height=500)

else:
    st.error("Please select at least one stock")
