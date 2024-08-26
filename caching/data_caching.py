import streamlit as st
from time import perf_counter

import pandas as pd

st.set_page_config(layout="wide")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)


code ="""
import streamlit as st
import pandas as pd
from time import perf_counter

url_1 = st.text_input("url_1", "https://raw.githubusercontent.com/vega/vega-datasets/main/data/flights-3m.csv",
                      label_visibility="collapsed", key="url_1")

if st.button("Show", key="btn_1"):
    start = perf_counter()
    data = load_data(url_1)
    st.write(data)
    end = perf_counter()
    st.write(f":red[It took {(end - start):.3f} seconds to load the data!]")
"""

st.markdown("#### :material/code_blocks: :blue[Source code to run]")

with st.container(border=True):
    st.code(code)

st.markdown("#### :material/widgets: :red[Rendered output]")

with st.container(border=True):
    url_1 =  st.text_input("url_1", "https://raw.githubusercontent.com/vega/vega-datasets/main/data/flights-3m.csv",
                        label_visibility="collapsed", key="url_1")

    if st.button("Show", key="btn_1"):
        start = perf_counter()
        st.write(pd.read_csv(url_1))
        end = perf_counter()
        st.write(f":red[It took {(end - start):.3f} seconds to load the data!]")


st.divider()


st.markdown("### :material/list_alt: [`@st.cache_data`](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_data)")

st.markdown(
"""<br/>

To prevent redudant data computations across reruns, we can simply modularize relevant steps into a separate function
and decorate it with `@st.cache_data` (i.e., simply add the decorator on top of the `def` statement).

It tells Streamlit to associate this function with a cache and store the function's return value in it for each unique set of inputs.

Conceptually, the cache acts like *an associative table*, mapping inputs to their corresponding outputs.

On subsequent calls, if the inputs match a cached entry, Streamlit skips executing the function and get us a copy of the cached value,
regardless of whether the calls originate from reruns or different user sessions.

""", unsafe_allow_html=True)

code ="""
import streamlit as st
import pandas as pd
from time import perf_counter

@st.cache_data(show_spinner="Loading data ...")
def load_data(url):
    return pd.read_csv(url)

url_2 = st.text_input("url_2", "https://raw.githubusercontent.com/vega/vega-datasets/main/data/flights-3m.csv",
                      label_visibility="collapsed", key="url_2")

if st.button("Show", key="btn_2"):
    start = perf_counter()
    data = load_data(url_2)
    st.write(data)
    end = perf_counter()
    st.write(f":red[It took {(end - start):.3f} seconds to load the data!]")
"""

st.markdown("#### :material/code_blocks: :blue[Source code to run]")

with st.container(border=True):
    st.code(code)

st.markdown("#### :material/widgets: :red[Rendered output]")

@st.cache_data(show_spinner="Loading data ...")
def load_data(url):
    return pd.read_csv(url)

with st.container(border=True):
    url_2 =  st.text_input("url_2", "https://raw.githubusercontent.com/vega/vega-datasets/main/data/flights-3m.csv",
                        label_visibility="collapsed")

    if st.button("Show", key="btn_2"):
        start = perf_counter()
        st.write(load_data(url_2))
        end = perf_counter()
        st.write(f":red[It took {(end - start):.3f} seconds to load the data!]")


st.write("Try a different URL: ")

st.code("https://raw.githubusercontent.com/plotly/datasets/master/data.csv", language="markup")


st.info("Cached values will be updated automatically as the function code changes, ensuring that the latest changes are reflected in the cache.",
        icon="💡")



st.divider()




st.markdown("""
Cached values persist across user sessions and are available to all users of a Streamlit app. 
""")


st.info("To save results that should only be accessible within a session, use Session State instead.",
        icon="💡")

st.markdown("""
We can clear a function's cache with `func.clear()` or clear the entire cache with `st.cache_data.clear()`.
""")

st.markdown("#### :material/code_blocks: :blue[Source code to run]")

code = """
if st.button("Clear cache"): 
    load_data.clear()
    st.write("The cache associated with `load_data()` is cleared!")
"""


with st.container(border=True):
    st.code(code)

st.markdown("#### :material/widgets: :red[Rendered output]")

with st.container(border=True):
    if st.button("Clear cache"): 
        load_data.clear()
        st.write("The cache associated with `load_data()` is cleared!")
 



