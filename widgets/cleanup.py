import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
#### Widgets do not persist when not continually rendered

A widget needs to be continuously rendered on the frontend in order to remember user input.

If a widget's function is not called during a script run, none of its parts will be retained, including its value in `st.session_state`. This is because when Streamlit gets to the end of a script run, **a widget clean-up process** will delete all Session State items associated with widgets not currently on screen.

The following example shows even temporarily hiding a widget will cause the widget to reset when it reappears (and Streamlit will treat it like a new widget).
""")


code = """on_1 = st.toggle("Activate slider", True, key="toggle_1")

if on_1:
    st.slider('Choose a value', key="inside_toggle_1")

st.write(f"The value of the item `inside_toggle_1` in Session State: `{st.session_state.inside_toggle_1}`")"""

st.markdown("#### :material/code_blocks: :blue[Source code to run]")


with st.container(border=True):
    st.code(code)

st.markdown("#### :material/widgets: :red[Rendered output]")
 
with st.container(border=True):
    on_1 = st.toggle("Activate slider", True, key="toggle_1")

    if on_1:
        st.slider('Choose a value', key="inside_toggle_1")

    st.write(f"The value of the item `inside_toggle_1` in Session State: `{st.session_state.inside_toggle_1}`")

st.divider()

st.markdown("""#### How to save the information independently from the widget

##### Approach 1:

When the Session State item of a widget is manually re-saved, it will become detached from the widget until the widget function gets executed again. 

Consequently, even if its original widget is not rendered in a run, the Session State item will not be removed by the clean-up process.
""")

code = """if "inside_toggle_2" in st.session_state:
    # re-saving a Session State item decouples it from a widget
    st.session_state.inside_toggle_2 = st.session_state.inside_toggle_2

on_2 = st.toggle("Activate slider", True, key="toggle_2")

if on_2:
    x = st.slider('Choose a value', key="inside_toggle_2")

st.write(f"The value of the item `inside_toggle_2` in Session State: `{st.session_state.inside_toggle_2}`")
"""

st.markdown("#### :material/code_blocks: :blue[Source code to run]")

with st.container(border=True):
    st.code(code)

st.markdown("#### :material/widgets: :red[Rendered output]")
 
with st.container(border=True): 

    if "inside_toggle_2" in st.session_state:
        # re-saving a Session State item decouples it from a widget
        st.session_state.inside_toggle_2 = st.session_state.inside_toggle_2

    on_2 = st.toggle("Activate slider", True, key="toggle_2")

    if on_2:
        x = st.slider('Choose a value', key="inside_toggle_2")

    st.write(f"The value of the item `inside_toggle_2` in Session State: `{st.session_state.inside_toggle_2}`")


st.markdown("""But navigating away from this page will result in the same error, as the re-saving step is present and thereby takes effect only on this single page.

To completely circumvent the clean-up process, we need to add the re-saving step to every page of a multi-page app.        
""")


st.divider()

st.markdown("""##### Approach 2:

If we wish to navigate away from a widget and retain its value upon return, a better strategy is to use a separate key in `st.session_state` to save the information independently from the widget.

In the snippit below, `_inside_toggle_3` refers to the State State item coupled with the slider widget. It will be deleted by the widget clean-up process as we navigate away from the widget.

In contrast, `inside_toggle_3` is a separate Session State item that can hold a value persistently regardless of the widget's rendering and the clean-up process..

But then, how can we then ensure the value of the separate key to be always synchronized with that of the widget key?

            https://docs.streamlit.io/develop/concepts/architecture/widget-behavior                
""")

code = """def update_value(key):
    st.session_state[key] = st.session_state["_" + key]

def load_value(key):
    st.session_state["_" + key] = st.session_state[key]

if "inside_toggle_3" in st.session_state:
    load_value("inside_toggle_3")

on_3 = st.toggle("Activate slider", True, key="toggle_3")

if on_3:
    x = st.slider('Choose a value', key="_inside_toggle_3", on_change=update_value, args=["inside_toggle_3"])

st.write(f"The value of the item `_inside_toggle_3` in Session State: `{st.session_state._inside_toggle_3}`")
"""

st.markdown("#### :material/code_blocks: :blue[Source code to run]")

with st.container(border=True):
    st.code(code)



st.markdown("#### :material/widgets: :red[Rendered output]")

def update_value(key):
    st.session_state[key] = st.session_state["_" + key]

def load_value(key):
    st.session_state["_" + key] = st.session_state[key]

if "inside_toggle_3" in st.session_state:
        load_value("inside_toggle_3")

with st.container(border=True): 
    on_3 = st.toggle("Activate slider", True, key="toggle_3")

    if on_3:
        x = st.slider('Choose a value', key="_inside_toggle_3", on_change=update_value, args=["inside_toggle_3"])

    st.write(f"The value of the item `_inside_toggle_3` in Session State: `{st.session_state._inside_toggle_3}`")