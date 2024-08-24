import streamlit as st

 
st.set_page_config(layout="wide")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.markdown("Default values are configurable for all widgets with a few special exceptions like <code>st.button</code> and <code>st.file_uploader</code>.", 
            unsafe_allow_html=True)

st.markdown("The defaults of selectbox widgets and radio button widgets can be set via their widget functions' <code>index</code> argument:", 
            unsafe_allow_html=True)


st.markdown("##### Set the <code>index</code> argument:", unsafe_allow_html=True)
option_index = st.number_input("Set the index argument:", min_value=0, max_value=2, value=None, label_visibility="collapsed")
selectbox_dict = {0: "Email", 1: "Home phone", 2: "Mobile phone", None: None}
radio_dict = {0: "Comedy", 1: "Drama", 2: "Documentary", None: None}
 
def render_selectbox(index):
    with st.container(height=400):
        st.write("##### :blue[Source code to run:]")
        st.code(f"""st.selectbox("How would you like to be contacted?",
             ("Email", "Home phone", "Mobile phone"),
             index={index})""")   
        st.divider()
        st.session_state.selectbox = selectbox_dict[index]

        st.write("##### :red[Widget rendered upon initial load:]")

        # default to the 1st option
        contact_str = st.selectbox(
            "How would you like to be contacted?",
            ("Email", "Home phone", "Mobile phone"),
            key="selectbox"
        )

def render_radio(index):
    with st.container(height=400):
        st.write("##### :blue[Source code to run:]")
        st.code(f"""st.radio("What's your favorite movie genre?",
         ["Comedy", "Drama", "Documentary"],
         index={index})""")   
        st.divider()
        st.session_state.radio = radio_dict[index]

        st.write("##### :red[Widget rendered upon initial load:]")

        st.radio(
            "What's your favorite movie genre?",
            ["Comedy", "Drama", "Documentary"],
            key="radio"
        )

col1, col2 = st.columns(2)

with col1:
    render_selectbox(option_index)

with col2:
    render_radio(option_index)

st.divider()

st.markdown("The default of a multiselect widget can be configured via the widget function's <code>default</code> argument:", 
            unsafe_allow_html=True)

st.markdown("##### Set the <code>default</code> argument:", unsafe_allow_html=True)

if "selected_options"  not in st.session_state:
    st.session_state["selected_options"] = []

col3, col4, *_ = st.columns(5)

with col3:
    green = st.checkbox("Green")
    red = st.checkbox("Red")

with col4:    
    yellow = st.checkbox("Yellow")
    blue = st.checkbox("Blue")


for color, selected in zip(["Green", "Yellow", "Red", "Blue"], [green, yellow, red, blue]):
    if selected:
        if color not in st.session_state["selected_options"]:
            st.session_state["selected_options"].append(color)
    else:
        if color in st.session_state["selected_options"]:   
            st.session_state["selected_options"].remove(color)

 

def render_multiselect(options):
    with st.container(height=400):
        st.write("##### :blue[Source code to run:]")
        code = f"""st.multiselect("What are your favorite colors?",
               ["Green", "Yellow", "Red", "Blue"]
"""
        
        if options:
            code += f"""               default={options}
)"""
        else: code += """)"""
        st.code(code) 
        st.divider()
        st.session_state.multiselect = options

        st.write("##### :red[Widget rendered upon initial load:]")
        st.multiselect("What are your favorite colors?", ["Green", "Yellow", "Red", "Blue"], key="multiselect")



col5, _ = st.columns(2)

with col5:
    render_multiselect(st.session_state["selected_options"])
    
st.divider()

st.markdown("The defaults of most of the other widegets can be configured via their widget functions' <code>value</code> argument.", 
            unsafe_allow_html=True)

st.markdown("For widget functions such as <code>st.slider</code> and <code>st.number_input</code>, the defaults can also affect the functionality of the rendered widegets.", 
            unsafe_allow_html=True)

st.markdown("##### Set the <code>value</code> argument:", unsafe_allow_html=True)

selected_value = st.selectbox("Set the value argument:", 
                              [10, 0.5, 5.0], 
                              label_visibility="collapsed")
 

col6, col7 = st.columns(2)

def render_number_input(value):
    with st.container(height=400):
        st.write("##### :blue[Source code to run:]")
        code = f"""st.number_input("Choose a number", value={value})"""
        st.code(code) 
        st.divider()

        st.write("##### :red[Widget rendered:]")

        st.number_input("Choose a number", value=value, key="number_input")

def render_slider(value):
    with st.container(height=400):
        st.write("##### :blue[Source code to run:]")
        code = f"""st.slider("Choose a number", value={value})"""
        st.code(code) 
        st.divider()

        st.write("##### :red[Widget rendered:]")

        st.slider("Choose a number", value=value, key="slider")

with col6:
    render_number_input(selected_value) 

with col7:
    render_slider(selected_value)    