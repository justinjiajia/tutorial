import streamlit as st

st.set_page_config(layout="centered")

st.markdown("""
<style>
[data-testid=stExpander] summary p {
    font-size: 18px;
    font-weight: bold;
    color: salmon;
}
</style>
""", unsafe_allow_html=True)


st.markdown("#### :material/code_blocks: :blue[Source code to run]")

code = """x = st.slider('Choose a value', 0, 10)
y = st.slider('Choose a value', 0, 10)"""

with st.container(border=True):
    st.code(code)

st.markdown("#### :material/widgets: :red[Rendered output]")

with st.container(border=True):
    try:
        x = st.slider('Choose a value', 0, 10)
        y = st.slider('Choose a value', 0, 10)
    except Exception as e:
        st.error(e)    


with st.expander("Explanation"):
    st.markdown("Streamlit assigns an ID internally to each widget based on the arguments passed to the widget function (such as label, min or max value, default value, placeholder text, help text, and key).")
    st.markdown("When creating two widgets of the same type with the same arguments, we will get a `DuplicateWidgetID` error.")

st.divider()

st.markdown("This can be solved either by using different arguments when creating the same type of widgets:")

st.markdown("#### :material/code_blocks: :blue[Source code to run]")

code = """x = st.slider('Choose a value for variable x', 0, 10)
y = st.slider('Choose a value for variable y', 0, 10, step=2)"""

with st.container(border=True):
    st.code(code)

st.markdown("#### :material/widgets: :red[Rendered output]")

with st.container(border=True):
    x = st.slider('Choose a value for variable x', 0, 10)
    y = st.slider('Choose a value for variable y', 0, 10, step=2)  

st.info("Now the two widgets are different from Streamlit's perspective.")       


st.divider()

st.markdown("or by assigning widgets unique keys:")

st.markdown("#### :material/code_blocks: :blue[Source code to run]")

code = """x = st.slider('Choose a value', 0, 10, key="a")
y = st.slider('Choose a value', 0, 10, key="b")"""

with st.container(border=True):
    st.code(code)

st.markdown("#### :material/widgets: :red[Rendered output]")

with st.container(border=True):
    x = st.slider('Choose a value', 0, 10, key="a")
    y = st.slider('Choose a value', 0, 10, key="b")

st.markdown("When a widget is associated with a key, its value will be automatically added as a new item to `st.session_state`, which is a dictionary-like object that maintains the state of a user session.")
st.markdown("Then, we can use either an attribute-style or a dictionary-style syntax to read that item from `st.session_state`:")

st.markdown("#### :material/code_blocks: :blue[Source code to run]")

code = """st.write(f"The value of variable `x` is: `{st.session_state.a}`") 
st.write(f"The value of variable `y` is: `{st.session_state['b']}`")"""

with st.container(border=True):
    st.code(code)
    
st.markdown("#### :material/widgets: :red[Rendered output]")

with st.container(border=True):    
    st.markdown(f"The value of variable `x` is: `{st.session_state.a}`")       
    st.write(f"The value of variable `y` is: `{st.session_state["b"]}`")   

st.markdown("""Every time we update a widget associated with a key, the corresponding item in `st.session_state` gets updated as well.""")
    
st.markdown("""Therefore, widget keys serve two purposes:
- Distinguishing two otherwise identical widgets;
- Providing a means to access (and manipulate) the widget's value through `st.session_state`.""")    