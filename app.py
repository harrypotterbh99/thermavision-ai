import os
os.environ["STREAMLIT_SERVER_FILE_WATCHER_TYPE"] = "none"

import streamlit as st
from PIL import Image
import numpy as np
import cv2

st.title("ThermaVision AI")

uploaded_file = st.file_uploader(
    "Upload Thermal Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.subheader("Original Image")
    st.image(image)

    img_np = np.array(image)

    gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
    colorized = cv2.applyColorMap(gray, cv2.COLORMAP_JET)

    st.subheader("Colorized Image")
    st.image(colorized)

    st.success("Image processed successfully!")
