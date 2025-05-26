import streamlit as st

import yfinance as yf

ticker = yf.Ticker("AAPL")

st.write(ticker.info)