import streamlit as st
import plotly.express as px
from vega_datasets import data

st.set_page_config(layout="centered")

st.markdown("Streamlit also provides ways for controlling how different elements are laid out on the screen.")



st.markdown("""Each page can feature a sidebar implemented by `st.sidebar`. 
Passing an element to `st.sidebar` positions it to the left of the main viewport, allowing users to focus on the content in our app.
            
<img src="https://docs.streamlit.io/images/api/sidebar.jpg" width=400/>
<br> <br>

We can organize page elements into a sidebar by
1) Calling methods directly on `st.sidebar`;
2) Wrapping element functions within `st.sidebar` using `with` notation.""", unsafe_allow_html=True)


code = """import streamlit as st
import plotly.express as px
from vega_datasets import data

source = data.stocks()

stock = st.sidebar.selectbox("Select a stock", 
                              source.symbol.unique())
year = st.sidebar.slider("Select a year", 2004, 2010)

query_str = f"date < {year + 1} and date >= {year} and symbol == '{stock}'"
chart_data = source.query(query_str)

st.markdown(f"### Prices for `{stock}` in {year}")
st.area_chart(chart_data, x="date", y="price")"""

st.markdown("#### :material/code_blocks: :blue[Source code to run]")

st.markdown("Call methods directly on `st.sidebar`:")

with st.container(border=True):
    st.code(code)


st.markdown("Use `with` notation:")
code = """import streamlit as st
import plotly.express as px
from vega_datasets import data

source = data.stocks()

with st.sidebar:
    stock = st.selectbox("Select a stock", 
                         source.symbol.unique())
    year = st.slider("Select a year", 2004, 2010)

query_str = f"date < {year + 1} and date >= {year} and symbol == '{stock}'"
chart_data = source.query(query_str)

st.markdown(f"### Prices for `{stock}` in {year}")
st.area_chart(chart_data, x="date", y="price")"""

with st.container(border=True):
    st.code(code)

st.markdown("#### :material/widgets: :red[Rendered output]")



source = data.stocks()

with st.container(border=True):
    stock = st.sidebar.selectbox("Select a stock", source.symbol.unique())
    year = st.sidebar.slider("Select a year", 2004, 2010)
    st.markdown(f"### Prices for `{stock}` in {year}<br>", unsafe_allow_html=True)
 
    chart_data = source.query(f"date < {year + 1} and date >= {year} and symbol == '{stock}'")
    st.area_chart(chart_data, x="date", y="price")