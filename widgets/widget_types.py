import streamlit as st

st.set_page_config(layout="wide")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.markdown("## Widgets that return string values")


st.markdown("### :material/list_alt: [`st.selectbox()`](https://docs.streamlit.io/develop/api-reference/widgets/st.selectbox)")

st.markdown("<br/>", unsafe_allow_html=True)


with st.container(border=True):
    with st.echo("below"):
        # default to the 1st option
        contact_str = st.selectbox(
            "How would you like to be contacted?",
            ("Email", "Home phone", "Mobile phone")
        )

st.markdown(f"The value of variable <code>contact_str</code> is <code>'{contact_str}'</code> of <code>{type(contact_str)}</code>.",
            unsafe_allow_html=True)
with st.expander("Show documentation"):
    st.write(st.selectbox.__doc__)
st.divider()

st.markdown("### :material/list_alt: [`st.radio()`](https://docs.streamlit.io/develop/api-reference/widgets/st.radio)")

st.markdown("<br/>", unsafe_allow_html=True)

with st.container(border=True):
    with st.echo("below"):
        # default to the 1st option
        genre_str = st.radio(
            "What's your favorite movie genre?",
            ["Comedy", "Drama", "Documentary"]
        )
        
st.markdown(f"The value of variable <code>genre_str</code> is <code>'{genre_str}'</code> of <code>{type(genre_str)}</code>.",
            unsafe_allow_html=True)
with st.expander("Show documentation"):
    st.write(st.radio.__doc__)

st.divider()

st.markdown("### :material/list_alt: [`st.text_input()`](https://docs.streamlit.io/develop/api-reference/widgets/st.text_input)")

st.markdown("<br/>", unsafe_allow_html=True)


with st.container(border=True):
    with st.echo("below"):
    # default to an empty string
        name_str = st.text_input("Entuer your username")
st.markdown(f"The value of variable <code>name_str</code> is <code>'{name_str}'</code> of <code>{type(name_str)}</code>.",
            unsafe_allow_html=True)


st.info("Simply typing inside the widget won't rerun its widget function to return a new value. An update is triggered either by clicking or tabbing out of the widget or by pressing `Enter`.", 
        icon="🚨")

with st.expander("Show documentation"):
    st.write(st.text_input.__doc__)

st.divider()
 
st.markdown("### :material/list_alt: [`st.text_area()`](https://docs.streamlit.io/develop/api-reference/widgets/st.text_area)")

st.markdown("<br/>", unsafe_allow_html=True)

with st.container(border=True):
    with st.echo("below"):
        # default to an empty string
        txt_str = st.text_area("Text to analyze")
st.markdown(f"The value of variable <code>name_str</code> is<br><code>'''{txt_str}'''</code><br>of <code>{type(txt_str)}</code>",
            unsafe_allow_html=True)
with st.expander("Show documentation"):
    st.write(st.text_area.__doc__)


st.info("Simply typing inside the widget won't rerun the widget function to return a new value. An update is triggered either by clicking or tabbing out of the widget or by pressing `Ctrl+Enter`.",
        icon="🚨")


st.divider()

st.markdown("### Widgets that return list values")

st.markdown("### :material/list_alt: [`st.multiselect()`](https://docs.streamlit.io/develop/api-reference/widgets/st.multiselect)")

st.markdown("<br/>", unsafe_allow_html=True)
 
with st.container(border=True):
    with st.echo("below"):
        # default to an empty list
        colors_list = st.multiselect(
            "What are your favorite colors",
            ["Green", "Yellow", "Red", "Blue"]
        )

st.markdown(f"The value of variable <code>colors_list</code> is <code>{colors_list}</code> of <code>{type(colors_list)}</code>.",
            unsafe_allow_html=True)
with st.expander("Show documentation"):
    st.write(st.multiselect.__doc__)
st.divider()

st.markdown("### Widgets that return numeric values")
 

st.markdown("### :material/list_alt: [`st.slider()`](https://docs.streamlit.io/develop/api-reference/widgets/st.slider)")

st.markdown("<br/>", unsafe_allow_html=True)

with st.container(border=True):
    with st.echo("below"):
        # default to the minimum value
        slider_float = st.slider(
            'Choose a value',
            min_value=10.0, max_value=50.0
        )

st.markdown(f"The value of variable <code>slider_float</code> is <code>{slider_float}</code> of <code>{type(slider_float)}</code>.",
            unsafe_allow_html=True)

with st.container(border=True):
    with st.echo("below"):
        # default to the minimum value
        slider_int = st.slider(
            'Choose a value',
            min_value=10, max_value=50
        )

