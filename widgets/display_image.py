import streamlit as st

st.set_page_config(layout="centered")


with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.markdown("""## Display an image based on user input 
            
### :material/description:  Requirements
            
- Use a text input widget to take an image's URL from the user.
            
- Click a button to submit the URL and display the image above the widget.
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


url = st.text_input("Enter the URL of an image:", 
                    "https://hkust.edu.hk/sites/default/files/styles/news_image_single/public/2023-06/HKUST Piazza_0.jpg",
                    key="_url")
st.button('Submit', on_click=click_button)

