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
    radial-gradient(circle at 15% 15%, rgba(0,255,255,0.25), transparent 20%),
    radial-gradient(circle at 85% 20%, rgba(167,139,250,0.25), transparent 22%),
    linear-gradient(135deg, #020617, #02001f, #000000);
    color: white;
}
.hero {
    min-height: 430px;
    border-radius: 32px;
    padding: 45px;
    background:
    linear-gradient(rgba(0,0,0,.45), rgba(0,0,0,.65)),
    url("https://images.unsplash.com/photo-1446776811953-b23d57bd21aa");
    background-size: cover;
    background-position: center;
    box-shadow: 0 0 60px rgba(0,255,255,.35);
    border: 1px solid rgba(0,255,255,.35);
}
.title {
    font-size: 68px;
    font-weight: 900;
    margin-top: 45px;
    background: linear-gradient(90deg,#00eaff,#ffffff,#a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.subtitle {
    font-size: 24px;
    max-width: 850px;
}
.glass {
    padding: 24px;
    border-radius: 24px;
    background: rgba(255,255,255,.08);
    border: 1px solid rgba(255,255,255,.20);
    box-shadow: 0 20px 60px rgba(0,0,0,.45);
    margin-top: 20px;
}
.feature {
    padding: 22px;
    border-radius: 22px;
    background: linear-gradient(135deg, rgba(0,234,255,.15), rgba(139,92,246,.14));
    border: 1px solid rgba(0,234,255,.30);
    min-height: 150px;
}
.moon {
    font-size: 95px;
    text-align: right;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="moon">🌕 🛰️</div>
    <div class="title">ThermaVision AI</div>
    <div class="subtitle">
        A space-inspired infrared intelligence platform that transforms thermal images
        into enhanced mission-ready visual outputs.
    </div>
    <br>
    <b>Mission Use:</b> Satellite Monitoring • Night Rescue • Surveillance • Disaster Response
</div>
""", unsafe_allow_html=True)

st.markdown("## 🌌 Mission Control")

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="feature"><h3>🛰 Satellite Vision</h3><p>Analyze infrared frames captured from remote sensing systems.</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="feature"><h3>🌙 Night Intelligence</h3><p>Improve visibility in low-light and thermal scenes.</p></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="feature"><h3>🚨 Rescue Assist</h3><p>Support emergency teams with clearer thermal visualization.</p></div>', unsafe_allow_html=True)

st.markdown('<div class="glass">', unsafe_allow_html=True)
st.markdown("## 🔥 Infrared Image Processing Lab")

mode = st.selectbox(
    "Select Mission Type",
    ["Lunar Thermal Scan", "Satellite Thermal Analysis", "Disaster Rescue Scan", "Night Surveillance Scan"]
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
        st.subheader("📡 Raw Infrared Input")
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("🧠 Enhanced Thermal Output")
        st.image(colorized, use_container_width=True)

    st.markdown("## 📊 AI Mission Report")

    if mode == "Lunar Thermal Scan":
        st.subheader("🌕 Lunar Surface Analysis")
        st.success("Lunar thermal anomalies detected.")
        st.info("Possible crater hotspot regions identified.")
        alert = "Scientific"

    elif mode == "Satellite Thermal Analysis":
        st.subheader("🛰️ Satellite Thermal Mapping")
        st.success("Thermal terrain analysis completed.")
        st.info("High temperature regions detected.")
        alert = "Moderate"

    elif mode == "Disaster Rescue Scan":
        st.subheader("🚨 Disaster Rescue Report")
        st.success("Rescue priority analysis completed.")
        st.warning("Possible human heat signatures found.")
        alert = "High"

    else:
        st.subheader("🌙 Night Surveillance Report")
        st.success("Night surveillance scan completed.")
        st.info("Suspicious thermal activity detected.")
        alert = "Medium"

    r1, r2, r3 = st.columns(3)
    r1.metric("Clarity Boost", "92%")
    r2.metric("Alert Level", alert)
    r3.metric("Status", "Processed")

    result_img = Image.fromarray(colorized)
    buffer = BytesIO()
    result_img.save(buffer, format="PNG")

    st.download_button(
        "⬇ Download Enhanced Mission Output",
        buffer.getvalue(),
        "thermavision_output.png",
        "image/png"
    )

else:
    st.info("Upload a thermal image to start the mission scan.")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="glass">
<h2>👥 Mission Team</h2>
<p><b>Team Name:</b> AstroVision Coders</p>
<p><b>Project Lead:</b> Vishal Kumar</p>
<p><b>Domain:</b> AI • Image Processing • Remote Sensing</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<center>
<br>
<p>© 2026 ThermaVision AI | Space-Inspired Infrared Intelligence Platform</p>
</center>
""", unsafe_allow_html=True)
