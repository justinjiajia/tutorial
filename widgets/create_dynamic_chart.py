import streamlit as st
from vega_datasets import data

st.set_page_config(layout="centered")



code ="""
from vega_datasets import data
source = data.stocks()
"""


st.code(code)

source = data.stocks()

st.dataframe(source)

source = data.stocks()

with st.container(border=True):
    stock = st.selectbox("Select a stock", source.symbol.unique())
    year = st.slider("Select a year", 2004, 2010)
    st.markdown(f"### Prices for `{stock}` in {year}<br>", unsafe_allow_html=True)
    chart_data = source.query(f"date < {year + 1} and date >= {year} and symbol == '{stock}'")
    st.area_chart(chart_data, x="date", y="price")