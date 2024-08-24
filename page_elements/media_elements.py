import streamlit as st

st.set_page_config(layout="centered")

st.markdown("### :material/list_alt: [`st.image()`](https://docs.streamlit.io/develop/api-reference/media/st.image)")


with st.container(border=True):
    with st.echo():
        st.image('https://geco.hkust.edu.hk/sites/default/files/images/School-of-Business-and-Management.png',
                 caption='SBM Logo', width=300)
        
with st.container(border=True):
    with st.echo():
        st.image("static/cat.jpg", width=300)

with st.container(border=True):
    with st.echo():
        st.image(["static/cat.jpg", "static/dog.jpg", "static/owl.jpg"], width=200)

with st.expander("Show documentation"):
    st.write(st.image.__doc__)

st.divider()

st.markdown("### :material/list_alt: [`st.video()`](https://docs.streamlit.io/develop/api-reference/media/st.video)")


with st.container(border=True):
    with st.echo():
        st.video("https://www.youtube.com/watch?v=uEztHu4NHrs")

with st.container(border=True):
    with st.echo():
        st.video("https://cdn.openai.com/ctf-cdn/paper-planes.mp4", 
                 autoplay=True, muted=True)

with st.container(border=True):
    with st.echo():
        st.video("static/sora_gen.mp4", 
                 start_time="5s", end_time="17s",
                 autoplay=True, muted=True, loop=True)

with st.expander("Show documentation"):
    st.write(st.video.__doc__)