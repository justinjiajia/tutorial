import streamlit as st

# idea: https://weekly-shopping-and-recipe-list.streamlit.app/

st.set_page_config(layout="centered")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)



st.markdown("""## Create a to-do list
            
### :material/description: Requirements
            
- 
""")


st.divider()

st.markdown("#### :material/widgets: :red[Expected output]")

if "adv_to_do_list" not in st.session_state:
    st.session_state["adv_to_do_list"] = []

with st.container(border=True):
    st.subheader("My To-do List")

    def add_item():
        if thing_to_add not in st.session_state.adv_to_do_list and thing_to_add is not None:  
            st.session_state.adv_to_do_list.append(thing_to_add)
        st.session_state.adv_to_do = None # empty the text field once the item is submitted

    def delete_item(thing):
        st.session_state.adv_to_do_list.remove(thing)

    if not st.session_state.adv_to_do_list:
        st.markdown(":rainbow[Hooray! My to-do list is empty!]")
    else:
        st.markdown(":blue[Things in my to-do list] (*clicking an item can remove it*):")    
        for thing in st.session_state.adv_to_do_list:
            st.button(thing, on_click=delete_item, args=[thing])

    thing_to_add = st.text_input("Things to add", key="adv_to_do")
    st.button("Add to list", on_click=add_item)



