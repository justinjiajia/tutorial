import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime, date
import sys

sys.path.append('..')

from utils import load_to_df

st.set_page_config(page_title="Stock Dashboard", layout="wide")

# ticker = yf.Ticker("AAPL")

# ticker.info.get('longName')
# ticker.info.get('sector')
# ticker.info.get('marketCap')

# ticker_list = ['AAPL', 'ABBV', 'ABT', 'ACN', 'ADBE', 'AIG', 'AMD', 'AMGN', 'AMT', 'AMZN', 'AVGO', 'AXP', 
#               'BA', 'BAC', 'BK', 'BKNG', 'BLK', 'BMY', 'BRK-B',
#               'C', 'CAT', 'CHTR', 'CL', 'CMCSA', 'COF', 'COP', 'COST', 'CRM', 'CSCO', 'CVS', 'CVX', 
#               'DE', 'DHR', 'DIS', 'DUK', 'EMR', 'FDX', 'GD', 'GE', 'GILD', 'GM', 'GOOG', 'GOOGL', 'GS',
#               'HD', 'HON', 'IBM', 'INTC', 'INTU', 'ISRG', 'JNJ', 'JPM', 'KO', 
#               'LIN', 'LLY', 'LMT', 'LOW', 'MA', 'MCD', 'MDLZ', 'MDT', 'MET', 'META', 'MMM', 'MO', 'MRK', 'MS', 'MSFT',
#               'NEE', 'NFLX', 'NKE', 'NOW', 'NVDA', 'ORCL', 'PEP', 'PFE', 'PG', 'PLTR', 'PM', 'PYPL', 
#               'QCOM', 'RTX', 'SBUX', 'SCHW', 'SO', 'SPG', 'T', 'TGT', 'TMO', 'TMUS', 'TSLA', 'TXN',
#               'UNH', 'UNP', 'UPS', 'USB', 'V', 'VZ', 'WFC', 'WMT', 'XOM']


# name_list = []
# sector_list = []
# market_cap_list = []
 
# for ticker in ticker_list:
#    stock = yf.Ticker(ticker)
#    info = stock.info

#    name_list.append(info.get('longName'))
#    sector_list.append(info.get('sector'))
#    market_cap = info.get('marketCap')
#    market_cap_bn = round(market_cap / 1e9, 2)
#    market_cap_list.append(market_cap_bn)

# ticker_info_df = pd.DataFrame({'Ticker': ticker_list, 'Company':name_list, 'Sector':sector_list, 'Market Cap (B)': market_cap_list})
# ticker_info_df.to_csv('ticker_info.csv', index=False)   




st.markdown("### :material/dataset: Data & variables to use")


code = """
import pandas as pd
import yfinance as yf
from datetime import date

ticker_info = pd.read_csv("https://raw.githubusercontent.com/justinjiajia/datafiles/refs/heads/main/ticker_info.csv")

# extract S&P 100 tickers from ticker_info
ticker_list = list(ticker_info.Ticker.unique())

start_date="2020-01-01"
end_date = f"{date.today().year}-12-31"  

stock_data = yf.download(ticker_list, start=start_date, end=end_date).stack(level='Ticker') \\
               .reset_index().rename(columns={'level_1': 'Ticker'})
"""

st.code(code)
    



url = "https://raw.githubusercontent.com/justinjiajia/datafiles/refs/heads/main/ticker_info.csv"

ticker_info = load_to_df(url)
st.write(ticker_info)

 
@st.cache_data(show_spinner=False)
def yf_download(symbol_list, start_date="2020-01-01", end_date=f"{date.today().year}-12-31"):
    # This transformation converts stock data from a wide format (where each ticker is a column) into a long format 
    # (where each ticker's data is in separate rows).
    return yf.download(symbol_list, start=start_date, end=end_date).stack(level='Ticker').reset_index().rename(columns={'level_1': 'Ticker'})


ticker_list = list(ticker_info.Ticker.unique())


stock_data = yf_download(ticker_list)

st.write(stock_data)



"---"

 


st.markdown("""### :material/description:  Requirements

            
- Include a sidebar that contains the following widgets:
    
    - A checkbox widget (`st.checkbox()`) that alows the user to toggle the visibility of a bar chart visualizing the market caps of S&P 100 stocks by sector. This checkbox is checked by default.
            
    - A multiselect widget (`st.multiselect()`) for users to choose from `ticker_list` which stocks should be included for plotting. The default selections are `'TSLA'`, `'NVDA'`, and `'AAPL'`.
    
    - A slider widget (`st.slider()`) for users to select the year range for stock comparison, ranging from 2020 to 2025. The default range is 2024 to 2025.

            
        - If no stocks are selected, display an error message `"Please select at least one stock!"` using `st.error()`; 

        - If stocks are selected, plot their closing prices (the column `'Close'`) with a line chart and their volumes (the column '`Volume`') with a bar chart.
 
            
- Tips:

    - Use [`DataFrame.query()`](https://pandas.pydata.org/docs/user_guide/indexing.html#the-query-method) to filter data for plotting. For example, if `selected_tickers` holds the chosen stocks and `selected_years` holds the year range, use `.query(f"Date <= '{selected_years[1]}-12-31' and Date >= '{selected_years[0]}-01-01' and Ticker in {selected_tickers}")` to get the filtered data.
""")          

st.divider()

st.markdown("#### :material/widgets: :red[Expected output]")

# set page title
st.title("S&P 100 Stock Dashboard 📊")  



# Sidebar controls
with st.sidebar:

    show_sector = st.checkbox("Show Market Cap by Sector", True)

    selected_tickers = st.multiselect(
        "Select Companies",
        options=ticker_list,
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

    chart_data = stock_data.query(f"Date <= '{selected_years[1]}-12-31' and Date >= '{selected_years[0]}-01-01' and Ticker in {selected_tickers}")


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
    st.error("Please select at least one stock") # st.warning("Please select at least one stock!")
