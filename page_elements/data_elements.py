import streamlit as st

st.set_page_config(layout="wide")

st.markdown("### :material/dataset: Data to use")


with st.echo():
    import pandas as pd

    df = pd.DataFrame(
        {
            "name": ["Roadmap", "Extras", "Issues"],
            "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
            "likes": [842, 503, 938],
            "in_progress": [True, False, True]
        }
    )

    st.write(df)

st.divider()

st.markdown("### :material/list_alt: [`st.dataframe()`](https://docs.streamlit.io/develop/api-reference/data/st.dataframe)")

with st.container(border=True):
    with st.echo():
        st.dataframe(df)

with st.expander("Show documentation"):
    st.write(st.dataframe.__doc__)
    
st.divider()

st.markdown("### :material/list_alt: [`st.table()`](https://docs.streamlit.io/develop/api-reference/data/st.table)")

with st.container(border=True):
    with st.echo():
# display DataFrames in a static table
        st.table(df)

with st.expander("Show documentation"):
    st.write(st.table.__doc__)

st.divider()



st.markdown("### :material/list_alt: [`st.data_editor()`](https://docs.streamlit.io/develop/api-reference/data/st.data_editor)")

with st.container(border=True):
    with st.echo():
# display DataFrames in a static table
        st.data_editor(df, disabled=['url'])

with st.expander("Show documentation"):
    st.write(st.data_editor.__doc__)

st.divider()


st.markdown("### :material/dataset: Data to use")


with st.echo():
    import random
    import pandas as pd

    random.seed(125)
    df["views_history"] = [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)]
    
    st.dataframe(df)

st.divider()


st.markdown("### :material/list_alt: [`st.column_config()`](https://docs.streamlit.io/develop/api-reference/data/st.column_config)")


st.markdown("""The [`st.column_config` class](https://docs.streamlit.io/develop/api-reference/data/st.column_config) is a powerful tool for configuring data display and interaction.
It provides a suite of methods to tailor your columns to various data types, translating data into user-friendly formats or utilizing charts and progress bars for clearer data display.
""")


 # random.seed(125) below is critical; otherwise, every rerun generates a set of different values for the view_history_column
        # resulting in a complete redraw of the data editor table
        # no incremental change can be retained (e.g., uncheck a checkbox)
#       



with st.container(border=True):
    with st.echo():
        st.dataframe(
            df, 
            column_config={"name": "App name",
                           "url": st.column_config.LinkColumn("App URL"),
                           "likes": st.column_config.NumberColumn("Stars", format="%d ⭐"),
                           "views_history": st.column_config.BarChartColumn("Views", y_min=0, y_max=5000),
                           "in_progress": "In progress?"},
            hide_index=True,
            column_order=("name", "url", "views_history", "likes", "in_progress")
        )


with st.container(border=True):
    with st.echo():
        st.data_editor(
            df, 
            column_config={"name": "App name",
                           "url": st.column_config.LinkColumn("App URL", disabled=True),
                           "likes": st.column_config.ProgressColumn("Stars", max_value=1000, format="%d ⭐"),
                           "views_history": st.column_config.LineChartColumn("Views", y_min=0, y_max=5000),
                           "in_progress": st.column_config.SelectboxColumn("In progress?")}
        )


st.write([col for col in dir(st.column_config) if col.endswith("Column")])