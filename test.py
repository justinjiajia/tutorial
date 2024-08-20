import streamlit as st

if 'visible' not in st.session_state:
    st.session_state.visible = False

def submit_to_show():
    st.session_state.visible = True

def submit_to_hide():
    st.session_state.visible = False  

if st.session_state.visible:
    st.write(f"**Message:** {st.session_state.txt}")

st.text_input("Enter your message", "hey, what's up?", 
              key="txt")

if not st.session_state.visible:
    st.button('Show message', on_click=submit_to_show)
else:    
    st.button('Hide message', on_click=submit_to_hide)

