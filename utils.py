import pandas as pd
import streamlit as st

@st.cache_data(show_spinner=False)
def load_to_df(url, parse_dates=None, date_format=None):
    return pd.read_csv(url, parse_dates=parse_dates, date_format=date_format)