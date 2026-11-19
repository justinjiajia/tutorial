import streamlit as st
import time
from openai import OpenAI

# --- 1. Setup & API Config ---
st.set_page_config(layout="wide", page_title="My Chatbot", page_icon="🤖")
st.header('🤖 💬 My Chatbot')

model = "deepseek/deepseek-v4-flash-0731"
apikey = "72c2c675ef7b47a0b3fb2f4932086bd6" # Replace with your actual API key
custom_headers = {"api-key": apikey}

client = OpenAI(
    base_url="https://hkust.azure-api.net/hkust-genai/v1",
    api_key=apikey,
    default_headers=custom_headers,
)

# --- 2. Modified Chatbot Logic ---
class Chatbot:
    def __init__(self, system_prompt="You are a friendly assistant.", max_turns=10):
        self.system_prompt = system_prompt
        self.max_turns = max_turns
        self.conversation = []

    def add_turn(self, role, content):
        self.conversation.append({"role": role, "content": content})
        return len(self.conversation) // 2

    def format_history(self):
        n_msgs = len(self.conversation)
        lines = [f"--- history ({n_msgs} messages stored) ---"]
        for i, turn in enumerate(self.conversation, start=1):
            lines.append(f"{i:2d}. {turn['role']:<9} | {turn['content']}")
        lines.append("---")
        return "\n".join(lines)

    def call_llm(self):
        messages = [{"role": "system", "content": self.system_prompt}]
        messages += self.conversation
        response = client.chat.completions.create(
            model=model,
            messages=messages,
        )
        return response.choices[0].message.content

    def handle_command(self, text):
        if not text.startswith(":"):
            return "message", None
        
        if text == ":history":
            return "handled", self.format_history()
        if text == ":clear":
            self.conversation = []
            return "handled", "Context cleared. Starting fresh."
        
        return "handled", f"Unknown command: '{text}'"

# --- 3. Streamlit State Management ---
# Initialize the bot once and store it in session_state
if "bot" not in st.session_state:
    st.session_state.bot = Chatbot()
    # Add initial greeting to UI
    st.session_state.bot.add_turn("assistant", "How may I assist you today?")

# --- 4. Render Chat History ---
for msg in st.session_state.bot.conversation:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# --- 5. User Input & Command Handling ---
if prompt := st.chat_input("Say something (or type :clear, :history)..."):
    
    # Check for commands first
    status, command_output = st.session_state.bot.handle_command(prompt)
    
    if status == "handled":
        # Display command output as a system info message
        st.info(command_output)
    elif status == "message":
        # It's a normal message, add user turn
        st.session_state.bot.add_turn("user", prompt)
        
        # Render user message immediately
        with st.chat_message("user"):
            st.write(prompt)

        # --- 6. Generate & Stream Response ---
        # Only generate if we haven't hit the max turns
        if len(st.session_state.bot.conversation) // 2 < st.session_state.bot.max_turns:
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    try:
                        reply = st.session_state.bot.call_llm()
                    except Exception as e:
                        st.error(f"API error: {e}")
                        reply = None
                
                if reply:
                    # Typing effect (using st.empty)
                    placeholder = st.empty()
                    full_response = ""
                    
                    # Split by characters for a smooth typing effect
                    for char in reply:
                        full_response += char
                        placeholder.markdown(full_response + "▌") # Add a cursor
                        time.sleep(0.01)
                    
                    # Final render without cursor
                    placeholder.markdown(full_response)
                    
                    # Save to history AFTER rendering
                    st.session_state.bot.add_turn("assistant", full_response)
        else:
            st.warning("You have reached the maximum number of questions. Please clear the history to continue.")