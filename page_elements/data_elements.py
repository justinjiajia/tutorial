import streamlit as st

st.set_page_config(layout="wide")

with st.container(border=True):
    with st.echo():
        import pandas as pd
        df = pd.DataFrame(
            {
                "name": ["Roadmap", "Extras", "Issues"],
                "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
                "stars": [842, 503, 1016],
                "in_progress": [True, False, True]
            }
        )

with st.container(border=True):
    with st.echo():
        st.write(df)

with st.container(border=True):
    with st.echo():
        st.dataframe(df)

with st.expander("Show documentation"):
    st.write(st.dataframe.__doc__)
    
with st.container(border=True):
    with st.echo():
# display DataFrames in a static table
        st.table(df)

st.divider()

st.markdown("We can customize the way to display a DataFrame via `column_config`, `hide_index`, or `column_order`:")

st.markdown("""When working with data in Streamlit, the `st.column_config` class, specifically designed for the `column_config` parameter, is a powerful tool for configuring data display and interaction.
It provides a suite of methods to tailor your columns to various data types - from simple text and numbers to lists, URLs, images, and more.
""")

with st.container(border=True):
    with st.echo():
        import random
        import pandas as pd

        df = pd.DataFrame(
            {
                "name": ["Roadmap", "Extras", "Issues"],
                "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
                "stars": [842, 503, 1016],
                "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
                "in_progress": [True, False, True]
            }
        )
        st.dataframe(df)

with st.container(border=True):
    with st.echo():
        st.dataframe(
            df, 
            column_config={"name": "App name",
                        "url": st.column_config.LinkColumn("App URL"),
                        "stars": st.column_config.NumberColumn("Stars",
                                                                help="Number of stars on GitHub",
                                                                format="%d ⭐"),
                        "views_history": st.column_config.LineChartColumn("Views", y_min=0, y_max=5000, 
                                                                            help="Number of views in the past 30 days"),
                        "in_progress": st.column_config.CheckboxColumn("In progress?", help="Is the development is still in progress?")
                        },
            hide_index=True,
            column_order=("name", "url", "views_history", "stars", "in_progress")
        )
