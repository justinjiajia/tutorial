import streamlit as st
import pandas as pd
from datetime import datetime
import sys

sys.path.append('..')

from utils import load_to_df

st.set_page_config(page_title="Stock Dashboard", layout="wide")


with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)



st.markdown("### :material/dataset: Data & variables to use")


code = """
import pandas as pd

stocks_df = pd.read_csv("https://raw.githubusercontent.com/justinjiajia/datafiles/refs/heads/main/stocks_2000_2025.csv", 
                     parse_dates=['date'], date_format="%b %d %Y")

# Default settings
DEFAULT_TICKERS = ['AAPL', 'GOOG', 'MSFT', 'AMZN']
CURRENT_YEAR = 2025  
"""

st.code(code)
    
stocks_df = load_to_df("https://raw.githubusercontent.com/justinjiajia/datafiles/refs/heads/main/stocks_2000_2025.csv", 
                    parse_dates=['date'], date_format="%b %d %Y")


st.dataframe(stocks_df)

st.markdown("""### :material/description:  Requirements

            
- Include a sidebar that contains the following widgets:
            
    - A multiselect widget (`st.multiselect()`) for users to choose from `DEFAULT_TICKERS` which stocks should be included for plotting. The default selection is `'AAPL'`.
    
    - A slider widget (`st.slider()`) for users to select the year range for stock comparison, ranging from 2000 to 2025. The default range is 2020 to 2025.

- If no stocks are selected, display an error message `"Please select at least one stock!"` using `st.warning()`; 

- If stocks are selected, plot their closing prices (the column `'price'`) with a line chart and their volumes (the column '`volume`') with a bar chart.
 
            
- Tips:

    - Use [`DataFrame.query()`](https://pandas.pydata.org/docs/user_guide/indexing.html#the-query-method) to filter data for plotting. For example, if `selected_tickers` holds the chosen stocks and `selected_years` holds the year range, use `.query(f"date <= '{selected_years[1]}-12-31' and date >= '{selected_years[0]}-01-01' and symbol in {selected_tickers}")` to get the filtered data.
""")          

st.divider()

st.markdown("#### :material/widgets: :red[Expected output]")

st.divider() 

# Default settings
DEFAULT_TICKERS = ['AAPL', 'GOOG', 'MSFT', 'AMZN']
CURRENT_YEAR = 2025 # datetime.today().year


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



data = stocks_df.query(f"date <= '{selected_years[1]}-12-31' and date >= '{selected_years[0]}-01-01' and symbol in {selected_tickers}")

#if data.empty:
#    st.warning("No data retrieved")
#    st.stop()

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
    
    #if st.checkbox("Show Raw Data"):
    #    st.dataframe(data.style.highlight_max(axis=0))
else:
    st.warning("Please select at least one stock!")

# Data download
#st.sidebar.download_button(
#    "Download Closing Prices",
#    data=data.to_csv().encode('utf-8'),
#    file_name='stock_prices.csv',
#    mime='text/csv'
#)