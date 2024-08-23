import streamlit as st

st.set_page_config(layout="wide")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
    
st.markdown("""
<style>
[data-testid=stExpander] summary p {
    font-size: 20px;
    font-weight: bold;
    color: salmon;
}
</style>
""", unsafe_allow_html=True)


st.markdown("### :rainbow[Motivating Example: How to create a chat-like UI?]")


if "msgs" not in st.session_state:
    st.session_state.msgs = []

def send_message():
    st.session_state.msgs.append(st.session_state.message)

def clear_history():
    st.session_state.msgs = []

with st.container(border=True):
    for m in st.session_state.msgs:
        st.markdown(f"**Message**: {m}") 
        
    st.text_input("Enter your message", placeholder="hey, what's up?", 
                  key="message", label_visibility="collapsed")
    st.button('Send', key="send", on_click=send_message)

st.button('Clear chat history', key="clear", on_click=clear_history)

st.divider()


code = """message = st.text_input("Enter your message")
clicked = st.button('Show message below')

if clicked:
    st.write(f"**Message:** {message}")
"""

st.markdown("#### :material/code_blocks: :blue[Source code to run]")
with st.container(border=True):
    st.code(code)

st.markdown("#### :material/widgets: :red[Rendered output]")
with st.container(border=True):
    message = st.text_input("Enter your message")
    clicked = st.button('Show message below')

    if clicked: st.write(f"**Message:** {message}")

st.markdown("***Question: Why does updating the text field cause the message to the disappear?***")

with st.expander("Explanation"):
    st.markdown("""The button widget has an ephemeral value of `True` only for a single run after being clicked.
                
During a rerun triggered by updating the text field, the button widget's value has reverted to `False`, causing control to forgo the `st.write()` step.""")
                
    

st.divider()

st.markdown("To ensure a clicked button to continue to be `True`, we can add a separate item to `st.session_state` and use the button to set that item to `True`:")

st.markdown("#### :material/code_blocks: :blue[Source code to run]")
code = """# the key arguments are primarily used for distinguishing identical widgets on this page
if 'btn_1_clicked' not in st.session_state:
    st.session_state.btn_1_clicked = False

st.text_input("Enter your message", key="txt_1")
st.button('Show message below', key="btn_1")

# now the button widget's value can be accessed via st.session_state.btn_1
if st.session_state.btn_1:
    st.session_state.btn_1_clicked = True

if st.session_state.btn_1_clicked:
    st.write(f"**Message:** {st.session_state.txt_1}")
"""


if 'btn_1_clicked' not in st.session_state:
    st.session_state.btn_1_clicked = False

with st.container(border=True):
    st.code(code)

st.markdown("#### :material/widgets: :red[Rendered output]")

with st.container(border=True):
    st.text_input("Enter your message", key="txt_1")
    st.button('Show message below', key="btn_1")
    
    if st.session_state.btn_1:
        st.session_state.btn_1_clicked = True

    if st.session_state.btn_1_clicked:
        st.write(f"**Message:** {st.session_state.txt_1}")

st.markdown("`st.session_state.btn_1_clicked` remains `True` throughout this user session (i.e., connection).")

st.markdown("***Question: Why can't we simply use `st.session_state.btn_1` to govern the execution of `st.write()`?***")

with st.expander("Explanation"):
    st.markdown("""The value of `st.session_state.btn_1` is inherently coupled with the button widget's backend value. Like the widget, this state item can only hold a value of `True` temporarily.

In contrast, `st.session_state.btn_1_clicked` is an independent item and won't be affected by the value of the button widget.
""")
                

st.divider()


st.markdown("""What if we want to show the input message above?

Can we simply advance the `if` statement that encloses `st.write()` as follows?
""")


code = """if 'btn_2_clicked' not in st.session_state:
    st.session_state.btn_2_clicked = False

if st.session_state.btn_2_clicked:
    st.write(f"**Message:** {st.session_state.txt_2}")

st.text_input("Enter your message", key="txt_2")
st.button('Show message above', key="btn_2")

if st.session_state.btn_2:
    st.session_state.btn_2_clicked = True
"""

if 'btn_2_clicked' not in st.session_state:
    st.session_state.btn_2_clicked = False


st.markdown("#### :material/code_blocks: :blue[Source code to run]")
with st.container(border=True):
    st.code(code)

st.markdown("#### :material/widgets: :red[Rendered output]")
with st.container(border=True):
    if st.session_state.btn_2_clicked:

        try: 
        # navigating away from this page and revisiting it will thrown an error
        # because st.session_state.txt_2 is removed by the widget clean-up process
        # the re-saving approach does not solve the problem, because it won't be reached as the next run involves a different page
            st.write(f"**Message:** {st.session_state.txt_2}")
        except:
            st.error("`'txt_2'` is not found in `st.session_state`, because it is coupled with the text input widget and was removed by the widget clean-up process when we navigated away from this page. The second to last example provides a solution to this error.")

    st.text_input("Enter your message", key="txt_2")
    st.button('Show message above', key="btn_2")

    if st.session_state.btn_2:
        st.session_state.btn_2_clicked = True


