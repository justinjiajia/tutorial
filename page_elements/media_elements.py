import streamlit as st

st.set_page_config(layout="centered")

 
st.markdown("### Image")

with st.container(border=True):
    with st.echo("below"):
        st.image('https://geco.hkust.edu.hk/sites/default/files/images/School-of-Business-and-Management.png',
                 caption='SBM Logo', width=300)
        
with st.container(border=True):
    with st.echo("below"):
        st.image("cat.jpg", width=200)

with st.container(border=True):
    with st.echo("below"):
        st.image(["cat.jpg", "dog.jpg", "owl.jpg"], width=200)

with st.expander("Show documentation"):
    st.write(st.image.__doc__)

st.divider()

st.markdown("### Video")

with st.container(border=True):
    with st.echo("below"):
        st.video("https://www.youtube.com/watch?v=uEztHu4NHrs")

with st.expander("Show documentation"):
    st.write(st.video.__doc__)