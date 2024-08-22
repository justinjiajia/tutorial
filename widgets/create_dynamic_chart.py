import streamlit as st

st.set_page_config(layout="wide")


with st.echo():
    import pandas as pd
    source = pd.read_csv("https://raw.githubusercontent.com/vega/vega-datasets/main/data/stocks.csv", 
                         parse_dates=['date'], date_format="%b %d %Y")



st.dataframe(source)

with st.container(border=True):
    stocks = st.multiselect("Select stocks for comparison", source.symbol.unique(), ['AMZN', 'AAPL'])
    
    all = st.checkbox("Show prices for the whole period")
    year = st.slider("Select a year", 2005, 2009, disabled=all)
    st.markdown(f"### Stock prices in {year}<br>", unsafe_allow_html=True)
    if not all:
        chart_data = source.query(f"date < {year + 1} and date >= {year} and symbol in {stocks}")
    else:
        chart_data = source.query(f"symbol in {stocks}")  
    st.line_chart(chart_data, x="date", y="price", color="symbol", width=600, height=500, use_container_width=False)

