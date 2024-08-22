import streamlit as st

st.set_page_config(layout="wide")



with st.echo():
    import pandas as pd
    stocks = pd.read_csv('https://raw.githubusercontent.com/justinjiajia/datafiles/main/stocks_l.csv', 
                         parse_dates=['date'], date_format="%y/%m/%d")



st.write(stocks)


st.markdown("### [<code>st.line_chart</code>](https://docs.streamlit.io/develop/api-reference/charts/st.line_chart)", unsafe_allow_html=True)

code ="""
st.line_chart(data=stocks, x="date", y="return", color="symbol")
"""
with st.container(border=True):
    st.code(code)


st.markdown("#### :red[Rendered output]") 

with st.container(border=True):
    st.line_chart(data=stocks, x="date", y="return", color="symbol", 
                  width=600, height=500, use_container_width=False)




with st.expander("Show documentation"):
    st.write(st.line_chart.__doc__)


st.divider()

st.markdown("### [<code>st.area_chart</code>](https://docs.streamlit.io/develop/api-reference/charts/st.area_chart)", unsafe_allow_html=True)


code ="""
st.area_chart(data=stocks, x="date", y="return", color="symbol")
"""

with st.container(border=True):
    st.code(code)

st.markdown("#### :red[Rendered output]") 
with st.container(border=True):
    st.area_chart(data=stocks, x="date", y="return", color="symbol", 
                 width=600, height=500, use_container_width=False)


with st.expander("Show documentation"):
    st.write(st.area_chart.__doc__)

st.divider()


with st.echo():
    import pandas as pd
    iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

st.write(iris)



st.markdown("### [<code>st.scatter_chart</code>](https://docs.streamlit.io/develop/api-reference/charts/st.scatter_chart)", unsafe_allow_html=True)

col1, col2 = st.columns(2)

iris_x = col1.selectbox("Choose variable for coordinate x", ["sepal_length", "sepal_width", "petal_length", "petal_width"])
iris_y = col2.selectbox("Choose variable for coordinate y", ["sepal_length", "sepal_width", "petal_length", "petal_width"], index=1)
iris_size =  st.selectbox("Choose variable for size", ["sepal_length", "sepal_width", "petal_length", "petal_width"], 
                     index=None)
iris_color = st.checkbox("Use color to annotate species")

if iris_size:
    code = f"""
    st.scatter_chart(iris, x="{iris_x}", y="{iris_y}", size="{iris_size}"{', color="species"' if iris_color else ""})
    """
else:
    code = f"""
    st.scatter_chart(iris, x="{iris_x}", y="{iris_y}"{', color="species"' if iris_color else ""})
    """


with st.container(border=True):
    st.code(code)



st.markdown("#### :red[Rendered output]") 

with st.container(border=True):
    if iris_color:
        st.scatter_chart(iris, x=iris_x, y=iris_y, size=iris_size, color="species",
                        width=600, height=500, use_container_width=False)
    else:
        st.scatter_chart(iris, x=iris_x, y=iris_y, size=iris_size, 
                         width=600, height=500, use_container_width=False)


with st.expander("Show documentation"):
    st.write(st.scatter_chart.__doc__)

st.divider()

with st.echo():
    import pandas as pd
    tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')




st.write(tips)

st.markdown("### [<code>st.bar_chart</code>](https://docs.streamlit.io/develop/api-reference/charts/st.bar_chart)", unsafe_allow_html=True)

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


with st.container(border=True):
    st.code(code)

st.markdown("#### :red[Rendered output]") 
with st.container(border=True):
    st.bar_chart(tips, x=tips_x, y=tips_y, color=tips_color, horizontal=tips_horizontal,
                 width=600, height=500, use_container_width=False)

with st.expander("Show documentation"):
    st.write(st.bar_chart.__doc__)


st.divider()


with st.echo():
    import pandas as pd
    us_city_pop = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/2014_us_cities.csv")
    


st.write(us_city_pop)

us_city_pop["pop"] = us_city_pop["pop"] / 20

code = """
st.map(us_city_pop, latitude="lat", longitude="lon", size="pop")
"""
st.markdown("### [<code>st.map</code>](https://docs.streamlit.io/develop/api-reference/charts/st.map)", unsafe_allow_html=True)

with st.container(border=True):
    st.code(code)

st.markdown("#### :red[Rendered output]") 

with st.container(border=True):
    st.map(us_city_pop, latitude="lat", longitude="lon", size="pop", zoom=4)


with st.expander("Show documentation"):
    st.write(st.map.__doc__)



