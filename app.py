from main import *  # Ensure 'main.py' exists and is needed
import streamlit as st
import matplotlib.pyplot as plt
import cv2 
import numpy as np

st.title("Enhancement Of Image")

# Read image using OpenCV (BGR format)
img = cv2.imread('./img/normal.png')

# Convert BGR to RGB
rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Show conversion code
code = """img = cv2.imread('./img/normal.png')
rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)"""
st.code(code, language="Python")

st.text("OpenCV follows BGR (Blue-Green-Red), so we need to convert it to RGB.")

# Display original and converted images side by side
col1, col2 = st.columns(2)
with col1:
    st.image(img, caption=f"BGR Image (Shape: {img.shape})", use_container_width=True)

with col2:
    st.image(rgb_image, caption=f"RGB Image (Shape: {rgb_image.shape})", use_container_width=True)

# Resize the image
resized_image = cv2.resize(rgb_image, (340, 340))

# Show resizing code
code = """resized_image = cv2.resize(rgb_image, (340, 340))"""
st.code(code, language="Python")

# Display resized image
st.image(resized_image, caption=f"Resized Image (Shape: {resized_image.shape})", width=500)

# Extract color channels
red_channel = resized_image[:, :, 0]
green_channel = resized_image[:, :, 1]
blue_channel = resized_image[:, :, 2]

st.title("__Split Image__")

# Display color channels in columns
col1, col2, col3 = st.columns(3)

with col1:
    st.image(red_channel, caption="Red Channel", use_container_width=True)

with col2:
    st.image(green_channel, caption="Green Channel", use_container_width=True)

with col3:
    st.image(blue_channel, caption="Blue Channel", use_container_width=True)
