import streamlit as st
from utils import chat_with_model
from prompts import greeting_prompt, info_collection_prompt, tech_question_prompt

st.set_page_config(page_title="TalentScout Hiring Assistant", page_icon="💼")

st.title("💼 TalentScout Hiring Assistant")
st.markdown("Welcome to TalentScout! I’ll guide you through the initial interview process.")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []  # only visible messages
    st.session_state.step = "greeting"
    st.session_state.candidate_info = {}

    # Initial assistant message (not system prompt)
    st.session_state.messages.append({
        "role": "assistant",
        "content": (
            "👋 Hi! I'm **TalentScout**, your hiring assistant.\n\n"
            "I’ll collect some details to help with your initial screening. "
            "Type 'exit' anytime to end the chat."
        )
    })

# Display chat history (in order)
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# Handle user input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Exit conditions
    if user_input.lower() in ["exit", "quit", "bye"]:
        st.chat_message("assistant").markdown(
            "Thank you for chatting with TalentScout! We'll reach out soon. 👋"
        )
        st.stop()

    # Add and display user message
    user_msg = {"role": "user", "content": user_input}
    st.session_state.messages.append(user_msg)
    st.chat_message("user").markdown(user_input)

    # Conversation flow logic
    
    assistant_reply = ""
    response = None

    if st.session_state.step == "greeting":
        response = chat_with_model([
            {"role": "system", "content": greeting_prompt()},
            {"role": "user", "content": user_input}
        ])
        st.session_state.step = "collect_info"
        assistant_reply = (
            "Great! Let's start by collecting some details.\n\n"
            "Could you please share your **name**, **email**, and **tech stack** (languages, frameworks, tools)?"
        )

    elif st.session_state.step == "collect_info":
        st.session_state.candidate_info["raw_input"] = user_input
        if "tech" in user_input.lower() or "stack" in user_input.lower():
            tech_stack = user_input
            assistant_reply = f"Got it! Generating interview questions for **{tech_stack}**..."
            st.session_state.step = "questions"

            # Hidden system prompt (not visible to user)
            response = chat_with_model([
                {"role": "system", "content": tech_question_prompt(tech_stack)}
            ])
        else:
            assistant_reply = (
                "Please provide your full tech stack — e.g., Python, Django, React, MySQL."
            )

    elif st.session_state.step == "questions":
        assistant_reply = "That concludes your initial screening. Thank you for your time!"

    # Combine assistant response + model output
    if response:
        assistant_reply += "\n\n" + response

    # Add and show assistant message
    assistant_msg = {"role": "assistant", "content": assistant_reply}
    st.session_state.messages.append(assistant_msg)
    st.chat_message("assistant").markdown(assistant_reply)
