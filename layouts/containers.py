import streamlit as st


st.set_page_config(layout="wide")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.markdown("""`st.container` allows us to inserts an invisible container into our app that can hold multiple elements.

<img src="https://docs.streamlit.io/images/api/container.jpg" width=400/>
<br> <br>""", unsafe_allow_html=True)
 



st.markdown("""Calling the `st.columns()` function returns a list of column objects.


To add elements to the returned container, we can use the `with` statement (preferred) or just call methods directly on the returned object..""")



st.markdown("#### :material/code_blocks: :blue[Source code to run]")

code = """with st.container():     
   st.write("This is inside the container")
   st.write(":dog:")

st.write("This is outside the container")"""

with st.container(border=True):
    st.code(code)

st.markdown("####  :material/monitor: :red[Rendered output]")


with st.container():     
   st.write("This is inside the container")
   st.write(":dog:")

st.write("This is outside the container")

st.divider()

st.markdown("By default, the container grows to fit its content and no border is shown.")


st.markdown("""When a fixed height is provided, a grey border is shown around the container and scrolling is also enabled for large content:""")

code = """container = st.container(height=150)
container.write("This is inside the container")
st.write("This is outside the container")
container.write(":dog:")"""

st.markdown("#### :material/code_blocks: :blue[Source code to run]")

with st.container(border=True):
    st.code(code)

st.markdown("####  :material/monitor: :red[Rendered output]")



container = st.container(height=150)

container.write("This is inside the container")
st.write("This is outside the container")
container.write(":dog:")

st.divider()

st.markdown("`st.container` can be used along with `st.columns` to make a grid of containers like the following:")


st.markdown("#### :material/code_blocks: :blue[Source code to run]")

code = """row1 = st.columns(4)
row2 = st.columns(4)

for col in row1 + row2:
    tile = col.container(height=60)
    tile.write(":dog:")
"""

with st.container(border=True):
    st.code(code)

st.markdown("####  :material/monitor: :red[Rendered output]")



row1 = st.columns(4)
row2 = st.columns(4)

for col in row1 + row2:
    tile = col.container(height=60)
    tile.write(":dog:")





