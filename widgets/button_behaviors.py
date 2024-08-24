import streamlit as st

st.set_page_config(layout="wide")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
    
st.markdown("""
<style>
[data-testid=stExpander] summary p {
    font-size: 18px;
    font-weight: bold;
    color: salmon;
}
</style>
""", unsafe_allow_html=True)



code = """import streamlit as st

name_str = st.text_input("Enter your surname")
submitted_bool = st.button("Submit")

st.write(f"The return value of st.text_input is '{name_str}' of {type(name_str)}.")
st.write(f"The return value of st.button is {submitted_bool} of {type(submitted_bool)}.")

if submitted_bool:
    st.write(name_str)
"""
st.markdown("#### :material/code_blocks: :blue[Source code to run]")
with st.container(border=True):
    st.code(code)

st.markdown("#### :material/widgets: :red[Rendered output]")
with st.container(border=True):
    name_str = st.text_input("Enter your username")
    submitted_bool = st.button("Submit")

    st.write(f"The return value of <code>st.text_input</code> is <code>'{name_str}'</code> of <code>{type(name_str)}</code>.",
            unsafe_allow_html=True)
    st.write(f"The return value of <code>st.button</code> is <code>{submitted_bool}</code> of <code>{type(submitted_bool)}</code>.", 
            unsafe_allow_html=True)

    if submitted_bool:
        st.write(f"<code>'{name_str}'</code>", unsafe_allow_html=True)

with st.expander("Explanation"):
    st.markdown("""Every time a widget gets updated on the screen, Streamlit ***reruns the entire Python script from top to bottom***.
                
The values of all the other widgets remain persistent across reruns except for button-like widgets.

By default, the `st.button` function has a value of `False`and transitions to `True` temporarily when clicked. It only lasts for a single run before reverting to `False`.
""")
    