import streamlit as st

import sys

sys.path.append('..')

from utils import load_to_df

st.set_page_config(layout="wide")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)


st.markdown("## 🎯 Dynamic charting for stock price comparison")
            
st.markdown("### :material/dataset: Data to use")

code = """
import pandas as pd

stocks = pd.read_csv(
    "https://raw.githubusercontent.com/vega/vega-datasets/main/data/stocks.csv", 
    parse_dates=['date'], date_format="%b %d %Y"
    ).query(f"date < 2010 and date >= 2005")

symbols = ['AAPL', 'AMZN', 'GOOG', 'IBM', 'MSFT']
"""

st.code(code)

stocks = load_to_df(
    "https://raw.githubusercontent.com/vega/vega-datasets/main/data/stocks.csv", 
    parse_dates=['date'], date_format="%b %d %Y"
    ).query(f"date < 2010 and date >= 2005")

st.dataframe(stocks)

st.divider()

st.markdown("""### :material/description:  Requirements

- Add a multiselect widget (`st.multiselect()`) to choose which stocks to include in the plot.  
 
- Add a slider widget (`st.slider()`) to select a specific year for comparison.

- Add a checkbox widget (`st.checkbox()`) to compare stocks over the entire period. When checked, the slider widget should be disabled.

- If no stocks are selected, use `st.error()` to display the error message: `"Please select at least one stock!"`
            
#### Tips:

- Chart aesthetics: Use `st.line_chart()` to map your variables to specific visual aesthetics.

- Data filtering: Use [`DataFrame.query()`](https://pandas.pydata.org/docs/user_guide/indexing.html#the-query-method) to filter data before plotting. For example, if your selected stocks are stored in symbols and the chosen year is in year, this query will return the correct subset:
`.query(f"date < {year + 1} and date >= {year} and symbol in {symbols}")`

- Disabling widgets: Use the [`disabled`](https://docs.streamlit.io/develop/api-reference/widgets/st.slider) parameter of `st.slider()` to control when the slider is inactive (e.g., tie it to the state of your checkbox).

""")

st.divider()

st.markdown("#### :material/widgets: :red[Expected output]")

with st.container(border=True):
    symbols = st.multiselect("Select stocks for comparison", stocks.symbol.unique(), ['AMZN', 'AAPL'])
    all_years = st.checkbox("Show prices for the whole period")
    year = st.slider("Select a year", 2005, 2009, disabled=all_years)
 
    if not all_years:
        chart_data = stocks.query(f"date < {year + 1} and date >= {year} and symbol in {symbols}")
    else:
        chart_data = stocks.query(f"symbol in {symbols}")  
        year = "2005-2009"
    if not symbols:
        st.error("Please select at least one stock!")
    else:
        st.markdown(f"### Stock prices in {year}<br>", unsafe_allow_html=True)
        st.line_chart(chart_data, x="date", y="price", color="symbol", 
                      width=720, height=500, use_container_width=False)

