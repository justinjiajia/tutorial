import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.markdown("""Streamlit `columns` are containers laid out as side-by-side columns.

<img src="https://docs.streamlit.io/images/api/columns.jpg" width=400/>
<br> <br>""", unsafe_allow_html=True)
 



st.markdown("""Calling the `st.columns()` function returns a list of column objects.


To add elements to the returned container, we can use the `with` statement (preferred) or just call methods directly on the returned object..""")



st.markdown("#### :material/code_blocks: :blue[Source code to run]")

code = """col1, col2, col3 = st.columns(3)

# use with notation:
with col1:
   st.header("A cat")
   st.image("static/cat.jpg")

with col2:
   st.header("A dog")
   st.image("static/dog.jpg")

with col3:
   st.header("An owl")
   st.image("static/owl.jpg")"""

with st.container(border=True):
    st.code(code)

st.markdown("#### :red[Rendered output]")

 
col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   # the pathname is relative to the folder we're running Streamlit from
   st.image("static/cat.jpg")

with col2:
   st.header("A dog")
   st.image("static/dog.jpg")

with col3:
   st.header("An owl")
   st.image("static/owl.jpg")

st.divider()

code = """col1, col2 = st.columns([0.7, 0.3])

# call methods directly on a column object
col1.header("A cat")
col1.image("static/cat.jpg")

col2.header("A dog")
col2.image("static/dog.jpg")"""

st.markdown("#### :material/code_blocks: :blue[Source code to run]")

with st.container(border=True):
    st.code(code)

st.markdown("#### :red[Rendered output]")


col1, col2 = st.columns([0.7, 0.3])

col1.header("A cat")
col1.image("static/cat.jpg")

col2.header("A dog")
col2.image("static/dog.jpg")

st.divider()

st.markdown("""The `vertical_alignment` argument of `st.columns` allows us to customize how to align contents of side-by-side columns:""")



v_align = st.selectbox("Customize vertical alignment",
                       ["top", "center", "bottom"])

st.markdown("#### :material/code_blocks: :blue[Source code to run]")

code = f"""left, middle, right = st.columns(3, vertical_alignment="{v_align}")
left.image("static/cat.jpg")
middle.image("static/dog.jpg")
right.image("static/owl.jpg")
"""
with st.container(border=True):
   st.code(code)

st.markdown("#### :red[Rendered output]")

with st.container(border=True):
   left, middle, right = st.columns(3, vertical_alignment=v_align)
   left.image("static/cat.jpg")
   middle.image("static/dog.jpg")
   right.image("static/owl.jpg")