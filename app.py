
import streamlit as st
from chatbot import run_chatbot  # your updated chatbot.py file
from image_classifier import run_image_classifier  # assuming you have this
# from other_module import run_other_module  # add other modules if needed

# Sidebar navigation
st.sidebar.title("Edu-Space AI Navigation")
module = st.sidebar.radio(
    "Select a Module:",
    ["AI Chatbot", "Image Classifier"]
)

# Run selected module
if module == "AI Chatbot":
    run_chatbot()

elif module == "Image Classifier":
    run_image_classifier()

# You can add other elif blocks for additional modules
