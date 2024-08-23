import streamlit as st

st.set_page_config(layout="wide")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)


st.markdown("""Recall: Streamlit reruns the script from top to bottom upon user input. 
            
Each reruns takes place in a blank slate (with a fresh namespace). So, variables do not live beyond a single run and cannot be shared between runs.

The following example helps you see this.
            
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
Then, how can we share information across reruns of a Streamlit app? This is where [`st.session_state`](https://docs.streamlit.io/develop/concepts/architecture/session-state) comes to the rescue.
            
As you may know, a session in the context of Web development refers to a way of maintaining state information about a user's interactions with a website or web application.

In Streamlit, a session is simply a connection to the backend server in a browser tab. Its state endures and can also be updated across reruns. 
            
Streamlit allows us to access a session's state through a global dictionary, called ***Session State***, which persists through a user's session and is exposed by `st.session_state`, providing a way to share data between reruns.""")

code = """try:
    st.write(f"The value of the state item `'contact'`: `{st.session_state.contact}`")
except:
    st.error("`'contact'` does not exist in `st.session_state` before the initial rendering of the selectbox widget.")

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
Session State also persists across pages of a multi-page app as long as those pages are loaded within the same connection.""") 


code = """try: 
    st.write(f"`{st.session_state.state_item}`")
except:
    st.error("`'state_item'` does not exist in `st.session_state`.")
    
st.session_state.state_item = "initialized"
"""

st.markdown("#### :material/code_blocks: :blue[Source code to run]")


with st.container(border=True):
    st.code(code)

st.markdown("#### :material/monitor: :red[Rendered output]")


with st.container(border=True):
    try: 
        st.write(f"`{st.session_state.state_item}`")
    except:
        st.error("`'state_item'` does not exist in `st.session_state`.")

    st.session_state.state_item = "initialized"

st.page_link("sessions/check_state_item.py", label="Click to see if `state_item` can be accessed from a different page.", icon="🖱️")
st.markdown("""Note that refreshing a page will terminate the previous connection and establish a new one, resulting in a new session with a fresh state.
""")    

st.divider()

st.markdown("""
When we want some data items to persist and potentially  mutate throughout a user session, remember to add them to Session State.
This requires some initialization steps to be executed when the app script runs for the first time.

There are two ways to initialize a state item in Session State:

- First, it can be initialized through the first rendering of a widget associated with the key;

- Second, we can manually assign an initial value to the key using a direct assignment.
""")

code = """
# this guard condition is necessary
# otherwise, the state item resets every time the script reruns
if "bucket_list" not in st.session_state:
    st.session_state["bucket_list"] = []
    
st.subheader("My Bucket List:")

dest = st.text_input("Where do you want to travel?")
clicked = st.button("Add to list")

if clicked:
    st.session_state.bucket_list.append(dest.capitalize())

st.write(st.session_state["bucket_list"] )
"""

st.markdown("#### :material/code_blocks: :blue[Source code to run]")


with st.container(border=True):
    st.code(code)

st.markdown("#### :material/widgets: :red[Rendered output]")

with st.container(border=True):
 
    if "bucket_list" not in st.session_state:
        st.session_state["bucket_list"] = []
    
    st.subheader("My Bucket List:")

    dest = st.text_input("Where do you want to travel?")
    clicked = st.button("Add to list")

    if clicked:
        st.session_state.bucket_list.append(dest.title())
        
    
    st.write(st.session_state["bucket_list"] )

