import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")




st.markdown("""Recall: Streamlit reruns the script every time we interact with an app. 
            
Each reruns takes place in a blank slate (with a fresh namespace). So, variables do not live beyond a single run and cannot be shared between runs.

            https://docs.streamlit.io/develop/concepts/architecture/session-state
""")


code = """st.write(f"Check if variable `contact` exists: `{'contact' in locals()}`")

contact = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

st.write(f"Check if variable `contact` exists: `{'contact' in locals()}`")"""

st.markdown("#### :material/code_blocks: :blue[Source code to run]")


with st.container(border=True):
    st.code(code)

st.markdown("#### :material/widgets: :red[Rendered output]")

with st.container(border=True):
    st.write(f"Check if variable `contact` exists: `{'contact' in locals()}`")

    contact = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone")
    )

    st.write(f"Check if variable `contact` exists: `{'contact' in locals()}`")


st.divider()

st.markdown("""
Broadly speaking, a session in the context of web development refers to a way of maintaining state information about a user's interactions with a website or web application

In Streamlit, a session is simply a connection to the backend server in a browser tab. Its state endures and can change across reruns. 
            
Streamlit allows us to access a session's state through the `st.session_state` API, providing a way to share data between reruns.""")

code = """try:
    st.write(f"The value of the state item `'contact'`: `{st.session_state.contact}`")
except:
    st.error("`'contact'` does not exist in `st.session_state` before the initial load of the selectbox widget.")

st.selectbox("How would you like to be contacted?",
             ("Email", "Home phone", "Mobile phone"), key="contact")

st.write(f"The value of the state item `'contact'`: `{st.session_state.contact}`")"""

st.markdown("#### :material/code_blocks: :blue[Source code to run]")


with st.container(border=True):
    st.code(code)

st.markdown("#### :material/widgets: :red[Rendered output]")

with st.container(border=True):
    try:
        st.write(f"The value of the state item `'contact'`: `{st.session_state.contact}`")
    except:
        st.error("`'contact'` does not exist in `st.session_state` before the initial load of the selectbox widget.")

    contact = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"), key="contact"
    )

    st.write(f"The value of the state item `'contact'`: `{st.session_state.contact}`")

st.divider()

st.markdown("""
Session state also persists across pages of a multi-page app as long as those pages are loaded within the same connection.""") 


code = """try: 
    st.write(f"`{st.session_state.state_item}`")
except:
    st.error("`'state_item'` does not exist in `st.session_state`.")
st.session_state.state_item = "initialized"
"""

st.markdown("#### :material/code_blocks: :blue[Source code to run]")


with st.container(border=True):
    st.code(code)

st.markdown("#### :material/widgets: :red[Rendered output]")


with st.container(border=True):
    try: 
        st.write(f"`{st.session_state.state_item}`")
    except:
        st.error("`'state_item'` does not exist in `st.session_state`.")
    st.session_state.state_item = "initialized"

st.page_link("sessions/check_state_item.py", label="Click to see if `state_item` can be accessed from a different page.", icon="🖱️")
st.markdown("""Note that refreshing a page will terminate the previous connection and establish a new one, resulting in a new session with a fresh state.
""")    

 