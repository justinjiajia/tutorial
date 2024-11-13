import streamlit as st

st.set_page_config(layout="wide")

with st.echo():
    import streamlit as st


with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>', unsafe_allow_html= True)


st.markdown("### :material/list_alt: [`st.write()`](https://docs.streamlit.io/develop/api-reference/write-magic/st.write)")


"""
This is the Swiss Army knife of Streamlit commands: it does different things depending on what you throw at it. 
"""

 
with st.container(border=True):
    with st.echo():
        passage = """
            Streamlit is an open-source Python framework for data scientists and AI/ML engineers to deliver interactive data apps – in only a few lines of code.
            """
        st.write(passage)
   
with st.container(border=True):
    with st.echo():
        import pandas as pd
        st.write(
            pd.DataFrame({"first column": [1, 2, 3], "second column": [10, 20, 30]}), 
            passage, 
            123
        )


with st.expander("Show documentation"):
    st.write(st.write.__doc__)


st.divider()


st.markdown("### :material/list_alt: [`st.markdown()`](https://docs.streamlit.io/develop/api-reference/text/st.markdown)")



with st.container(border=True):
    with st.echo():
        passage = """
            Streamlit's `.markdown()` function allows you to render [Markdown syntax](https://www.markdownguide.org/cheat-sheet/) 
            and display formatted text. 
        """
        st.markdown(passage)


with st.container(border=True):
    with st.echo():
        passage = """
            #### Markdown Examples

            | Element |    Markdown Syntax    |
            |-------- |-----------------------|
            | Heading | # H1 ; ## H2 ; ### H3 |
            | Bold    | \**bold text**        |
            | Italic  | \*italicized text*    |

            > Check out [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/) for a quick reference. 
        """
        st.markdown(passage)


"""###### Can show emojis"""

with st.container(border=True):
    with st.echo():
        st.markdown("a smiling face emoji 😊")        


"""###### Support emoji shortcodes"""

with st.container(border=True):
    with st.echo():
        st.markdown("e.g., :muscle:; a [list](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/) of supported codes")   


"""###### Support Google material symbols"""


with st.container(border=True):
    with st.echo():
        st.markdown("e.g., :material/shopping_cart_checkout:; a [list](https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded) of supported symbols")  

"""###### Support LaTeX expressions"""

with st.container(border=True):
    with st.echo():
        st.markdown("e.g., $\\beta$, $\\frac{1}{5}$, $x^2$; a [list](https://katex.org/docs/supported.html) of supported functions")  

"""###### Can decorate text with colors"""

with st.container(border=True):
    with st.echo():
        st.markdown("e.g., :orange[text to be colored], :rainbow-background[decorate text with a background color]")  
        st.markdown("All supported colors:  :blue[blue], :green[green], :orange[orange], :red[red], :violet[violet], :gray[gray], :rainbow[rainbow]")

"""###### Allow for HTML"""

with st.container(border=True):
    with st.echo():
        st.markdown("<a href='www.ust.hk'>HKUST</a><br/><br/>"
                    "<img src='https://brand.hkust.edu.hk/sites/default/files/2023-07/files/images/HKUST-Logo-Icon.svg'/>"
                    "<hr/>ISOM Department",
                    unsafe_allow_html=True)  


with st.expander("Show documentation"):
    st.write(st.markdown.__doc__)


st.divider()

st.markdown("### :material/list_alt: [`st.code()`](https://docs.streamlit.io/develop/api-reference/text/st.code)")


with st.container(border=True):
    with st.echo():
        st.code("sales_data = pd.read_csv('sales_data.csv')") # language defaults to Python; for syntax highlighting


code = """
html_source = '''<div>
    <a href="www.ust.hk">HKUST</a>
</div>
'''
st.code(html_source, language="html", line_numbers=True)
"""
with st.container(border=True):
    st.code(code)
    html_source = """<div>
    <a href="www.ust.hk">HKUST</a>
</div>"""
    st.code(html_source, language="html", line_numbers=True)


"Check out this [link](https://github.com/react-syntax-highlighter/react-syntax-highlighter/blob/master/AVAILABLE_LANGUAGES_PRISM.MD) for a list of available language values."


with st.expander("Show documentation"):
    st.write(st.code.__doc__)



st.divider()

st.markdown("### :material/list_alt: [`st.html()`](https://docs.streamlit.io/develop/api-reference/utilities/st.html)")

with st.container(border=True):
    with st.echo():
        st.html(
            "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>"
        )

with st.expander("Show documentation"):
    st.write(st.html.__doc__)



st.divider()

st.markdown("### :material/list_alt: [`st.divider()`](https://docs.streamlit.io/develop/api-reference/text/st.divider)")


with st.container(border=True):
    with st.echo():
        st.write("Display a horizontal bar:")
        st.divider()
        st.write("You can achieve the same effect with either:")
        st.write("---")
        st.write("or:")
        '---'
        

st.divider()

st.markdown("#### :material/list_alt: Other text elements")


with st.container(border=True):
    with st.echo():
        st.title("ISOM3400")

        st.header("Module 6: Streamlit")

        st.subheader("Setup Instructions")

        st.caption("This page illustrates various text and formatting commands availableis in Streamlit.")

        st.latex(r'''a + ar + a r^2 + \cdots + a r^{n-1} = a \left(\frac{1-r^{n}}{1-r}\right)''')








