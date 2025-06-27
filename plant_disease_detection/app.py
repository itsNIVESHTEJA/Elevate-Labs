import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
import gdown
import os

# Constants
IMG_SIZE = (128, 128)
CLASS_NAMES = ['Apple Black Rot', 'Apple Cedar Rust', 'Apple Scab', 'Apple Healthy']

MODEL_PATH = "plant_model_small.h5"

# Download the model from Google Drive if not present
if not os.path.exists(MODEL_PATH):
    file_id = "1_cQAi6fXzIrEBYIHhqYLQGGGkAcLL4sN"
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, MODEL_PATH, quiet=False)

# Load the model
model = load_model(MODEL_PATH)

# Streamlit UI
st.title(" Apple Leaf Disease Classifier")
st.markdown("Upload a leaf image to detect the disease.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Display image
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Preprocess
    image = image.resize(IMG_SIZE)
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array)[0]
    predicted_class = CLASS_NAMES[np.argmax(prediction)]
    confidence = np.max(prediction)

    # Display result
    st.success(f"Predicted Class: **{predicted_class}**")
    st.info(f"Confidence: **{confidence:.2%}**")


    # Result
    st.markdown(f"###  Prediction: **{predicted_class}**")
    st.markdown(f"###  Confidence: **{confidence * 100:.2f}%**")
