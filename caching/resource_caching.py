
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

The easiest way to make a Streamlit app more efficient is through its ***caching*** mechanism, which stores some results in memory so that the app does not repeat the same work
whenever possible.

A good analogy for an app's cache is a human's short-term memory, where we keep bits of information close at hand that we think might be useful.         
            
More specifically, Streamlit caching works by storing the results of a function in our app. If that function is called with the same parameters by another user (or by us if we rerun
the app), Streamlit does not run the same function but instead loads the result of the function from memory.
            
There are two Streamlit caching functions, one for data (`st.cache_data`) and one for resources
like database connections or machine learning models (`st.cache_resource`). 

""")
