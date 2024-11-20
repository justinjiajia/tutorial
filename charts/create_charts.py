import streamlit as st
import sys

sys.path.append('..')

from utils import load_to_df

st.set_page_config(layout="wide")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)


st.markdown("## 🎯 Charts for stock price comparison")
            
st.markdown("### :material/dataset: Data to use")


code = """
import pandas as pd

stocks = pd.read_csv("https://raw.githubusercontent.com/vega/vega-datasets/main/data/stocks.csv", 
                     parse_dates=['date'], date_format="%b %d %Y")
"""

st.code(code)
    
stocks = load_to_df("https://raw.githubusercontent.com/vega/vega-datasets/main/data/stocks.csv", 
                    parse_dates=['date'], date_format="%b %d %Y")

#with st.echo():
#    import pandas as pd
#    stock_returns = pd.read_csv('https://raw.githubusercontent.com/justinjiajia/datafiles/main/stocks_l.csv', 
#                         parse_dates=['date'], date_format="%Y-%m-%d")

st.dataframe(stocks)

st.divider()

st.markdown("""### :material/description:  Requirements

 
- Tips:
    - Recall how `st.line_chart()` allows us to align variables with desired aesthetics;
    - [`DataFrame.query()`](https://pandas.pydata.org/docs/user_guide/indexing.html#the-query-method) can be used to filter data for plotting, 
        - e.g., if your variable that holds the selected stocks is called `stocks` and that holds the specified year is called `year`, `.query(f"date < {year + 1} and date >= {year} and symbol in {stocks}")` will give you the desired subset.
""")

st.divider()

st.markdown("#### :material/ssid_chart: :red[Expected output]")

with st.container(border=True):
    
    st.markdown(f"### Stock prices")
    st.line_chart(stocks, x="date", y="price", color="symbol", 
                  width=800, height=500, use_container_width=False)
    

st.divider()

with st.container(border=True):

    symbols = ['IBM', 'AAPL', 'MSFT', 'AMZN']
    year = 2005
    chart_data = stocks.query(f"date < {year + 2} and date >= {year} and symbol in {symbols}")
    
    st.markdown(f"### Stock prices in {year}<br>", unsafe_allow_html=True)
    st.line_chart(chart_data, x="date", y="price", color="symbol", 
                    width=800, height=500, use_container_width=False)

