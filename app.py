"""
Interactive Streamlit Web Application for Plant Disease Detection.
Provides drag-and-drop image upload, instant diagnosis, confidence rankings,
and agronomic actionable treatment recommendations.
"""

import os
from PIL import Image
import streamlit as st
import pandas as pd

from src.inference import DiseasePredictor
from src.classes import CLASS_NAMES

# Page configuration
st.set_page_config(
    page_title="Plant Disease AI Diagnostic",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1b5e20;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #4a5568;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background-color: #f8fafc;
        border-radius: 10px;
        padding: 1rem;
        border: 1px solid #e2e8f0;
    }
    .badge-healthy {
        background-color: #dcfce7;
        color: #166534;
        padding: 0.35rem 0.75rem;
        border-radius: 9999px;
        font-weight: 600;
        display: inline-block;
    }
    .badge-warning {
        background-color: #fef3c7;
        color: #92400e;
        padding: 0.35rem 0.75rem;
        border-radius: 9999px;
        font-weight: 600;
        display: inline-block;
    }
    .badge-critical {
        background-color: #fee2e2;
        color: #991b1b;
        padding: 0.35rem 0.75rem;
        border-radius: 9999px;
        font-weight: 600;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)


@st.cache_resource
def load_predictor():
    weights_path = "models/plant_disease_model.pth"
    if not os.path.exists(weights_path):
        weights_path = None
    return DiseasePredictor(weights_path=weights_path)


predictor = load_predictor()

# Sidebar
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1530836369250-ef72a3f5cda8?w=500&auto=format&fit=crop&q=60", caption="Smart Agriculture Diagnostics")
    st.markdown("### 🌾 About the System")
    st.markdown("""
    This application utilizes an **optimized MobileNetV3 Deep Neural Network** trained on crop leaf pathology.
    
    **Features:**
    - ⚡ Fast, lightweight edge-ready inference
    - 🔍 Multi-class crop & pathogen detection
    - 📋 Prescriptive treatment recommendations
    - 📊 Multi-prediction confidence distribution
    """)
    st.markdown("---")
    st.caption("Developed by Soham Deokar | [GitHub](https://github.com/sohamdeokar101-coder)")

# Main Area
st.markdown('<div class="main-header">🌿 AI Plant Disease Diagnostic Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Upload a clear photograph of a crop leaf to detect diseases, assess severity, and view targeted care instructions.</div>', unsafe_allow_html=True)

col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
    st.subheader("📸 Leaf Image Input")
    
    upload_tab, sample_tab = st.tabs(["Upload Photo", "Try Sample Images"])
    
    image = None
    
    with upload_tab:
        uploaded_file = st.file_uploader("Select an image (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            
    with sample_tab:
        sample_dir = "sample_images"
        sample_files = []
        if os.path.exists(sample_dir):
            sample_files = [f for f in os.listdir(sample_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        
        if sample_files:
            selected_sample = st.selectbox("Choose a sample test leaf:", sample_files)
            if selected_sample:
                sample_path = os.path.join(sample_dir, selected_sample)
                image = Image.open(sample_path)
        else:
            st.info("No sample images found in `sample_images/` yet.")

    if image is not None:
        st.image(image, caption="Uploaded Leaf Photograph", use_container_width=True)

with col_right:
    st.subheader("🔬 Diagnostic Analysis")
    
    if image is None:
        st.info("👈 Please upload a leaf photo or pick a sample leaf from the left panel to begin diagnosis.")
    else:
        with st.spinner("Processing image through Deep Learning classifier..."):
            result = predictor.predict(image, top_k=3)
        
        severity = result["severity"]
        if severity == "None":
            badge_class = "badge-healthy"
        elif severity in ["Low", "Moderate"]:
            badge_class = "badge-warning"
        else:
            badge_class = "badge-critical"

        st.markdown(f"""
        <div class="metric-card">
            <h3>Crop: <b>{result['crop']}</b></h3>
            <h4>Diagnosis: <b>{result['condition']}</b></h4>
            <p>Confidence: <b>{result['confidence']*100:.1f}%</b></p>
            <p>Severity: <span class="{badge_class}">{severity}</span></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### 💊 Actionable Treatment & Recommendation")
        st.success(result["recommendation"])

        st.markdown("#### 📊 Confidence Breakdown")
        df_top = pd.DataFrame([
            {
                "Candidate": p["condition"],
                "Confidence": round(p["confidence"] * 100, 2)
            } for p in result["top_k"]
        ])
        st.bar_chart(df_top.set_index("Candidate"), color="#2e7d32")
