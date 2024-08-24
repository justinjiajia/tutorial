import streamlit as st

import sys

sys.path.append('..')

from utils import load_to_df

st.set_page_config(layout="wide")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.markdown("""
Streamlit provides 5 built-in charting/plotting functions – `st.line_chart()`, `st.area_chart()`, `st.scatter_chart()`, `st.bar_chart()`, and `st.map()`. 
            
They all work similarly by aligning variables with desired aesthetics. 
""")

st.markdown("### :material/dataset: Data to use")



code = """
import pandas as pd

medals = pd.read_csv(
    'https://raw.githubusercontent.com/justinjiajia/datafiles/main/medals.csv', parse_dates=['year']
    ).query("country == 'China'")
"""

st.code(code)

medals = load_to_df('https://raw.githubusercontent.com/justinjiajia/datafiles/main/medals.csv', parse_dates=['year']).query("country == 'China'")    


st.write(medals)

st.divider()


st.markdown("### :material/list_alt: [`st.line_chart()`](https://docs.streamlit.io/develop/api-reference/charts/st.line_chart)")

st.markdown("""<br/>
            
For some datasets, we may want to understand changes in one variable as a function of time, or a similarly continuous variable. In this situation, a good choice is to draw a line chart, 
as it represents changes in value by sequentially connecting points with line segments.

If we align `color` with a categorical variable (i.e., a column that contains discrete values), data points will be grouped into lines of the same color based on the value of this variable. As a result, we can inspect the trends of different data series in one place.
""", unsafe_allow_html=True)

st.markdown("#### :material/code_blocks: :blue[Source code to run]")

code ="""
st.line_chart(medals, x="date", y="return", color="symbol")
"""

with st.container(border=True):
    st.code(code)


st.markdown("#### :material/ssid_chart: :red[Rendered output]") 

with st.container(border=True):
    st.line_chart(medals, x="year", y="total", color="type", 
                  width=720, height=500, use_container_width=False)


### st.line_chart will sort the values of the column used for the x axis automatically """
## To create an effective line chart, we typcially need to ensure that the values of the variable used for the horizontal axis are sorted in their inherent order.
##This is because  Therefore, messing up the order will result in confusing and meaningless charts that do not accurately represent the underlying data patterns.
##""")


with st.expander("Show documentation"):
    st.write(st.line_chart.__doc__)


st.divider()


st.markdown("### :material/list_alt: [`st.area_chart()`](https://docs.streamlit.io/develop/api-reference/charts/st.area_chart)")

st.markdown("""<br/>
            
Area charts are a type of chart that uses filled areas to represent the evolution of values over time or another continuous variable. 
            
Additionally, by stacking multiple area segments on top of each other,
an area chart also allows us to visualize the cumulative sum or total of the values at each point, along with the individual trends.

<br/>
""", unsafe_allow_html=True)


stack = st.toggle("Stack medals", value=True)


 
st.markdown("#### :material/code_blocks: :blue[Source code to run]")

code =f"""
st.area_chart(medals, x="year", y="total", color="type", stack={stack})
"""

with st.container(border=True):
    st.code(code)

st.markdown("#### :material/area_chart: :red[Rendered output]") 
with st.container(border=True):
    st.area_chart(medals, x="year", y="total", color="type", stack=stack,
                 width=720, height=500, use_container_width=False)



with st.expander("Show documentation"):
    st.write(st.area_chart.__doc__)

st.divider()
    

st.markdown("""<br/>

Streamlit also allows us to customize the colors used for different categories.
However, to leverage this color customization feature,  it's necessary to first transform the DataFrame into a wide format.

In such a wide format, categories are no longer represented as distinct values within a single column (e.g., `total`).
Rather, they are mapped into independent columns (e.g., `Gold`, `Silver`, and `Bronze`).
""", unsafe_allow_html=True) 

st.markdown("### :material/dataset: Data to use")


code = """
import pandas as pd

medals_w = pd.read_csv(
    'https://raw.githubusercontent.com/justinjiajia/datafiles/main/medals_w.csv', parse_dates=['year']
    ).query("country == 'China'")
"""

with st.container():
    st.code(code)

medals_w = load_to_df('https://raw.githubusercontent.com/justinjiajia/datafiles/main/medals_w.csv', parse_dates=['year']).query("country == 'China'")    

st.write(medals_w)


st.divider()

chart_type = st.selectbox("Select chart type", ["Area", "Line"])

st.markdown("#### :material/code_blocks: :blue[Source code to run]")

if chart_type == "Area":
    code ="""
    # "#A77044", "#FEE101", and "#A7A7AD" are the Hex color codes for Bronze, Gold, and Silver, respectively
    # https://www.schemecolor.com/olympic-medals-color-scheme.php

    st.area_chart(medals_w, x="year", y=['Bronze', 'Gold', 'Silver'], 
                  color=["#A77044", "#FEE101", "#A7A7AD"], stack=True)
    """
else:
    code ="""
    # "#A77044", "#FEE101", and "#A7A7AD" are the Hex color codes for Bronze, Gold, and Silver, respectively
    # https://www.schemecolor.com/olympic-medals-color-scheme.php

    st.line_chart(medals_w, x="year", y=['Bronze', 'Gold', 'Silver'], 
                  color=["#A77044", "#FEE101", "#A7A7AD"])
    """



with st.container(border=True):
    st.code(code)


