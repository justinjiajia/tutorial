import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime
 

st.set_page_config(page_title="Stock Dashboard", layout="wide")
st.markdown("""### :material/description:  Requirements

Download the [starter code](https://raw.githubusercontent.com/justinjiajia/img/refs/heads/master/python/dashboard_template.py) and fill your code in the indicated place to create a simple stock performance dashboard using Streamlit.
 
""")

st.divider()

st.markdown("#### :material/widgets: :red[Expected output]")

st.divider()


# Load stock data
@st.cache_data
def load_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)
    return data

# Default settings
DEFAULT_TICKERS = ['AAPL', 'GOOG', 'MSFT', 'AMZN']
CURRENT_YEAR = datetime.today().year

# Configure page
st.title("Simple Stock Performance Dashboard 📊")

# Sidebar controls
st.sidebar.header("Controls")
selected_tickers = st.sidebar.multiselect(
    "Select Companies",
    options=DEFAULT_TICKERS,
    default=['AAPL']
)

# Year range slider
selected_years = st.sidebar.slider(
    "Select Year Range",
    min_value=2000,
    max_value=CURRENT_YEAR,
    value=(2020, CURRENT_YEAR)
)

# Convert years to datetime objects
start_date = datetime(selected_years[0], 1, 1)
end_date = datetime(selected_years[1], 12, 31)

# Load data
data = load_data(selected_tickers, start_date, end_date)
st.write(data)

# Main dashboard
if selected_tickers:
    st.header(f"Price Analysis ({selected_years[0]} - {selected_years[1]})")
    
    # Closing Prices
    st.subheader("Closing Prices")
    close_prices = data['Close'].copy()
    st.line_chart(close_prices)
    
    # Moving Averages
    if st.checkbox("Show Moving Averages"):
        ma_days = st.slider("MA Period (days)", 10, 200, 50)
        ma_prices = close_prices.rolling(ma_days).mean()
        st.line_chart(pd.concat([close_prices, ma_prices], axis=1))
    
    # Volume Analysis
    st.subheader("Trading Volume")
    volume_data = data['Volume'].copy()
    st.bar_chart(volume_data)
    
    # Statistics
    st.subheader("Key Statistics")
    col1, col2 = st.columns(2)
    
    
    with col1:
        annual_returns = close_prices.pct_change(365).iloc[-1].mean() * 100
        st.metric("Annual Return", 
                 f"{annual_returns.round(2)}%")
    
    with col2:
        volatility = close_prices.pct_change().std().mean() * 100
        st.metric("Volatility", 
                 f"{volatility.round(2)}%")
    
    # Raw data
    if st.checkbox("Show Raw Data"):
        st.dataframe(close_prices.style.highlight_max(axis=0))
else:
    st.warning("Please select at least one company")

# Data download
st.sidebar.download_button(
    "Download Closing Prices",
    data=close_prices.to_csv().encode('utf-8'),
    file_name='stock_prices.csv',
    mime='text/csv'
)