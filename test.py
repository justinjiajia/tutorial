import streamlit as st
import subprocess
import time

with st.form("code"):
    code = st.text_area("type in your code", height=200, key="code")
    submitted = st.form_submit_button("submit your code")


if submitted:
    with open("run.py", "w") as f:
        f.write(code)
    
    proc = subprocess.run(["python", "run.py"], capture_output=True, check=True)
    
    st.write(proc.stdout.decode("utf-8"))    

# https://realpython.com/python-subprocess/
# https://docs.python.org/3/library/subprocess.html#subprocess.run
# https://docs.python.org/3/library/io.html    