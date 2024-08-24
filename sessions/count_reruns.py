import streamlit as st

st.set_page_config(layout="centered")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

code = """
if "count_reruns" not in st.session_state:
    st.session_state.count_reruns = 0

st.session_state.count_reruns += 1   

st.write(f"No. of runs: {st.session_state.count_reruns}")

st.text_input("Entuer your username")

st.toggle("Activate feature")

st.selectbox("How would you like to be contacted?", 
             ("Email", "Home phone", "Mobile phone"))
"""

st.markdown("#### :material/code_blocks: :blue[Source code to run]")

with st.container(border=True):
    st.code(code)

st.markdown("#### :material/widgets: :red[Rendered output]")  

if "count_reruns" not in st.session_state:
    st.session_state.count_reruns = 0

with st.container(border=True):


    st.session_state.count_reruns += 1   

    st.write(f"No. of runs: {st.session_state.count_reruns}")

    st.text_input("Entuer your username")

    st.toggle("Activate feature")

    st.selectbox("How would you like to be contacted?",
                ("Email", "Home phone", "Mobile phone"))

    st.button("Rerun")

