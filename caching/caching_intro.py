
import streamlit as st
import pandas as pd
from time import perf_counter

st.set_page_config(layout="wide")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)


st.markdown("""
Streamlit runs your script from top to bottom at every user interaction or code change. This execution model makes development super easy. But it comes with two major challenges:

- Long-running functions run again and again, which slows down your app.
  
- Objects get recreated again and again, which makes it hard to persist them across reruns or sessions.

  
Streamlit lets you tackle both issues with its built-in caching mechanism.
            

Caching stores the results of slow function calls, so they only need to run once. This makes your app much faster and helps with persisting objects across reruns. 

""")
