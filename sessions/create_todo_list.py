import streamlit as st


st.set_page_config(layout="centered")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)



st.markdown("""## Create a to-do list
            
### :material/description: Requirements
            
- 
""")


st.divider()

if "to_do_list" not in st.session_state:
    st.session_state["to_do_list"] = []

st.markdown("#### :material/widgets: :red[Expected output]")

with st.container(border=True):
    st.subheader("My To-do List:")

    thing = st.text_input("Things to add")
    add = st.button("Add to list")
    clear = st.button("Clear list")

    if add:
        st.session_state.to_do_list.append(thing)

    if clear:
        st.session_state.to_do_list = []

    if not st.session_state.to_do_list:
        text = ":rainbow[Hooray! My to-do list is empty!]"
    else:
        text = "Things in my to-do list:\n"
        for item in st.session_state.to_do_list:
            text += f"- {item}\n"

    st.markdown(text)        


obselete = """
if "to_do_list" not in st.session_state:
    st.session_state["to_do_list"] = {}
    


task = st.text_input("Things to add")
add = st.button("Add to list")

if add:
    st.session_state.to_do_list[task.capitalize()] = 1 
    
to_delete = st.multiselect("Things to delete", list(st.session_state.to_do_list.keys()))
delete = st.button("Delete from list")

if delete:
    for item in to_delete:
        st.session_state.to_do_list.pop(item)

if not st.session_state.to_do_list:
    text = "#### :rainbow[Hooray! My to-do list is empty!]"
else:
    text =  "#### Things in my to-do list:\n"
    for item in st.session_state.to_do_list.keys():
        text += f"- {item}\n"

st.markdown(text)        

"""