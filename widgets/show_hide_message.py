import streamlit as st

 
with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
    
st.markdown("""## Show/hide messages
            
### :material/description:  Requirements
            
- 
""")

if 'show_1' not in st.session_state:
    st.session_state.show_1 = False

def show_1():
    st.session_state.show_1 = True

def hide_1():
    st.session_state.show_1 = False  

if st.session_state.show_1:
    try:
        st.write(f"**Message:** {st.session_state.txt_1}")
    except: st.error("error")        

st.text_input("Enter your message", key="txt_1")

if not st.session_state.show_1:
    st.button('Show message', on_click=show_1)
else:    
    st.button('Hide message', on_click=hide_1)

st.divider()

if 'show_2' not in st.session_state:
    st.session_state.show_2 = False

def show_2():
    st.session_state.show_2 = True

def hide_2():
    st.session_state.show_2 = False  

def update_value():
    st.session_state.txt_2 = st.session_state._txt_2

def load_value():
    st.session_state._txt_2 = st.session_state.txt_2

if "txt_2" in st.session_state:
    load_value()

if st.session_state.show_2:
    st.write(f"**Message:** {st.session_state._txt_2}")

st.text_input("Enter your message", key="_txt_2", on_change=update_value)

if not st.session_state.show_2:
    st.button('Show message', key="show_msg_2", on_click=show_2)
else:    
    st.button('Hide message', key="hide_msg_2", on_click=hide_2)


st.code("""
import streamlit as st

def store_value(key):
    st.session_state[key] = st.session_state["_"+key]
def load_value(key):
    st.session_state["_"+key] = st.session_state[key]

load_value("my_key")
st.number_input("Number of filters", key="_my_key", 
                on_change=store_value, args=["my_key"])
""")    

st.markdown("https://docs.streamlit.io/develop/concepts/architecture/widget-behavior")