# Space science education
 AI tools based Space science education
link for the app
https://edu-space--study-space-with-ai-vpjrdatfnrexyizk5sk8yg.streamlit.app/

🚀 Edu-Space: AI-Based Space Learning Platform

Edu-Space is an AI-powered educational platform designed to make learning astronomy interactive, fun, and accessible. It combines a multilingual chatbot with a constellation image classifier, allowing users to ask questions about space and identify constellations using images.

🌟 Key Features

AI Chatbot

Answers questions about space science using AI.

Supports 5 languages: English, Hindi, French, German, Spanish.

Accepts text input and speech input.

Provides answers using a combination of a knowledge base (space_facts.txt) and a Hugging Face QA model.
<img width="1000" height="1000" alt="Screenshot 2025-10-10 164904" src="https://github.com/user-attachments/assets/8fd9c7c0-6015-4e1d-a297-a2c5f067db5a" />

Constellation Image Classifier

Currently identifies 3 constellations: Leo, Cancer, Capricorn.

Accepts images uploaded from the device or via image URL in the browser.

Powered by a MobileNetV2 deep learning model.

Work in progress: More constellations will be added in future updates.

Multilingual Support & Translation

Answers can be translated into multiple languages using GoogleTranslator (deep-translator).

Interactive & Accessible UI

Web interface built with Streamlit.

Real-time responses for both chatbot and image classifier.

<img width="1000" height="1000" alt="Screenshot 2025-10-10 164918" src="https://github.com/user-attachments/assets/66dd60df-2d31-4c04-bbe0-8bda04b6f7cc" />


🧰 Tech Stack

Frontend / Web App: Streamlit

Deep Learning: TensorFlow, Keras, Hugging Face Transformers

Python Libraries: numpy, pillow, transformers, torch, deep-translator, pyttsx3, speech_recognition

Deployment: Streamlit Cloud

📂 Project Structure
Edu-Space/
│── app.py                # Main Streamlit app
│── chatbot.py            # Chatbot module
│── image_classifier.py   # Constellation classifier module
│── model/
│   └── my_model.keras    # Pre-trained MobileNetV2 model
│── space_facts.txt       # Knowledge base for chatbot
│── requirements.txt      # Python dependencies
│── README.md

🧪 Usage

Ask questions via text or speech.

Upload images of constellations from your device or using an image URL.

Get answers and predictions in real-time in your selected language.

🚀 Deployment

Can be deployed on Streamlit Cloud or other Python web hosting services.

Requires requirements.txt to install all dependencies.

🧭 Future Improvements

Add more constellations to the image classifier.

Expand chatbot knowledge base with additional astronomy content.

Include full voice-based interaction for chatbot (speech-to-text and text-to-speech).




🙌 License

MIT License — free to use, modify, and share.


