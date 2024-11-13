import sys
import streamlit as st

st.markdown("""
            ### A task that ensures you set up everything properly
            
            1. Launch ***Visual Studio Code***

            2. Create a new project

                - Choose <kbd>File</kbd> → <kbd>Open Folder...</kbd>;
            
                - Navigate to a proper folder (perhaps the folder you use to save your class materials) and create a new folder within it (suggested name: *streamlit_project*);
            
                - **❗Important**: Click to open the new folder and choose <kbd>Select Folder</kbd>;
            
                - Download [*translator_app.py*](https://canvas.ust.hk/courses/58723/files/9731498) from Canvas;
            
                - Put the *.py* file into the folder you just created;
            
                - Click to open the file from the Explorer panel
            
            3. Ensure a Python interpreter to be selected

               - You should see **3.XX.X('base':conda)** at the right corner of the status bar;
            
               - If you see a "Select Interpreter" warning as follows <br/><br/>
                 <img src="https://code.visualstudio.com/assets/docs/python/environments/no-interpreter-selected-statusbar.png" width="300" /> <br/><br/>
                 click it and select the interpreter shipped with Anaconda (path: *~\\anaconda3\\python.exe*) from the Command Palette that appears at the top;
             
               - If you want to use a different interpreter, type <kbd>></kbd> in the search bar at the top and choose **Python: Select Interpreter** from the dropdown menu
            
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

                - Download [*setup_manual.py*](https://canvas.ust.hk/courses/58723/files/9739042) from Canvas;
            
                - Put it into your project folder;
            
                - Create a new Terminal session
                  
                  - Approach 1: Choose <kbd>Terminal</kbd> →  <kbd>New Terminal</kbd>
            
                  - Approach 2: Choose a shell from the popped menu (Windows users: PowerShell or Command Prompt; Mac users: Git Bash)
                  
                    <img src="https://code.visualstudio.com/assets/docs/terminal/basics/select-profile-dropdown.png" width=500/><br/>
            
                - Run 
            
                  ```systmd
                  streamlit run setup_manual.py --server.port 8502
                  ```
            
            """, unsafe_allow_html=True)


st.divider()

st.markdown("""
### References

- [Visual Studio Code User Interface](https://code.visualstudio.com/docs/getstarted/userinterface)
            
- [Python in Visual Studio Code](https://code.visualstudio.com/docs/languages/python)
            
- [Streamlit online documentation](https://docs.streamlit.io/)
            
""")

