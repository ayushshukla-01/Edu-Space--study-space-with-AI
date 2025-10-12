import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import streamlit as st
import requests
from io import BytesIO

# Load the trained .keras model
model = tf.keras.models.load_model('model/my_model.keras')

# Define class names (same order as your training folders)
class_names = ['cancer', 'capricorn', 
'leo']

# Image preprocessing function
def preprocess_image(img):
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def run_image_classifier():
    st.title("Edu-Space: Constellation Image Classifier")

    # Upload image from device
    uploaded_file = st.file_uploader("Upload a space image (JPG/PNG)", type=["jpg", "png"])

    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_container_width=True)

        img_array = preprocess_image(img)
        prediction = model.predict(img_array)
        predicted_class = class_names[np.argmax(prediction)]
        confidence = np.max(prediction)

        st.success(f"Prediction: **{predicted_class}** with {confidence:.2f} confidence")

        

    # Image URL upload
    image_url = st.text_input("Or paste an image URL:")
    if image_url:
        try:
            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))
            st.image(img, caption="Uploaded Image from URL", use_container_width=True)

            img_array = preprocess_image(img)
            prediction = model.predict(img_array)
            predicted_class = class_names[np.argmax(prediction)]
            confidence = np.max(prediction)

            st.success(f"Prediction: **{predicted_class}** with {confidence:.2f} confidence")

        except:
            st.error("Could not fetch or process image from URL.")

