import streamlit as st
import pandas as pd
import numpy as np
import joblib
from PIL import Image
import os
# from tensorflow.keras.models import load_model

# —————— CONFIG ——————
st.set_page_config(
    page_title="Flood Prediction App (Prototype)",
    layout="wide"
)

# —————— HEADER ——————
col_title, col_blank = st.columns([5, 5])
# ganti dengan path logo kamu
with col_title:
    st.markdown("<h1 style='margin-bottom:0;'>Flood Prediction</h1>", unsafe_allow_html=True)
st.markdown("---")

# —————— LOAD MODEL ——————
model = joblib.load("boosting_model.pkl")

with st.container():
    # Menampilkan home image
    # st.image("flood.jpg")

    # Menampilkan HOme image dengan custom size
    IMAGE_DIRECTORY = "."
    IMAGE_FILENAME = "flood.jpg"
    image_path = os.path.join(IMAGE_DIRECTORY, IMAGE_FILENAME)
    home_image = Image.open(image_path)
    home_image_resized = home_image.resize((1980, 840))
    landing_image = None
    st.image(home_image_resized, use_container_width=True)


    # —————— FORM INPUT ——————
    with st.form("flood_input_form", clear_on_submit=False):
        st.subheader("📝Silahkan Masukkan Data Untuk Prediksi Dibawah ini")

        col1, col2 =st.columns([1,1])
        with col1:
            MoonSoonIntensity = st.number_input("Moon Soon Intensity", step=1, min_value=1)

            CoastalVulnerability = st.number_input("Coastal Vulnerability", step=1, min_value=1)

            EnvironmentDegradationScore = st.number_input("Environment Degradation Score", min_value=0.00)
        
        with col2:
            RiverObstructionRisk = st.number_input("River Obstruction Risk", max_value=0.00)

            Siltation = st.number_input("Siltation", step=1, min_value=1)
            Deforestation = st.number_input("Deforestation", step=1, min_value=1)
        
        submitted = st.form_submit_button("Predict", type="primary")

    st.markdown("---")


    # —————— PREDIKSI ——————
    if submitted:
        # Bangun DataFrame
        df_input = pd.DataFrame({
            "MoonSoonIntensity":         [MoonSoonIntensity],
            "CoastalVulnerability":     [CoastalVulnerability],
            "EnvironmentDegradationScore":          [EnvironmentDegradationScore],
            "RiverObstructionRisk":   [RiverObstructionRisk],
            "Siltation":   [Siltation],
            "Deforestation":   [Deforestation],
        })
        

        # Prediksi
        prediction = model.predict(df_input)

    # Kode untuk hasil prediksi
        st.write("Hasil Prediksi: ", prediction)

        if prediction >= 0.8:
            st.warning("Potensi Banjir Tinggi. lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", width="stretch")
        else:
            st.success("Potensi Banjir Rendah")


        # KODE UNTUK SOSIALISASI
        st.subheader("Sosialisasi")
        st.error('This is a warning', icon="⚠️")


        col1, col2, col3 = st.columns([1,1,1])
        with col1:
            st.image("chris-gallagher-9Jgn8hSYUFc-unsplash.jpg")
            st.write("lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ")
        with col2:
            st.image("chris-gallagher-9Jgn8hSYUFc-unsplash.jpg")
            st.write("lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ")
        with col3:
            st.image("chris-gallagher-9Jgn8hSYUFc-unsplash.jpg")
            st.write("lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")

        
    else:
        st.info("🔎 Masukkan nilai fitur di atas, lalu klik **Predict** untuk melihat hasil.")

# —————— FOOTER ——————
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>"
    "© 2025 Flood Prediction Capstone"
    "</p>", unsafe_allow_html=True
)
