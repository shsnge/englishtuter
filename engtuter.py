import streamlit as st
import google.generativeai as genai

# --- Configure Gemini API ---
genai.configure(api_key="AIzaSyCM4vIdZylsML_EvYub0ky-ynPuJtYXvUE")  # apni API key yahan lagao

# --- System Instruction for English Teacher ---
system_instruction = """
You are a personal English teacher. 
You can:
- Teach grammar, vocabulary, and pronunciation
- Translate English words/sentences into Urdu
- Summarize English paragraphs
- Provide exercises, lesson plans, and corrections
- Answer questions about English literature, reading, and writing

If the user asks anything not related to English, 
politely decline with: 
"Sorry — I can only help with English language-related questions."
"""

# --- Chatbot Function ---
def english_teacher_chatbot(user_query):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(
        [system_instruction, f"User: {user_query}\nTeacher:"]
    )
    return response.text

# --- Streamlit UI ---
st.set_page_config(page_title="📘 Personal English Teacher", page_icon="📘")

st.title("📘 Your Personal English Teacher")
st.write("Ask me anything about English — grammar, vocabulary, translation, summaries, or exercises!")

# Input box
user_query = st.text_area("✍️ Enter your question:", height=100)

if st.button("Ask"):
    if user_query.strip():
        with st.spinner("Teacher is thinking..."):
            answer = english_teacher_chatbot(user_query)
        st.success(f"**Teacher:** {answer}")
    else:
        st.warning("Please enter a question before submitting.")
