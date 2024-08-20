import streamlit as st

st.set_page_config(layout="centered")




st.markdown("""#### Display an image based on user input 
            
**Requirements**: 
            
- Use a text input widget to take an image's URL from the user.
            
- Click a button to submit the URL and load the image above.
""")


st.divider()



if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    # print("invoke the callback first")
    st.session_state.clicked = True
    st.session_state.url = st.session_state._url

if st.session_state.clicked:
    try:

        st.image(st.session_state.url)
    except:
        st.error("Cannot find the image!")    


url = st.text_input("Enter the URL of an image here", key="_url")
st.button('Submit', on_click=click_button)

