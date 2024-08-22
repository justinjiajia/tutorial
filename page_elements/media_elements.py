import streamlit as st

st.set_page_config(layout="centered")

st.markdown("### [<code>st.image</code>](https://docs.streamlit.io/develop/api-reference/media/st.image)", unsafe_allow_html=True)

with st.container(border=True):
    with st.echo():
        st.image('https://geco.hkust.edu.hk/sites/default/files/images/School-of-Business-and-Management.png',
                 caption='SBM Logo', width=300)
        
with st.container(border=True):
    with st.echo():
        st.image("cat.jpg", width=400)

with st.container(border=True):
    with st.echo():
        st.image(["cat.jpg", "dog.jpg", "owl.jpg"], width=200)

with st.expander("Show documentation"):
    st.write(st.image.__doc__)

st.divider()

st.markdown("### [<code>st.video</code>](https://docs.streamlit.io/develop/api-reference/media/st.video)", unsafe_allow_html=True)

with st.container(border=True):
    with st.echo():
        st.video("https://www.youtube.com/watch?v=uEztHu4NHrs")

with st.container(border=True):
    with st.echo():
        st.video("https://cdn.openai.com/ctf-cdn/paper-planes.mp4", 
                 autoplay=True, muted=True)

with st.container(border=True):
    with st.echo():
        st.video("static/sora_gen.mp4", autoplay=True, muted=True, loop=True)

with st.expander("Show documentation"):
    st.write(st.video.__doc__)