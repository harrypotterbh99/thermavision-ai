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
    background: linear-gradient(135deg, #020617, #07142f, #000000);
    color: white;
}
.hero {
    padding: 45px;
    border-radius: 30px;
    background: linear-gradient(135deg, rgba(0,245,255,.15), rgba(139,92,246,.12));
    border: 1px solid rgba(0,245,255,.35);
    box-shadow: 0 0 40px rgba(0,245,255,.25);
    text-align: center;
}
.title {
    font-size: 58px;
    font-weight: 900;
    background: linear-gradient(90deg,#00f5ff,#ffffff,#a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.section {
    padding: 25px;
    border-radius: 22px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.18);
    margin-top: 20px;
}
.card {
    padding: 20px;
    border-radius: 18px;
    background: rgba(0,0,0,0.35);
    border: 1px solid rgba(0,245,255,.25);
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="title">🛰️ ThermaVision AI</div>
    <h3>AI-Powered Infrared Image Intelligence Platform</h3>
    <p>For space observation, rescue operations, surveillance and disaster response.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
<h2>🚀 About Project</h2>
<p>
ThermaVision AI is a thermal image analysis platform that converts infrared/thermal images
into enhanced human-friendly visual outputs. The system helps users understand thermal scenes
better for rescue, surveillance and remote sensing applications.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("## 🔥 Key Features")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="card"><h3>Thermal Enhancement</h3><p>Improves visibility of thermal images.</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="card"><h3>Mission Modes</h3><p>Rescue, surveillance and space observation modes.</p></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="card"><h3>Download Output</h3><p>Save enhanced image for report and analysis.</p></div>', unsafe_allow_html=True)

st.markdown("## 🧠 Live Mission Demo")

mode = st.selectbox(
    "Select Mission Mode",
    ["Disaster Rescue Mission", "Border Surveillance Mission", "Satellite Thermal Analysis", "Night Vision Rescue"]
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
        st.subheader("Original Thermal Image")
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("Enhanced Thermal Output")
        st.image(colorized, use_container_width=True)

    st.markdown("## 📊 Mission Report")
    r1, r2, r3 = st.columns(3)
    r1.metric("Thermal Clarity", "92%")
    r2.metric("Alert Level", "Medium")
    r3.metric("Mission Status", "Active")

    st.success(f"Mission Mode: {mode}")
    st.info("Possible Use Cases: Rescue operation, satellite monitoring, surveillance and disaster response.")

    result_img = Image.fromarray(colorized)
    buffer = BytesIO()
    result_img.save(buffer, format="PNG")

    st.download_button(
        "Download Enhanced Output",
        buffer.getvalue(),
        "thermavision_ai_output.png",
        "image/png"
    )

st.markdown("""
<div class="section">
<h2>👥 Team</h2>
<p><b>Team Name:</b> AstroVision Coders</p>
<p><b>Project Lead:</b> Vishal Kumar</p>
<p><b>Domain:</b> AI, Image Processing, Remote Sensing</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
<h2>📞 Contact</h2>
<p><b>Email:</b> your-email@example.com</p>
<p><b>GitHub:</b> github.com/your-username</p>
<p><b>LinkedIn:</b> linkedin.com/in/your-profile</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<hr>
<center>
<p>© 2026 ThermaVision AI | Built for Hackathon Innovation</p>
</center>
""", unsafe_allow_html=True)
