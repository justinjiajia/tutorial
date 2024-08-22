import streamlit as st

code = """st.write(f"`{st.session_state.state_item}`")
"""

st.markdown("#### :material/code_blocks: :blue[Source code to run]")


with st.container(border=True):
    st.code(code)

st.markdown("#### :material/widgets: :red[Rendered output]")

# to make sure sessions.py is always loaded before this script
if "state_item" not in st.session_state:
    st.switch_page("sessions/sessions.py")

with st.container(border=True):

    st.write(f"`{st.session_state.state_item}`")
