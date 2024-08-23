import streamlit as st
import plotly.express as px
import altair as alt

st.set_page_config(layout="wide")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.markdown("""
As we've seen, Streamlit built-in charting functions can be useful if we want to visualize data quickly, but we trade off speed for customizability.

In production, more powerful libraries, such as Matplotlib, Seaborn, Plotly, and Altair, can give us the flexibility and customizability we want. 

Streamlit supports 6 popular Python visualization libraries. The rest of this section will provide a walk-through of Plotly and Altair for interactive plotting.
""")

st.markdown("### :material/dataset: Data to use")

with st.echo():
    import pandas as pd
    gapminder = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder-unclean.csv").dropna()

st.write(gapminder)

st.divider()


st.markdown("### [<code>st.plotly_chart</code>](https://docs.streamlit.io/develop/api-reference/charts/st.plotly_chart)", unsafe_allow_html=True)


st.markdown("""
[Plotly](https://plotly.com/) is an interactive visualization library that many data scientists use to visualize data. This library is very similar to Streamlit in its intent and useful in creating interactive visuals and dashboards.
            
Streamlit allows us to call plotly graphs from within Streamlit apps using the `st.plotly_chart()` function, making it a breeze to port any Plotly dashboards. 
""", unsafe_allow_html=True)




st.markdown("#### :material/code_blocks: :blue[Source code to run]")

code = """
# to run this snippet on your computer, you need to first install Plotly using pip install plotly
import plotly.express as px

fig = px.scatter(gapminder, x="gdpPercap", y="lifeExp", size="pop", color='continent', hover_data="country",
                 log_x=True, range_x=[100, 100000], range_y=[25, 90], size_max=55,
                 color_discrete_sequence=px.colors.qualitative.Set1,
                 category_orders={"continent": ["Asia", "Africa", "Americas", "Oceania", "Europe"]},
                 labels={'gdpPercap': 'GDP Per Capita', 'lifeExp': 'Life Expectancy', "continent": "Continent"},
                 animation_frame="year", animation_group="country",
                 width=800, height=500)

st.plotly_chart(fig, use_container_width=False)
"""



with st.container(border=True):
    st.code(code)

st.markdown("#### :material/animation: :red[Rendered output]") 

with st.container(border=True):
    # https://plotly.com/python/discrete-color/
    fig = px.scatter(gapminder, x="gdpPercap", y="lifeExp", size="pop", color='continent', hover_data="country",
                    log_x=True, range_x=[100, 100000], range_y=[25, 90], size_max=55,
                    color_discrete_sequence=px.colors.qualitative.Set1,
                    category_orders={"continent": ["Asia", "Africa", "Americas", "Oceania", "Europe"]},
                    labels={'gdpPercap': 'GDP Per Capita', 'lifeExp': 'Life Expectancy', "continent": "Continent"},
                   animation_frame="year", animation_group="country", width=800, height=500)
    fig.update_layout(legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01))
    st.plotly_chart(fig, use_container_width=False)


st.divider()

st.markdown("### [<code>st.altair_chart</code>](https://docs.streamlit.io/develop/api-reference/charts/st.altair_chart)", unsafe_allow_html=True)


st.markdown("""
[Altair](https://altair-viz.github.io/) is another popular Python library for interactive visualization. It uses a declarative grammer, which allows us to describe the intended chart outcome from different aspects (e.g., chart, mark, encodings, etc.) rather than force us to manually programming every step.
            
`st.altair_chart()` allows us to easily port any Altair charts into our streamlit apps.
""", unsafe_allow_html=True)




st.markdown("#### :material/code_blocks: :blue[Source code to run]")

code = """
# to run this snippet on your computer, you need to first install Altair using pip install altair
import altair as alt

x_slider = alt.binding_range(min=1952, max=2007, step=5, name='Year ')
x_select = alt.selection_point(name="x_select", fields=['year'], bind=x_slider, value=1952)

c = (alt.Chart(gapminder)
     .mark_circle()
     .encode(
         x=alt.X("gdpPercap", title='GDP Per Capita').scale(type="log", domain=[100, 100000]), 
         y=alt.Y("lifeExp", title='Life Expectancy').scale(domain=[25, 90])
             .axis(values=list(range(30, 91, 10))), 
         size=alt.Size('pop').scale(rangeMax=3000).legend(None), 
         color=alt.Color('continent', title="Continent", sort=["Asia", "Africa", "Americas", "Oceania", "Europe"])
             .scale(scheme="set1").legend(orient='top-left'),
         detail=alt.Detail("country"))
     .properties(width=800, height=500).transform_filter(x_select).add_params(x_select)
)

st.altair_chart(c, use_container_width=False)
"""



with st.container(border=True):
    st.code(code)


st.markdown("#### :material/animation: :red[Rendered output]") 

with st.container(border=True):
    x_slider = alt.binding_range(min=1952, max=2007, step=5, name='Year ')
    x_select = alt.selection_point(name="x_select", fields=['year'], bind=x_slider, value=1952)
    # Scales map a data domain (input range) to a visual range (output range)
    # without Detail, country information won't be displayed in the tooltip
    c = (
    alt.Chart(gapminder)
    .mark_circle()
    .encode(x=alt.X("gdpPercap", title='GDP Per Capita').scale(type="log", domain=[100, 100000]), 
            y=alt.Y("lifeExp", title='Life Expectancy').scale(domain=[25, 90]).axis(values=list(range(30, 91, 10))), 
            size=alt.Size('pop').scale(rangeMax=3000).legend(None), 
            color=alt.Color('continent', title="Continent", sort=["Asia", "Africa", "Americas", "Oceania", "Europe"])
               .scale(scheme="set1").legend(orient='top-left'),
            detail=alt.Detail("country")
            ).properties(width=800, height=500).transform_filter(x_select).add_params(x_select)
    )

    st.altair_chart(c, use_container_width=False)