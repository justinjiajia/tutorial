import streamlit as st
import time

st.set_page_config(layout="wide")

# Assuming you have a static/font.css file. If not, you can remove this block.
try:
    with open( "static/font.css" ) as css:
        st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
except FileNotFoundError:
    pass
    
st.markdown("""
<style>
[data-testid=stExpander] summary p {
    font-size: 20px;
    font-weight: bold;
    color: salmon;
}
</style>
""", unsafe_allow_html=True)

if "messages_1" not in st.session_state.keys():
    st.session_state.messages_1 = [{"role": "assistant", "content": "How may I assist you today?"}]


if "messages_2" not in st.session_state.keys():
    st.session_state.messages_2 = [{"role": "assistant", "content": "How may I assist you today?"}]

if "messages_3" not in st.session_state.keys():
    st.session_state.messages_3 = [{"role": "assistant", "content": "How may I assist you today?"}]

st.markdown("### :rainbow[Creating a Chat UI Using Streamlit's Built-in Chat Elements]")


# ==========================================
# SECTION 1: Chat Input
# ==========================================
st.markdown("#### 1. The Entry Point: `st.chat_input()`")
st.markdown("""
`st.chat_input` renders as a modern messaging box with a send arrow, instantly signaling to the user that this is a conversational interface. 


Different from a simple combination of a text input and a button, it natively handles the submission action and styling as a single cohesive widget. 

When used in the main body of an app, it docks to the bottom of the viewport, ensuring the user never has to scroll to find the input box as the chat history grows.
""")

code_1 = """
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

for msg in st.session_state.messages:
    st.write(msg["content"])

prompt = st.chat_input("Say something")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append({"role": "assistant", "content": f"Echo: {prompt}"})

    # Rerun explicitly to display the new messages
    st.rerun()  """

st.markdown("#### :material/code_blocks: :blue[Source code to run]")
with st.container(border=True):
    st.code(code_1, language="python")

st.markdown("#### :material/widgets: :red[Rendered output]")
 


with st.container(border=True):
    
    # 2. Render messages FIRST
    for msg in st.session_state.messages_1:
        st.write(msg["content"])

    # 3. Render input LAST (It will sink to the bottom of the container)
    prompt_1 = st.chat_input("Say something", key="prompt_1")
    if prompt_1:
        st.session_state.messages_1.append({"role": "user", "content": prompt_1})
        st.session_state.messages_1.append({"role": "assistant", "content": f"Echo: {prompt_1}"})
        st.rerun()

st.divider()


# ==========================================
# SECTION 2: Chat Message
# ==========================================
st.markdown("#### 2. The UI: `st.chat_message()`")
st.markdown("""
Right now, the output is just plain text. To make it look like a real chat application, we use **`st.chat_message()`**. 

- This is a layout container that automatically styles its contents into a chat bubble with an avatar.
- We pass a string like `"user"` or `"assistant"` to tell it which type of bubble to render.
""")

code_2 = """if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

prompt = st.chat_input("Say something")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append({"role": "assistant", "content": f"Echo: {prompt}"})

    # Rerun the app to display the new messages
    st.rerun()"""

st.markdown("#### :material/code_blocks: :blue[Source code to run]")

with st.container(border=True):
    st.code(code_2, language="python")

st.markdown("#### :material/widgets: :red[Rendered output]")

with st.container(border=True):

    for msg in st.session_state.messages_2:
        st.chat_message(msg["role"]).write(msg["content"])
    
    prompt_2 = st.chat_input("Say something", key="prompt_2")
    if prompt_2:
        st.session_state.messages_2.append({"role": "user", "content": prompt_2})
        st.session_state.messages_2.append({"role": "assistant", "content": f"Echo: {prompt_2}"})

        # Rerun explicitly to display the new messages
        st.rerun()

st.divider()


