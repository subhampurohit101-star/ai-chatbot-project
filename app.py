import streamlit as st
from transformers import pipeline

# Load free chatbot model
chatbot = pipeline(
    "text-generation",
    model="gpt2"
)

# Page settings
st.set_page_config(
    page_title="Free AI Chatbot",
    page_icon="🤖"
)

# Title
st.title("🤖 Free AI Chatbot")
st.write("AI chatbot without OpenAI payment")

# User input
user_input = st.text_input("Enter your message:")

# Button
if st.button("Send"):

    if user_input.strip() != "":

        with st.spinner("Generating response..."):

            response = chatbot(
                user_input,
                max_length=100,
                num_return_sequences=1
            )

            answer = response[0]["generated_text"]

            st.success("Response Generated!")

            st.write("### 🤖 Chatbot:")
            st.write(answer)

    else:
        st.warning("Please enter a message.")