import streamlit as st

# Page setup
st.set_page_config(page_title="Iron Lady Chatbot", page_icon="🤖", layout="centered")

# Sidebar Branding
st.sidebar.image("iron_lady_community_logo.jpeg", use_container_width=True)
st.sidebar.title("About Iron Lady")
st.sidebar.info(
    "Iron Lady offers leadership development programs for women professionals, "
    "focusing on career growth, leadership coaching, and skill-building workshops."
)

# Custom CSS for chat bubbles
st.markdown(
    """
    <style>
    .chat-bubble-user {
        background-color: #DCF8C6;
        padding: 10px;
        border-radius: 10px;
        margin: 5px;
        text-align: right;
    }
    .chat-bubble-bot {
        background-color: #E6E6E6;
        padding: 10px;
        border-radius: 10px;
        margin: 5px;
        text-align: left;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🤖 Iron Lady FAQ Chatbot")
st.write("Ask me about Iron Lady's leadership programs!")

# Hardcoded FAQ responses
faq_responses = {
    "programs": "Iron Lady offers leadership development programs for women professionals including leadership coaching, career growth, and skill-building workshops.",
    "duration": "The program duration varies between 6 weeks to 3 months depending on the course.",
    "online": "Most programs are conducted online, but some workshops may be offline at partner locations.",
    "certificate": "Yes, certificates are provided upon successful completion of the program.",
    "mentors": "The mentors and coaches are experienced leaders, corporate professionals, and certified leadership trainers associated with Iron Lady."
}

# Store chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Suggested Questions
st.subheader("💡 Suggested Questions")
col1, col2 = st.columns(2)
if col1.button("Programs Offered"):
    st.session_state.history.append(("user", "What programs does Iron Lady offer?"))
    st.session_state.history.append(("bot", faq_responses["programs"]))
if col2.button("Program Duration"):
    st.session_state.history.append(("user", "What is the program duration?"))
    st.session_state.history.append(("bot", faq_responses["duration"]))
if col1.button("Online or Offline?"):
    st.session_state.history.append(("user", "Is the program online or offline?"))
    st.session_state.history.append(("bot", faq_responses["online"]))
if col2.button("Certificates"):
    st.session_state.history.append(("user", "Are certificates provided?"))
    st.session_state.history.append(("bot", faq_responses["certificate"]))
if col1.button("Mentors"):
    st.session_state.history.append(("user", "Who are the mentors/coaches?"))
    st.session_state.history.append(("bot", faq_responses["mentors"]))

# User input box
user_input = st.text_input("You:", "")

if user_input:
    # Add user message
    st.session_state.history.append(("user", user_input))

    # Find bot response
    response = None
    for keyword, answer in faq_responses.items():
        if keyword in user_input.lower():
            response = answer
            break
    if not response:
        response = "🤖 I can answer FAQs about Iron Lady programs. Try asking about programs, duration, mode, certificates, or mentors."

    # Add bot message
    st.session_state.history.append(("bot", response))

# Clear chat button
if st.button("🗑️ Clear Chat"):
    st.session_state.history = []

# Display chat history
for sender, message in st.session_state.history:
    if sender == "user":
        st.markdown(f"<div class='chat-bubble-user'>👤 {message}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bubble-bot'>🤖 {message}</div>", unsafe_allow_html=True)