# ==========================================
# SECTION 3: Spinner
# ==========================================
st.markdown("#### 3. Adding Realism: `st.spinner()`")
st.markdown("""
In reality, AI doesn't respond instantly. To show the user that the system is working, we use **`st.spinner()`**.

- This is a context manager (`with` block) that displays a loading animation.
- Place it *inside* the assistant's chat bubble. While the code inside the block runs (e.g., waiting for an API), the spinner shows.
""")

code_3 = """import time

if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

prompt = st.chat_input("Say something")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            time.sleep(1.5)
    
    st.session_state.messages.append({"role": "assistant", "content": f"Echo: {prompt}"})

    # Rerun explicitly to display the new messages
    st.rerun()"""

st.markdown("#### :material/code_blocks: :blue[Source code to run]")

with st.container(border=True):
    st.code(code_3, language="python")

st.markdown("#### :material/widgets: :red[Rendered output]")


with st.container(border=True):

    for msg in st.session_state.messages_3:
        st.chat_message(msg["role"]).write(msg["content"])
    
    prompt_3 = st.chat_input("Say something", key="prompt_3")

    if prompt_3:
        st.session_state.messages_3.append({"role": "user", "content": prompt_3})
        with st.chat_message("user"):
            st.write(prompt_3)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                time.sleep(1.5)

        st.session_state.messages_3.append({"role": "assistant", "content": f"Echo: {prompt_3}"})

        # Rerun explicitly to display the new messages
        st.rerun()


 
st.divider()


# ==========================================
# SECTION 4: Empty & Streaming
# ==========================================
st.markdown("#### 4. The Typing Effect: `st.empty()`")
st.markdown("""
The final touch is the "streaming" effect, where the text types itself out. To do this, we use **`st.empty()`**.

- Normally, Streamlit appends elements top-to-bottom. `st.empty()` creates a placeholder that acts like a magic window.
- You can repeatedly overwrite what's inside this placeholder. By looping through words and updating the placeholder, it looks like the text is being typed live.
""")

code_4 = """with st.chat_message("assistant"):
    placeholder = st.empty()
    full_response = ""
    
    for word in "This is a simulated response. I am typing this out word by word!".split():
        full_response += word + " "
        time.sleep(0.15)
        placeholder.markdown(full_response)"""

st.markdown("#### :material/code_blocks: :blue[Source code to run]")
with st.container(border=True):
    st.code(code_4, language="python")

st.markdown("#### :material/widgets: :red[Rendered output]")
with st.container(border=True):
    if st.button("Show me the typing effect", key="sim4"):
        with st.chat_message("assistant"):
            placeholder = st.empty()
            full_response = ""
            
            for word in "This is a simulated response. I am typing this out word by word!".split():
                full_response += word + " "
                time.sleep(0.15)
                placeholder.markdown(full_response)



st.divider()


# ==========================================
# FULL CODE AT THE END
# ==========================================
st.markdown("### :rainbow[The Complete Code]")
st.markdown("Here is how all four steps combine into a single, realistic chatbot interface:")

full_code = """
import streamlit as st
import time

# 1. Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# 2. Display chat messages from history on app rerun
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# 3. Accept user input
prompt = st.chat_input("Say something")

if prompt:
    # Display and store user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Display assistant response with spinner and typing effect
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            time.sleep(1.5) # Simulate processing delay
        
        # Setup for streaming effect
        placeholder = st.empty()
        full_response = ""
        
        # Combine the echo logic with the typing effect text
        response_text = f"I am typing my response out word by word: {prompt}"
        
        for word in response_text.split():
            full_response += word + " "
            time.sleep(0.15)
            placeholder.markdown(full_response)
            
    # Note: No st.rerun() is needed here because we've already displayed it!
    st.session_state.messages.append({"role": "assistant", "content": full_response})
"""

st.markdown("#### :material/code_blocks: :blue[Source code to run]")
with st.container(border=True):
    st.code(full_code, language="python")