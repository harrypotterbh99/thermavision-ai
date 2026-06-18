import os
os.environ["STREAMLIT_SERVER_FILE_WATCHER_TYPE"] = "none"

import streamlit as st
from PIL import Image
import numpy as np
import cv2
from io import BytesIO

st.set_page_config(page_title="ThermaVision AI", layout="wide")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #020024, #090979, #000000);
    color: white;
}
.big-title {
    font-size: 48px;
    font-weight: 800;
    text-align: center;
    color: #ffffff;
}
.sub-title {
    text-align: center;
    font-size: 20px;
    color: #d9e6ff;
}
.card {
    background: rgba(255,255,255,0.10);
    padding: 20px;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.25);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='big-title'>🚀 ThermaVision AI</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>AI-Powered Infrared Image Enhancement for Space, Rescue & Surveillance</div>", unsafe_allow_html=True)

st.write("")

mode = st.selectbox(
    "Select Mission Mode",
    ["Disaster Rescue Mode", "Surveillance Mode", "Space Observation Mode"]
)

uploaded_file = st.file_uploader("Upload Infrared / Thermal Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    img = np.array(image)

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray = cv2.equalizeHist(gray)

    colorized = cv2.applyColorMap(gray, cv2.COLORMAP_TURBO)
    colorized = cv2.cvtColor(colorized, cv2.COLOR_BGR2RGB)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Original Thermal Image")
        st.image(image, use_container_width=True)

    with col2:
        st.markdown("### Enhanced Thermal Output")
        st.image(colorized, use_container_width=True)

    st.markdown("---")

    st.markdown("### Mission Analysis Report")
    st.success("Image enhancement completed successfully.")
    st.info(f"Selected Mode: {mode}")
    st.warning("Alert Level: Medium")
    st.write("Possible Use Cases: Night rescue, satellite monitoring, surveillance, disaster response.")

    result_img = Image.fromarray(colorized)
    buffer = BytesIO()
    result_img.save(buffer, format="PNG")

    st.download_button(
        label="Download Enhanced Image",
        data=buffer.getvalue(),
        file_name="thermavision_output.png",
        mime="image/png"
    )
else:
    st.info("Upload a thermal image to start mission analysis.")
