
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime

st.set_page_config(page_title="Egypt Apartment Price Predictor", page_icon="🏠", layout="centered")

# --- Modern, clean UI ---
st.markdown("""
<style>
.big-title {font-size: 34px; font-weight: 800; margin-bottom: 0.25rem;}
.sub {color: #6b7280; margin-bottom: 1.0rem;}
.card {background: #ffffff; padding: 1.2rem; border-radius: 1rem; box-shadow: 0 10px 25px rgba(0,0,0,0.06);}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">🏡 Egypt Apartment Price Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">Fast ML app to estimate apartment prices in major Cairo districts.</div>', unsafe_allow_html=True)

@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

with st.container():
    with st.form("predict_form"):
        st.markdown('<div class="card">', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            district = st.selectbox("District", [
                "New Cairo", "Nasr City", "Maadi", "Zamalek", "6th of October",
                "Sheikh Zayed", "Heliopolis", "Dokki", "Mohandessin", "Tagamoa"
            ])
            area_sqm = st.slider("Area (sqm)", 45, 400, 140, step=5)
            bedrooms = st.slider("Bedrooms", 1, 6, 3)
            bathrooms = st.slider("Bathrooms", 1, 4, 2)
        with col2:
            floor = st.slider("Floor", 0, 15, 3)
            has_elevator = st.selectbox("Elevator", ["No", "Yes"])
            finishing = st.selectbox("Finishing", ["Core & Shell", "Semi-Finished", "Fully-Finished", "Luxury-Finished"])
            building_age = st.slider("Building age (years)", 0, 40, 10)

        submitted = st.form_submit_button("🔮 Predict Price")
        st.markdown('</div>', unsafe_allow_html=True)

if submitted:
    input_df = pd.DataFrame([{
        "district": district,
        "area_sqm": area_sqm,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "floor": floor,
        "has_elevator": 1 if has_elevator == "Yes" else 0,
        "finishing": finishing,
        "building_age": building_age
    }])
    pred = model.predict(input_df)[0]
    low = pred * 0.9
    high = pred * 1.1

    st.success(f"**Estimated price:** {pred:,.0f} EGP")
    st.caption(f"Range: {low:,.0f} — {high:,.0f} EGP")

    with st.expander("Show input details"):
        st.write(input_df)

st.markdown("---")
st.caption("Built with ❤️ using Streamlit + scikit-learn. Last updated: " + datetime.now().strftime("%Y-%m-%d"))