st.markdown(f"The value of variable <code>slider_int</code> is <code>{slider_int}</code> of <code>{type(slider_int)}</code>.",
            unsafe_allow_html=True)

st.divider()

st.markdown("""Passing a tuple/list of two numeric values as the `value` argument creates a range selector.

Make sure that the types of the numberic values is consistent of those of the maximum and minimum values."""
)

with st.container(border=True):
    with st.echo("below"):
        # default to the minimum value
        slider_float_range = st.slider(
            'Choose a value', min_value=10.0, max_value=50.0,
            value=(10.0, 20.0)
        )
st.markdown(f"The value of variable <code>slider_float_range</code> is <code>{slider_float_range}</code> of <code>{type(slider_float_range)}</code>.",
            unsafe_allow_html=True)

with st.container(border=True):
    with st.echo("below"):
        # default to the minimum value
        slider_int_range = st.slider(
            'Choose a value', min_value=10, max_value=50, 
            value=[30, 40]
        )
st.markdown(f"The value of variable <code>slider_int_range</code> is <code>{slider_int_range}</code> of <code>{type(slider_int_range)}</code>.",
            unsafe_allow_html=True)


with st.expander("Show documentation"):
    st.write(st.slider.__doc__)

st.divider()

st.markdown("### :material/list_alt: [`st.number_input()`](https://docs.streamlit.io/develop/api-reference/widgets/st.number_input)")

st.markdown("<br/>", unsafe_allow_html=True)
 

with st.container(border=True):
    with st.echo("below"):
        input_float = st.number_input('Input a value')

st.markdown(f"The value of variable <code>input_float</code> is <code>{input_float}</code> of <code>{type(input_float)}</code>.",
            unsafe_allow_html=True)

with st.container(border=True):
    with st.echo("below"):
        input_int = st.number_input('Input a value', value=0)

st.markdown(f"The value of variable <code>input_int</code> is <code>{input_int}</code> of <code>{type(input_int)}</code>.",
            unsafe_allow_html=True)

with st.expander("Show documentation"):
    st.write(st.number_input.__doc__)
st.divider()

st.markdown("### Widgets that return Boolean values")

st.markdown("### :material/list_alt: [`st.checkbox()`](https://docs.streamlit.io/develop/api-reference/widgets/st.checkbox)")

st.markdown("<br/>", unsafe_allow_html=True)
 
with st.container(border=True):
    with st.echo("below"):
        # default to False
        agree_bool = st.checkbox("I agree")
st.markdown(f"The value of variable <code>agree_bool</code> is <code>{agree_bool}</code> of <code>{type(agree_bool)}</code>.",
            unsafe_allow_html=True)
with st.expander("Show documentation"):
    st.write(st.checkbox.__doc__)
st.divider()

st.markdown("### :material/list_alt: [`st.toggle()`](https://docs.streamlit.io/develop/api-reference/widgets/st.toggle)")

st.markdown("<br/>", unsafe_allow_html=True)


with st.container(border=True):
    with st.echo("below"):
        # default to False
        activated_bool = st.toggle("Activate feature")
st.markdown(f"The value of variable <code>activated_bool</code> is <code>{activated_bool}</code> of <code>{type(activated_bool)}</code>.",
            unsafe_allow_html=True)
with st.expander("Show documentation"):
    st.write(st.toggle.__doc__)
st.divider()

st.markdown("### Widgets that return date/time values (Optional)")

st.markdown("### :material/list_alt: [`st.time_input()`](https://docs.streamlit.io/develop/api-reference/widgets/st.time_input)")

st.markdown("<br/>", unsafe_allow_html=True)
 
with st.container(border=True):
    with st.echo("below"):
        # default to the current time
        t_time = st.time_input("Set an alarm for")
st.markdown(f"The value of variable <code>t_time</code> is <code>{t_time}</code> of <code>{type(t_time)}</code>.",
            unsafe_allow_html=True)
with st.expander("Show documentation"):
    st.write(st.time_input.__doc__)
st.divider()

st.markdown("### :material/list_alt: [`st.date_input()`](https://docs.streamlit.io/develop/api-reference/widgets/st.date_input)")

st.markdown("<br/>", unsafe_allow_html=True)
 

with st.container(border=True):
    with st.echo("below"):
        # default to the current date
        bd_date = st.date_input("When's your birthday?")
st.markdown(f"The value of variable <code>bd_date</code> is <code>{bd_date}</code> of <code>{type(bd_date)}</code>.",
            unsafe_allow_html=True)
with st.expander("Show documentation"):
    st.write(st.date_input.__doc__)