st.markdown("***Question: Clicking the button doesn't display the message right away. Why doesn't it work as intended?***")

with st.expander("Explanation"):
    st.markdown("""Clicking the button triggers a rerun of the script from the beginning. When the if test that wraps `st.write()` is reached, `st.session_state.btn_2_clicked` is still `False`. This session state item gets set to `True` near the end of this rerun.
""")

st.divider()


st.markdown("""The problem would be solved if setting `st.session_state.btn_2_clicked` to `True` occurred before the rerun of the script or even as soon as the button gets clicked.  

This is where a callback function comes in handy.
            
A callback function gets executed as soon as its associated widget gets updated, prior to a rerun of the script.
            
We can use the argument `on_change` (or `on_click`) of a widget function to implement a callback:

- `on_change` or `on_click` takes the function name to be used as a callback;
  
- Additionally, there are optional arguments `args` and `kwargs` to take the inputs required by the callback function itself:

    - `args` (`tuple` or `list`) - List of arguments to be passed to the callback function

    - `kwargs` (`dict`) - Named arguments to be passed to the callback function.
""")            


code = """if 'btn_3_clicked' not in st.session_state:
    st.session_state.btn_3_clicked = False

def submit_btn_3():
    st.session_state.btn_3_clicked = True

if st.session_state.btn_3_clicked:
    st.write(f"**Message:** {st.session_state.txt_3}")

st.text_input("Enter your message", key="txt_3")
st.button('Show message above', key="btn_3", on_click=submit_btn_3)
"""

st.markdown("#### :material/code_blocks: :blue[Source code to run]")
 

with st.container(border=True):
    st.code(code)

if 'btn_3_clicked' not in st.session_state:
    st.session_state.btn_3_clicked = False

def submit_btn_3():
    st.session_state.btn_3_clicked = True


st.markdown("#### :material/widgets: :red[Rendered output]")

with st.container(border=True):
    if st.session_state.btn_3_clicked:
        try: 
            st.write(f"**Message:** {st.session_state.txt_3}")
        except:
            st.error("`'txt_3'` is not found in `st.session_state`, because it is coupled with the text input widget and was removed by the widget clean-up process when we navigated away from this page. The second to last example provides a solution to this error.")
    st.text_input("Enter your message", key="txt_3")
    st.button('Show message above', key="btn_3", on_click=submit_btn_3)

    


st.divider()


st.markdown("""Now, let's try to make our user interface more chat-like: We want the message displayed above to be updated only after clicking the button for confirmation.

So, how can we prevent the displayed message from continuously changing as we update the content in the text field?
""")


code = """if 'btn_4_clicked' not in st.session_state:
    st.session_state.btn_4_clicked = False

def send_msg_1():
    st.session_state.btn_4_clicked = True
    st.session_state.msg = st.session_state.txt_4

if st.session_state.btn_4_clicked:
        st.write(f"**Message:** {st.session_state.msg}")

st.text_input("Enter your message", key="txt_4", placeholder="hey, what's up?", 
              label_visibility="collapsed")
st.button('Send', key="btn_4", on_click=send_msg_1)
"""

st.markdown("#### :material/code_blocks: :blue[Source code to run]")
 

with st.container(border=True):
    st.code(code)

st.markdown("#### :material/widgets: :red[Rendered output]")

if 'btn_4_clicked' not in st.session_state:
    st.session_state.btn_4_clicked = False

def send_msg_1():
    st.session_state.btn_4_clicked = True
    st.session_state.msg = st.session_state.txt_4

with st.container(border=True):
    if st.session_state.btn_4_clicked:
        st.write(f"**Message:** {st.session_state.msg}")
    st.text_input("Enter your message", placeholder="hey, what's up?", 
                  key="txt_4", label_visibility="collapsed")
    st.button('Send', key="btn_4", on_click=send_msg_1)


st.divider()

code = """if "messages" not in st.session_state:
    st.session_state.messages = []

def send_msg_2():
    st.session_state.messages.append(st.session_state.txt_5)

for m in st.session_state.messages:
    st.markdown(f"**Message**: {m}") 

st.text_input("Enter your message", key="txt_5", placeholder="hey, what's up?", 
              label_visibility="collapsed")
st.button('Send', key="btn_5", on_click=send_msg_2)
"""

st.markdown("#### :material/code_blocks: :blue[Source code to run]")
with st.container(border=True):
    st.code(code)

st.markdown("#### :material/widgets: :red[Rendered output]")

if "messages" not in st.session_state:
    st.session_state.messages = []

def send_msg_2():
    st.session_state.messages.append(st.session_state.txt_5)


with st.container(border=True):
    for m in st.session_state.messages:
        st.markdown(f"**Message**: {m}") 
    st.text_input("Enter your message", key="txt_5", placeholder="hey, what's up?", 
                  label_visibility="collapsed")
    st.button('Send', key="btn_5", on_click=send_msg_2)