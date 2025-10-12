from transformers import pipeline
from deep_translator import GoogleTranslator
import pyttsx3
import speech_recognition as sr
import streamlit as st

# Load facts from text file
def load_facts(file_path):
    facts = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if ':' in line:
                key, value = line.strip().split(':', 1)
                facts[key.lower()] = value.strip()
    return facts

# Load your facts file (make sure it's in the same folder)
space_facts = load_facts("space_facts.txt")

# QA Pipeline from Huggingface (RoBERTa)
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

# Text-to-speech setup
engine = pyttsx3.init()


def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except RuntimeError:
        pass  # avoid double run loop error if speaking already in progress

    # Text-to-speech setup (initialize once using session state)
if 'engine' not in st.session_state:
    st.session_state.engine = pyttsx3.init()

def speak(text):
    try:
        st.session_state.engine.say(text)
        st.session_state.engine.runAndWait()
    except RuntimeError:
        pass


# Speech recognition setup
recognizer = sr.Recognizer()

def run_chatbot():
    st.title("🚀 Edu-Space AI Chatbot")
    language = st.selectbox("Choose language:", ["English", "Hindi", "French", "German", "Spanish"])
    input_mode = st.radio("Select Input Mode:", ("Text", "Speech"))

    user_input = ""

    if input_mode == "Text":
        user_input = st.text_input("Ask your question here:")
    else:
        if st.button("Start Listening"):
            with sr.Microphone() as source:
                st.info("Listening...")
                audio = recognizer.listen(source)
            try:
                user_input = recognizer.recognize_google(audio)
                st.success(f"You said: {user_input}")
            except:
                st.error("Sorry, couldn't recognize.")

    if user_input:
        lower_input = user_input.lower()

        # 1️⃣ Check in space facts first
        response = None
        for key in space_facts:
            if key in lower_input:
                response = space_facts[key]
                break

        # 2️⃣ If no fact found, use QA pipeline
        if not response:
            context_text = "\n".join(space_facts.values())  # combine all facts as context
            result = qa_pipeline(question=user_input, context=context_text)
            response = result['answer'] if result['answer'] else "Sorry, I don't have information about that."

        # 3️⃣ Translate if needed
        if language != "English":
            lang_map = {"Hindi": "hi", "French": "fr", "German": "de", "Spanish": "es"}
            response = GoogleTranslator(source='en', target=lang_map[language]).translate(response)

        # 4️⃣ Show text reply
        st.success(response)

        # 5️⃣ Speak the answer
        speak(response)

if __name__ == "__main__":
    run_chatbot()
