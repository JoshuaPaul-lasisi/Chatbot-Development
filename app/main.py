import streamlit as st
import pickle
from scripts.response_generation import get_response
from scripts.data_preprocessing import clean_text

# Load the trained model and vectorizer
with open('../models/intent_classifier.pkl', 'rb') as f:
    model, vectorizer = pickle.load(f)

# Frontend design
st.markdown(
    """
    <link rel="stylesheet" href="./frontend/style.css">
    <div class="chatbox">
        <div class="chatbox-header">
            <h2>Customer Service Chatbot</h2>
        </div>
        <div class="chatbox-body" id="chat-body">
            <div class="message bot-message">Hi! How can I assist you today?</div>
        </div>
        <div class="chatbox-footer">
            <input type="text" id="user-input" placeholder="Type your message..." onkeypress="sendMessage(event)">
        </div>
    </div>
    <script src="./frontend/script.js"></script>
    """, unsafe_allow_html=True
)

def classify_and_respond(user_input):
    cleaned_input = clean_text(user_input)
    input_tfidf = vectorizer.transform([cleaned_input])
    predicted_intent = model.predict(input_tfidf)[0]
    response = get_response(predicted_intent)
    return response

# Handle user input from Streamlit
user_input = st.text_input("You: ")

if user_input:
    response = classify_and_respond(user_input)
    st.write(f"Bot: {response}")