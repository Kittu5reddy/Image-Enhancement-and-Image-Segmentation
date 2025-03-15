import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Streamlit App Title
st.title("🖼️ Image Enhancement & Segmentation using OpenCV")

# Upload Image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Convert image to OpenCV format
    image = Image.open(uploaded_file)
    image = np.array(image)
    
    if len(image.shape) == 3:  # Convert RGB to Grayscale if needed
        image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    else:
        image_gray = image

    st.subheader("Original Image")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Sidebar Options for Enhancement
    st.sidebar.header("Image Enhancement")
    enhance_option = st.sidebar.selectbox("Choose Enhancement", ["None", "Histogram Equalization", "CLAHE", "Sharpening"])

    # Enhancement Processing
    enhanced_image = image_gray.copy()
    if enhance_option == "Histogram Equalization":
        enhanced_image = cv2.equalizeHist(image_gray)
    elif enhance_option == "CLAHE":
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        enhanced_image = clahe.apply(image_gray)
    elif enhance_option == "Sharpening":
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        enhanced_image = cv2.filter2D(image_gray, -1, kernel)

    if enhance_option != "None":
        st.subheader(f"Enhanced Image - {enhance_option}")
        st.image(enhanced_image, caption=f"{enhance_option} Applied", use_column_width=True, channels="GRAY")

    # Sidebar Options for Segmentation
    st.sidebar.header("Image Segmentation")
    segment_option = st.sidebar.selectbox("Choose Segmentation", ["None", "Thresholding", "Canny Edge Detection"])

    # Segmentation Processing
    segmented_image = image_gray.copy()
    if segment_option == "Thresholding":
        _, segmented_image = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    elif segment_option == "Canny Edge Detection":
        segmented_image = cv2.Canny(image_gray, 100, 200)

    if segment_option != "None":
        st.subheader(f"Segmented Image - {segment_option}")
        st.image(segmented_image, caption=f"{segment_option} Applied", use_column_width=True, channels="GRAY")

