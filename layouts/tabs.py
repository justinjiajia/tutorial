import streamlit as st

## may need to handle widget clean up process

st.set_page_config(layout="wide")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
    
st.markdown("""`st.container` allows us to inserts an invisible container into our app that can hold multiple elements.

<img src="https://docs.streamlit.io/images/api/tabs.jpg" width=400/>
<br> <br>""", unsafe_allow_html=True)
 



st.markdown("""Calling the `st.columns()` function returns a list of column objects.


To add elements to the returned container, we can use the `with` statement (preferred) or just call methods directly on the returned object..""")



st.markdown("#### :material/code_blocks: :blue[Source code to run]")

code = """ tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])    
with tab1:
    st.header("A cat")
    st.image("static/cat.jpg", width=200)

with tab2:
    st.header("A dog")
    st.image("static/dog.jpg", width=200)

with tab3:
    st.header("An owl")
    st.image("static/owl.jpg", width=200)"""

with st.container(border=True):
    st.code(code)

st.markdown("#### :red[Rendered output]")
 

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with st.container(border=True):
    with tab1:
        st.header("A cat")
        st.image("static/cat.jpg", width=200)

    with tab2:
        st.header("A dog")
        st.image("static/dog.jpg", width=200)

    with tab3:
        st.header("An owl")
        st.image("static/owl.jpg", width=200)




