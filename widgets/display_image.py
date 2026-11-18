import streamlit as st

st.set_page_config(layout="centered")


with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.markdown("""## 🎯 Display an image based on user input 
            
### :material/description:  Requirements
            
- Create a text input widget that allows the user to enter an image URL, e.g., `https://upload.wikimedia.org/wikipedia/en/a/a6/Pok%C3%A9mon_Pikachu_art.png`.
- Add a "Submit" button.
- When the button is clicked, display the image above the text input widget.
- If the URL is invalid or the image cannot be loaded, display an error message instead.

#### Tips

- Rendering order: Streamlit renders top-to-bottom. To show the image above the input, place the image logic (the `if` block) before `st.text_input`.

- Callbacks: Pass a function to the `on_click` argument to update `st.session_state` before the script reruns.

- Accessing widget values: To read a widget's value inside a callback, give it a key and access it via `st.session_state (e.g., st.session_state._url)`.

- Error handling: Wrap `st.image()` in a `try...except` block to catch invalid URLs and display a custom [`st.error()`](https://docs.streamlit.io/develop/api-reference/status/st.error) instead of crashing.

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
        st.image(st.session_state.url, width=200)
    except:
        st.error("Cannot find the image!")    


url = st.text_input("Enter the URL of an image", 
                    "https://upload.wikimedia.org/wikipedia/en/a/a6/Pok%C3%A9mon_Pikachu_art.png",
                    key="_url")
st.button('Submit', on_click=click_button)