st.markdown("#### :material/area_chart: :red[Rendered output]") 
# Streamlit chart functions sort column names automatically ; even if we put ['Gold', 'Silver', 'Bronze'], we still get these names sorted in dictionary order
# "#A77044" is the color for Bronze; "#FEE101" is the color for gold
with st.container(border=True):
    if chart_type == "Area":
        st.area_chart(medals_w, x="year", y=['Gold', 'Silver', 'Bronze'], color=["#A77044", "#FEE101", "#A7A7AD"], stack=True,
                    width=720, height=500, use_container_width=False)
    else:
        st.line_chart(medals_w, x="year", y=['Gold', 'Silver', 'Bronze'], color=["#A77044", "#FEE101", "#A7A7AD"],
                    width=720, height=500, use_container_width=False)




st.divider()

st.markdown("### :material/dataset: Data to use")

code = """
import pandas as pd

iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
"""

with st.container():
    st.code(code)

iris = load_to_df('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')


st.write(iris)

st.divider()

st.markdown("### :material/list_alt: [`st.scatter_chart()`](https://docs.streamlit.io/develop/api-reference/charts/st.scatter_chart)")

st.markdown("""<br/>
            
A scatter chart uses the positioning of geometric shapes to visually epresent the values of two numeric variables in a data set.
            
It proves particularly useful for revealing relationships between the variables and illustrating how data points are distributed across the plane formed by them.
            
<br/>
            
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

iris_x = col1.selectbox("Choose variable for coordinate x", ["sepal_length", "sepal_width", "petal_length", "petal_width"])
iris_y = col2.selectbox("Choose variable for coordinate y", ["sepal_length", "sepal_width", "petal_length", "petal_width"], index=1)
iris_size = st.selectbox("Choose variable for size", ["sepal_length", "sepal_width", "petal_length", "petal_width"], index=None)
iris_color = st.checkbox("Use color to annotate species")

if iris_size:
    code = f"""
    st.scatter_chart(iris, x="{iris_x}", y="{iris_y}", size="{iris_size}"{', color="species"' if iris_color else ""})
    """
else:
    code = f"""
    st.scatter_chart(iris, x="{iris_x}", y="{iris_y}"{', color="species"' if iris_color else ""})
    """

st.markdown("#### :material/code_blocks: :blue[Source code to run]")

with st.container(border=True):
    st.code(code)



st.markdown("####  :material/scatter_plot: :red[Rendered output]") 

with st.container(border=True):
    if iris_color:
        st.scatter_chart(iris, x=iris_x, y=iris_y, size=iris_size, color="species",
                        width=720, height=500, use_container_width=False)
    else:
        st.scatter_chart(iris, x=iris_x, y=iris_y, size=iris_size, 
                         width=720, height=500, use_container_width=False)


with st.expander("Show documentation"):
    st.write(st.scatter_chart.__doc__)

st.divider()

st.markdown("### :material/dataset: Data to use")


code = """
import pandas as pd

tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
"""

with st.container():
    st.code(code)

tips = load_to_df('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

st.write(tips)

st.divider()

st.markdown("### :material/list_alt: [`st.bar_chart()`](https://docs.streamlit.io/develop/api-reference/charts/st.bar_chart)")

st.markdown("<br/>", unsafe_allow_html=True)


col3, col4 = st.columns(2)
tips_x = col3.selectbox("Choose variable for coordinate x", ["sex", "day", "smoker", "time"])
tips_y = col4.selectbox("Choose variable for coordinate y", ["total_bill", "tip", "size"])
tips_color = st.selectbox("Choose variable for color", ["sex", "day", "smoker", "time"], index=None)
tips_horizontal = st.checkbox("horizontal")


if tips_color:
    code = f"""
    st.bar_chart(tips, x="{tips_x}", y="{tips_y}", color="{tips_color}"{', horizontal=True' if tips_horizontal else ""})
    """
else:
    code = f"""
    st.bar_chart(tips, x="{tips_x}", y="{tips_y}"{', horizontal=True' if tips_horizontal else ""})
    """

st.markdown("#### :material/code_blocks: :blue[Source code to run]")

with st.container(border=True):
    st.code(code)

st.markdown("#### :material/bar_chart: :red[Rendered output]") 
with st.container(border=True):
    st.bar_chart(tips, x=tips_x, y=tips_y, color=tips_color, horizontal=tips_horizontal,
                 width=720, height=500, use_container_width=False)

with st.expander("Show documentation"):
    st.write(st.bar_chart.__doc__)


st.divider()

st.markdown("### :material/dataset: Data to use")


code = """
import pandas as pd

us_city_pop = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/2014_us_cities.csv")
"""

with st.container():
    st.code(code)

us_city_pop = load_to_df('https://raw.githubusercontent.com/plotly/datasets/master/2014_us_cities.csv')


st.write(us_city_pop)

st.divider()

us_city_pop["pop"] = us_city_pop["pop"] / 20

code = """
st.map(us_city_pop, latitude="lat", longitude="lon", size="pop")
"""

st.markdown("### :material/list_alt: [`st.map()`](https://docs.streamlit.io/develop/api-reference/charts/st.map)")

st.markdown("<br/>", unsafe_allow_html=True)

st.markdown("#### :material/code_blocks: :blue[Source code to run]")

with st.container(border=True):
    st.code(code)

st.markdown("#### :material/map: :red[Rendered output]") 

with st.container(border=True):
    st.map(us_city_pop, latitude="lat", longitude="lon", size="pop", zoom=4)


with st.expander("Show documentation"):
    st.write(st.map.__doc__)



