import streamlit as st
from ollama_utils import list_ollama_models, chat_with_model
from canvas_template import generate_canvas_quiz_file

st.set_page_config(page_title="Canvas Quiz Generator with Local AI", layout="wide")
st.title("Canvas Quiz Generator (Local LLM via Ollama)")

# Sidebar: Model selection
models = list_ollama_models()
selected_model = st.sidebar.selectbox("Select LLM Model", models)

# Chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Chat input
user_input = st.text_input("Enter your quiz request:", "Create a 5-question multiple choice quiz on photosynthesis.")
if st.button("Send"):
    if user_input:
        st.session_state["chat_history"].append({"role": "user", "content": user_input})
        response = chat_with_model(selected_model, st.session_state["chat_history"])
        st.session_state["chat_history"].append({"role": "assistant", "content": response})

# Display chat
for msg in st.session_state["chat_history"]:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**AI:** {msg['content']}")

# Generate and download quiz file
if st.session_state["chat_history"]:
    last_ai_msg = next((m["content"] for m in reversed(st.session_state["chat_history"]) if m["role"] == "assistant"), None)
    if last_ai_msg:
        quiz_file = generate_canvas_quiz_file(last_ai_msg)
        st.download_button("Download Canvas Quiz File", quiz_file, file_name="canvas_quiz.csv")
