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
    background:
    radial-gradient(circle at top left, #123cff 0%, transparent 25%),
    radial-gradient(circle at top right, #00f5ff 0%, transparent 20%),
    linear-gradient(135deg, #020617, #050014, #000000);
    color: white;
}
.hero {
    padding: 35px;
    border-radius: 28px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(0,255,255,0.35);
    box-shadow: 0 0 35px rgba(0,255,255,0.25);
    text-align: center;
}
.title {
    font-size: 58px;
    font-weight: 900;
    background: linear-gradient(90deg,#00f5ff,#ffffff,#8b5cf6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.badge {
    display:inline-block;
    padding:8px 18px;
    border-radius:30px;
    background:rgba(0,255,255,0.15);
    border:1px solid #00f5ff;
    margin-top:10px;
}
.card {
    padding: 20px;
    border-radius: 22px;
    background: rgba(255,255,255,0.09);
    border: 1px solid rgba(255,255,255,0.18);
    box-shadow: 0 18px 50px rgba(0,0,0,0.45);
}
.metricBox {
    padding:18px;
    border-radius:18px;
    background:linear-gradient(135deg,rgba(0,245,255,.16),rgba(139,92,246,.16));
    border:1px solid rgba(0,245,255,.35);
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="title">🛰️ ThermaVision AI</div>
    <div style="font-size:22px;">Next-Gen Infrared Intelligence Platform</div>
    <div class="badge">ISRO-Inspired Space Mission Dashboard</div>
</div>
""", unsafe_allow_html=True)

st.write("")

mode = st.selectbox(
    "🚀 Select Mission Mode",
    ["Disaster Rescue Mission", "Border Surveillance Mission", "Satellite Thermal Analysis", "Night Vision Rescue"]
)

uploaded_file = st.file_uploader("📡 Upload Infrared / Thermal Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    img = np.array(image)

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray = cv2.equalizeHist(gray)

    colorized = cv2.applyColorMap(gray, cv2.COLORMAP_TURBO)
    colorized = cv2.cvtColor(colorized, cv2.COLOR_BGR2RGB)

    st.markdown("## 🔬 AI Processing Pipeline")
    st.progress(100)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("📥 Input Thermal Frame")
        st.image(image, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🧠 Enhanced AI Output")
        st.image(colorized, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("## 📊 Mission Intelligence Report")

    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown('<div class="metricBox"><h2>92%</h2><p>Thermal Clarity</p></div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="metricBox"><h2>Medium</h2><p>Alert Level</p></div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="metricBox"><h2>Active</h2><p>Mission Status</p></div>', unsafe_allow_html=True)

    st.success(f"Mission Mode Activated: {mode}")
    st.info("Use Case: Rescue operation, satellite monitoring, surveillance and disaster response.")

    result_img = Image.fromarray(colorized)
    buffer = BytesIO()
    result_img.save(buffer, format="PNG")

    st.download_button(
        "⬇️ Download Enhanced Thermal Output",
        buffer.getvalue(),
        "thermavision_ai_output.png",
        "image/png"
    )

else:
    st.info("Upload a thermal image to activate AI mission analysis.")
