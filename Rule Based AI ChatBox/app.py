import streamlit as st
from chatbot import get_response  # <-- IMPORT YOUR LOGIC HERE

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Chat Assistant",
    page_icon="💬",
    layout="centered"
)

# ---------------- SIMPLE PROFESSIONAL STYLE ----------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}

/* Chat message styling */
[data-testid="stChatMessage"] {
    background-color: #1c1f26;
    border-radius: 12px;
    padding: 10px;
    margin-bottom: 10px;
}

/* Input box fixed look */
.stChatInputContainer {
    position: fixed;
    bottom: 0;
    width: 100%;
    padding: 10px;
    background: #0e1117;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("💬 AI Chat Assistant")

# ---------------- MEMORY ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- SHOW CHAT HISTORY ----------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ---------------- USER INPUT ----------------
user_input = st.chat_input("Type your message...")

if user_input:
    # show user message
    st.chat_message("user").write(user_input)

    # save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # ---------------- BOT RESPONSE (USING YOUR chatbox.py) ----------------
    bot_response = get_response(user_input)  # <-- CALLING YOUR FUNCTION HERE

    # show bot message
    st.chat_message("assistant").write(bot_response)

    # save bot message
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_response
    })

# ---------------- CLEAR CHAT BUTTON ----------------
if st.sidebar.button("🧹 Clear Chat"):
    st.session_state.messages = []
    st.rerun()