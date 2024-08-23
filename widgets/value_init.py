import streamlit as st

st.set_page_config(layout="wide")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html=True)


st.markdown(
"""
We can initialize a widget's values via `st.session_state`. 

When a widget is assigned a key, calling the widget function at each run will first check if that key already exists in `st.session_state`.
If so, Streamlit assigns that key's value to the widget:
""")

st.markdown("#### :material/code_blocks: :blue[Source code to run]")

code = """if "a" not in st.session_state:   
    st.session_state["a"] = 2

# the widget's value will default to the key's value (i.e., 2)
x = st.slider('Choose a value', 0, 10, key="a")

st.write(f"The value of variable x is {x}.")
st.write(f"The value of st.session_state.a is {st.session_state.a}.")"""

with st.container(border=True):
    st.code(code)

st.markdown("#### :material/widgets: :red[Rendered output]")


with st.container(border=True):
    if "a" not in st.session_state: st.session_state["a"] = 2
    x = st.slider('Choose a value', 0, 10, key="a")

    st.write(f"The value of variable `x` is `{x}`.")
    st.write(f"The value of `st.session_state.a` is `{st.session_state.a}`.")

st.divider()

st.markdown("Streamlit will reset the widget's value in each run if the `if` test is removed:")


st.markdown("#### :material/code_blocks: :blue[Source code to run]")

code = """st.session_state["b"] = 2

y = st.slider('Choose a value', 0, 10, key="b")

st.write(f"The value of variable y is {y}.")
st.write(f"The value of st.session_state.b is {st.session_state.b}.")"""

with st.container(border=True):
    st.code(code)

st.markdown("#### :material/widgets: :red[Rendered output]")

with st.container(border=True):
    st.session_state["b"] = 2
    y = st.slider('Choose a value', 0, 10, key="b")

    st.write(f"The value of variable `y` is `{y}`.")
    st.write(f"The value of `st.session_state.b` is `{st.session_state.b}`.")

st.divider()

st.markdown("### Summary")

st.markdown("""
Here is a sequence of events triggered by a widget update on the screen:

   1. Update the backend value of the widget; If the widget is associated with a key, also update the corresponding item in `st.session_state`;
   2. Start (re)running the script;
   3. Call the widget function for this run to retrieve the backend value; If a key is attached to the widget and if that key alredy exists in `st.session_state`, use the key's value to override the widget's backend value.

The sequence of events upon an app's initial load is the same as described above, except that it starts from step 2 and the initial backend values are defaults configured via widget functions.
""")    

st.divider()

st.markdown("### Caveats to note")

st.markdown("- Setting a widget's value via `st.session_state` and using the `value` argument in the widget function at the same time is not recommended, and will throw a warning when the app is first started.")

code = """if "c" not in st.session_state: 
    st.session_state["c"] = 2
    
st.slider('Choose a value', 0, 10, 5, key="c")"""

with st.container(border=True):
    st.code(code)


with st.container(border=True):
    st.image("static/warning.png", width=750)

# thrown an error only upon using `streamlit run` to start it for the 1st run
# if "c" not in st.session_state: 
#    st.session_state["c"] = 2
# st.slider('Choose a value', 0, 10, 5, key="c")
    


st.markdown("- Once a widget is initialized with a key, modifying its value via `st.session_state` is not allowed:")

code = """st.slider('Choose a value', 0, 10, key="d")
st.session_state.d = 2)"""

with st.container(border=True):
    st.code(code)

with st.container(border=True):
    try: 
        st.slider('Choose a value', 0, 10, key="d")
        st.session_state.d = 2
    except Exception as e:
        st.error(e)    


st.markdown("- Setting the value of a button-like widget (e.g., `st.button`, `st.download_button`, `st.file_uploader`, etc.) via `st.session_state` is not allowed:")

code ="""st.session_state.my_button = True
st.button('Button', key='my_button')"""

with st.container(border=True):
    st.code(code)

with st.container(border=True):
    try: 
        
        st.session_state.my_button = True
        st.button('Button', key='my_button')

    except Exception as e:
        st.error(e)    