import streamlit as st
import pandas as pd
from datetime import datetime
 

st.set_page_config(page_title="Stock Dashboard", layout="wide")
st.markdown("""### :material/description:  Requirements
""")

st.divider()

st.markdown("#### :material/widgets: :red[Expected output]")

st.divider()


# Load stock data
# @st.cache_data(show_spinner="Downloading data...")
def load_data():
    return pd.read_csv("https://raw.githubusercontent.com/justinjiajia/datafiles/refs/heads/main/stocks_2000_2025.csv",
                        parse_dates=['date'], date_format="%b %d %Y")


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


# Load data
df = load_data()


data = df.query(f"date <= '{selected_years[1]}-12-31' and date >= '{selected_years[0]}-01-01' and symbol in {selected_tickers}")

if data.empty:
    st.warning("No data retrieved")
    st.stop()

# Main dashboard
if selected_tickers:
    st.header(f"Price Analysis ({selected_years[0]} - {selected_years[1]})")
    
    # Closing Prices
    st.subheader("Closing Prices")
    st.line_chart(data, x="date", y="price", color="symbol")
     
    
    # Volume Analysis
    st.subheader("Trading Volume")
    st.bar_chart(data, color='symbol', x='date', y='volume')
    
    
    
    # Raw data
    if st.checkbox("Show Raw Data"):
        st.dataframe(data.style.highlight_max(axis=0))
else:
    st.warning("Please select at least one company")

# Data download
st.sidebar.download_button(
    "Download Closing Prices",
    data=data.to_csv().encode('utf-8'),
    file_name='stock_prices.csv',
    mime='text/csv'
)