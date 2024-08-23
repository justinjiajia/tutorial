import streamlit as st

st.set_page_config(layout="wide")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
    
code = """if "msg_1" not in st.session_state:
    st.session_state.msgs_1 = []

def send_message_1():
    st.session_state.msgs_1.append({"user": st.session_state.user_1,
                                    "content": st.session_state.msg_1})
def clear_history_1():
    st.session_state.msgs_1 = []

for m in st.session_state.msgs_1:
    st.markdown(f"**To {m['user']}**: {m['content']}")

st.selectbox("Choose user", ["👧", "👱‍♀️", "👨🏿", "👴"], key="user_1")
st.text_input("Enter your message", key="msg_1",  placeholder="hey, what's up?", 
              label_visibility="collapsed")
st.button('Send', on_click=send_message_1)
st.button('Clear chat history', key="clear_1", on_click=clear_history_1)"""

st.markdown("#### :material/code_blocks: :blue[Source code to run]")
with st.container(border=True):
    st.code(code)

st.markdown("#### :material/widgets: :red[Rendered output]")

if "msg_1" not in st.session_state:
    st.session_state.msgs_1 = []

def send_message_1():
    st.session_state.msgs_1.append({"user": st.session_state.user_1,
                                    "content": st.session_state.msg_1})
def clear_history_1():
    st.session_state.msgs_1 = []

with st.container(border=True):
    for m in st.session_state.msgs_1:
        st.markdown(f"**To {m["user"]}**: {m["content"]}")

    st.selectbox("Choose user", ["👧", "👱‍♀️", "👨🏿", "👴"], key="user_1")
    st.text_input("Enter your message", key="msg_1", placeholder="hey, what's up?", label_visibility="collapsed")
    st.button('Send', on_click=send_message_1)

st.button('Clear chat history', key="clear_1", on_click=clear_history_1)


st.divider()

st.markdown("""Bear in mind: A Streamlit widget will trigger a script rerun whenever a user modifies its value.

                      
> However, when our app grows larger and more complex, this default behavior may make it less efficient and performant.
            
> More critically, it may result in an ill-designed app when the app's business logic depends on a full set of user inputs as opposed to any individual piece in that set.
            
When we don't want to rerun a script with each input made by a user, `st.form` comes to the rescue! 
            
A form is a container that visually groups other elements and widgets together. It helps batch multiple user inputs into a single rerun.

To add elements to a form object, we can either
1) use `with` notation (preferred);
2) or call methods directly on the form object.
""")

code = """# approach 1
with st.form("form"):
    st.selectbox("Choose user", ["👧", "👱‍♀️", "👨🏿", "👴"])
    st.text_input("Enter your message", placeholder="hey, what's up?", label_visibility="collapsed")
    st.form_submit_button('Send')"""

with st.container(border=True):
    st.code(code)

code = """# approach 2
chat = st.form("form")
chat.selectbox("Choose user", ["👧", "👱‍♀️", "👨🏿", "👴"])
chat.text_input("Enter your message", placeholder="hey, what's up?", label_visibility="collapsed")
chat.form_submit_button('Send')"""

with st.container(border=True):
    st.code(code)




st.markdown("#### :material/widgets: :red[Rendered output]")
 
chat = st.form("form")
chat.selectbox("Choose user", ["👧", "👱‍♀️", "👨🏿", "👴"])
chat.text_input("Enter your message", placeholder="hey, what's up?", label_visibility="collapsed")
chat.form_submit_button('Send')

st.markdown("""Note that every form must contain a `st.form_submit_button`. Other button-like widgets (i.e., `st.button` and `st.download_button`) can not be used within a form.

When the submission button is pressed, all frontend values inside the form are sent to the backend in batch, and the script reruns.""")


st.markdown("""Recall: for widgets outside of a form, when a user changes a widget's value on the frontend, the following events will occur in sequence:

- The widget's backend value is updated; if the widget is associated with a key, the corresponding item in `st.session_state` is also updated.

- The callback function if any is executed.
  
- The page reruns with the widget function returning its new value.
            
However, for widgets inside a form, any frontend changes made by a user do not get passed to the backend until the form is submitted. 
            
""")

st.divider()


st.markdown("""Now with the help with `st.form`, we can get rid of undesired reruns caused by frontend changes made to `st.selectbox` and `st.text_input`.

A bit more detail to know: `st.form_submit_button` is the only widget inside a form that can have a callback function.
                        
""")


code = """if "msgs_2" not in st.session_state:
    st.session_state.msgs_2 = []

def send_message_2():
    st.session_state.msgs_2.append({"user": st.session_state.user_2,
                                    "content": st.session_state.msg_2})
def clear_history_2():
    st.session_state.msgs_2 = []

with st.form("send_msg_1"):

    for m in st.session_state.msgs_2:
        st.markdown(f"**To {m['user']}**: {m['content']}")

    st.selectbox("Choose user", ["👧", "👱‍♀️", "👨🏿", "👴"], key="user_2")
    st.text_input("Enter your message", key="msg_2", placeholder="hey, what's up?", 
                  label_visibility="collapsed")
    st.form_submit_button('Send', on_click=send_message_2)

st.button('Clear chat history', key="clear_2", on_click=clear_history_2)"""

st.markdown("#### :material/code_blocks: :blue[Source code to run]")
with st.container(border=True):
    st.code(code)

st.markdown("#### :material/widgets: :red[Rendered output]")

if "msgs_2" not in st.session_state:
    st.session_state.msgs_2 = []

def send_message_2():
    st.session_state.msgs_2.append({"user": st.session_state.user_2,
                                    "content": st.session_state.msg_2})
def clear_history_2():
    st.session_state.msgs_2 = []

with st.form("send_msg_1"):

    for m in st.session_state.msgs_2:
        st.markdown(f"**To {m["user"]}**: {m["content"]}")

    st.selectbox("Choose user", ["👧", "👱‍♀️", "👨🏿", "👴"], key="user_2")
    st.text_input("Enter your message", key="msg_2", placeholder="hey, what's up?", label_visibility="collapsed")
    st.form_submit_button('Send', on_click=send_message_2)

st.button('Clear chat history', key="clear_2", on_click=clear_history_2)


