
import streamlit as st
import pandas as pd
from time import perf_counter

st.set_page_config(layout="wide")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)


st.markdown("""
Streamlit runs a script from top to bottom at every user interaction or code change. This execution model makes development super easy. 
But it comes with two major challenges:

- Long-running functions run again and again, which slows down your app.
  
- Objects get recreated again and again, which makes it hard to persist them across reruns or sessions.

The easiest way to circumvent these challenges and make a Streamlit app more performant is to opt for its ***caching*** mechanism, which stores some results in memory so that the app does not repeat the same work
whenever possible.

Streamlit provides two functions for this purpose:

- `st.cache_data` for data caching;
            
- `st.cache_resource` for caching resources like database connections or machine learning models.

""")
