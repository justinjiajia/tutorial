import streamlit as st


st.set_page_config(layout="centered")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>', unsafe_allow_html= True)

st.markdown("""
            ### A task that ensures you set up everything properly
            
            1. Launch ***Visual Studio Code***

            2. Create a new project

                - Choose <kbd>File</kbd> → <kbd>Open Folder...</kbd>;
            
                - Navigate to a proper folder (perhaps the folder you use to save your class materials) and create a new folder within it (suggested name: *streamlit_project*);
            
                - **❗Important**
            
                    - On Windows, click to open the new folder and choose <kbd>Select Folder</kbd>;
            
                    - On Mac computers, since you are already inside the new folder, simply click <kbd>Open</kbd>;
            
                - Download *translator_app.py* from Canvas;
            
                - Put the *.py* file into the folder you just created;
            
                - Click to open the file from the Explorer panel
            
            3. Make sure to select the correct Python interpreter

               - Make sure the Python extension is installed in your VS Code;
                 <br/>

                 <img src="https://raw.githubusercontent.com/justinjiajia/img/master/python/python_extension.png" width="300" /> 
                 <br/>

               - Type <kbd>></kbd> in the search bar at the top and choose **Python: Select Interpreter** from the dropdown menu;
               
               - Select the interpreter that comes bundled with Anaconda from the Command Palette;
                  - Something starting with "Python 3.XX.XX ('base') *~\\<some path>\\anaconda3\\python.exe*"
            
 
            
            4. Use system commands

               - Choose <kbd>View</kbd> → <kbd>Terminal</kbd> to show the Terminal window where you can issue system commands;
               
               - Run 
                 ```systemd
                 pip install googletrans-py -q
                 ```
                 in the Terminal window if you didn't install this Python library from Module 4
            
            5. Launch the app

               - Run 
                 ```systmd
                 streamlit run translator_app.py
                 ```
                 from the Terminal window to launch the app;
              
               - A new browser tab will be opened to render the app.
            
             6. Launch multiple apps
            
                - ***localhost:8501*** showing in the browser's location bar means the launched app is running on your local computer at port 8501.
              
                - You can run as many apps as you want simultaneously. But they must use different ports. 

                - Download *setup_manual.py* from Canvas;
            
                - Put it into your project folder;
            
                - Create a new Terminal session
                  
                  - Approach 1: Choose <kbd>Terminal</kbd> →  <kbd>New Terminal</kbd>
            
                  - Approach 2: Choose a shell from the popped menu (Windows users: PowerShell or Command Prompt; Mac users: zsh)
                  
                    <img src="https://code.visualstudio.com/assets/docs/terminal/basics/select-profile-dropdown.png" width=500/><br/>
            
                - Run 
            
                  ```systmd
                  streamlit run setup_manual.py --server.port 8502
                  ```
            
            7. Stop a running app

                - Switch to the terminal session where the app is running
            
                - Press <kbd>Ctrl + C</kbd> on Windows or  <kbd>Control + C</kbd> on Mac computers

            """, unsafe_allow_html=True)


st.divider()

st.markdown("""

### How to save a page as a PDF
            
<img src="https://raw.githubusercontent.com/justinjiajia/img/refs/heads/master/python/streamlit_pdf.png" width=200 />            
            
""", unsafe_allow_html=True
)            


st.divider()

st.markdown("""

### Access the source code
            
If you have a GitHub account, you can fork this [repository](https://github.com/justinjiajia/tutorial), which contains all source code for this tutorial website.
            
    
"""
)   

st.divider()



st.markdown("""
### References

- [Visual Studio Code User Interface](https://code.visualstudio.com/docs/getstarted/userinterface)
            
- [Python in Visual Studio Code](https://code.visualstudio.com/docs/languages/python)
            
- [Streamlit online documentation](https://docs.streamlit.io/)
            
""")

