

import streamlit as st
import pandas as pd
from time import perf_counter

st.set_page_config(layout="wide")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)



code ="""
import streamlit as st
import pandas as pd
from time import perf_counter

url_1 = st.text_input("", "https://raw.githubusercontent.com/justinjiajia/datafiles/main/EcommercePurchases.csv",
                       label_visibility="collapsed", key="url_1")

if st.button("Show", key="btn_1"):
    start = perf_counter()
    st.write(pd.read_csv(url_1))
    end = perf_counter()
    st.write(f":red[It took {(end - start):.3f} seconds to load the data!]")
"""

st.markdown("#### :material/code_blocks: :blue[Source code to run]")

with st.container(border=True):
    st.code(code)

st.markdown("#### :material/widgets: :red[Expected output]")   

with st.container(border=True):
    url_1 =  st.text_input("url_1", "https://raw.githubusercontent.com/justinjiajia/datafiles/main/EcommercePurchases.csv",
                        label_visibility="collapsed", key="url_1")

    if st.button("Show", key="btn_1"):
        start = perf_counter()
        st.write(pd.read_csv(url_1))
        end = perf_counter()
        st.write(f":red[It took {(end - start):.3f} seconds to load the data!]")


st.divider()


st.markdown("## :material/list_alt: [`@st.cache_data`](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_data)")

st.markdown(
"""<br/>

To avoid repeated data computation across reruns, we can simply modularize relevant steps into a separate function
and decorate it with the `@st.cache_data` decorator, telling Streamlit to store the function's return value in a cache.

As a result, subsequent calls to the function will skip function execution and return a copy of the cached value, thereby getting rid of redundant computations and improving overall performance.
""", unsafe_allow_html=True)

code ="""
import streamlit as st
import pandas as pd
from time import perf_counter

@st.cache_data(show_spinner="Loading data ...")
def load_data(url):
    return pd.read_csv(url)

url_2 = st.text_input("", "https://raw.githubusercontent.com/justinjiajia/datafiles/main/EcommercePurchases.csv",
                       label_visibility="collapsed", key="url_2")

if st.button("Show", key="btn_2"):
    start = perf_counter()
    st.write(load_data(url_2))
    end = perf_counter()
    st.write(f":red[It took {(end - start):.3f} seconds to load the data!]")
"""

st.markdown("#### :material/code_blocks: :blue[Source code to run]")

with st.container(border=True):
    st.code(code)

st.markdown("#### :material/widgets: :red[Expected output]")

@st.cache_data(show_spinner="Loading data ...")
def load_data(url):
    return pd.read_csv(url)

with st.container(border=True):
    url_2 =  st.text_input("url_2", "https://raw.githubusercontent.com/justinjiajia/datafiles/main/EcommercePurchases.csv",
                        label_visibility="collapsed")

    if st.button("Show", key="btn_2"):
        start = perf_counter()
        st.write(load_data(url_2))
        end = perf_counter()
        st.write(f":red[It took {(end - start):.3f} seconds to load the data!]")


st.write("Try a different URL: ")

st.code("https://raw.githubusercontent.com/justinjiajia/datafiles/main/price.csv")


st.info("Cached values will be updated automatically as the function code changes, ensuring that the latest changes are reflected in the cache.")



st.divider()


st.info("Cached values are available to all users of your app. If you need to save results that should only be accessible within a session, use Session State instead.")


    

st.markdown
("""
You can clear a function's cache with `func.clear()` or clear the entire cache with `st.cache_data.clear()`.
""")