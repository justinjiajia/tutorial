import streamlit as st
from PIL import Image

st.set_page_config(layout="centered")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)


st.markdown("### An improved chat UI")


if "msgs" not in st.session_state:
    st.session_state.msgs = []

chat_body = st.container(height=200)

def clear_history():
    st.session_state.msgs = []

with chat_body:
    for m in st.session_state.msgs:
        st.markdown(f"**To {m['user']}**: {m['content']}")

with st.form("send_msg"):
    _1, _2, _3 = st.columns([0.13, 0.74, 0.13])
    _1.selectbox("Choose user", ["👧", "👱‍♀️", "👨🏿", "👴"], key="user", label_visibility="collapsed")
    _2.text_input("Enter your message", key="msg", placeholder="hey, what's up?", 
                  label_visibility="collapsed")
    sent = _3.form_submit_button('Send')

st.button('Clear chat history', on_click=clear_history)

if sent:
    with chat_body:
      st.markdown(f"**To {st.session_state['user']}**: {st.session_state['msg']}")
    st.session_state.msgs.append({"user": st.session_state.user, "content": st.session_state.msg})

        

