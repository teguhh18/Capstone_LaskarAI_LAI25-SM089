import streamlit as st
import pandas as pd
import numpy as np
import joblib
from PIL import Image
import os
from tensorflow import keras

# —————— CONFIG ——————
st.set_page_config(page_title="Flood Prediction App (Prototype)", layout="wide")

# —————— HEADER ——————
col_title = st.columns(1)[0]
with col_title:
    st.markdown(
        "<h1 style='margin-bottom:0;'>Flood Prediction</h1>"
        "<div>lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</div>", unsafe_allow_html=True
    )
st.markdown("---")

# —————— LOAD MODEL ——————
@st.cache_resource
def load_my_model(model_path):
    try:
        model = keras.models.load_model(model_path)
        return model
    except Exception as e:
        st.error(f"Gagal memuat model: {e}")
        return None


# Path ke file model .h5
MODEL_PATH = "flood_model_f.h5"
model = load_my_model(MODEL_PATH)

# —————— END LOAD MODEL ——————


# —————— LOAD SCALER ——————
@st.cache_resource
def load_scaler(scaler_path):
    try:
        scaler = joblib.load(scaler_path)
        return scaler
    except Exception as e:
        st.error(f"Gagal memuat scaler: {e}")
        return None


SCALER_PATH = "flood_scaler.pkl"
scaler = load_scaler(SCALER_PATH)
# —————— END LOAD SCALER ——————

with st.container():
    # Menampilkan home image
    # st.image("flood.jpg")

    # Menampilkan HOme image dengan custom size
    IMAGE_DIRECTORY = "."
    IMAGE_FILENAME = "flood.jpg"
    image_path = os.path.join(IMAGE_DIRECTORY, IMAGE_FILENAME)
    home_image = Image.open(image_path)
    home_image_resized = home_image.resize((1540, 640))
    landing_image = None
    st.image(home_image_resized, use_container_width=True)

    # —————— FORM INPUT DATA——————
    with st.form("flood_input_form", clear_on_submit=False):
        st.subheader("📝Silahkan Masukkan Data Untuk Prediksi Dibawah ini")

        col1, col2 = st.columns([1, 1])
        with col1:
            MonsoonIntensity = st.number_input(
                "Moon Soon Intensity", step=1, min_value=0
            )

            CoastalVulnerability = st.number_input(
                "Coastal Vulnerability", step=1, min_value=0
            )

            EnvironmentalDegradationScore = st.number_input(
                "Environmental Degradation Score", min_value=0.00
            )

        with col2:
            RiverObstructionRisk = st.number_input(
                "River Obstruction Risk", min_value=0.00
            )

            Siltation = st.number_input("Siltation", step=1, min_value=0)
            Deforestation = st.number_input("Deforestation", step=1, min_value=0)

        submitted = st.form_submit_button("Predict", type="primary")

    st.markdown("---")

    # —————— PREDIKSI ——————
    if submitted:
        # Bangun DataFrame
        df_input = pd.DataFrame(
            {
                "MonsoonIntensity": [MonsoonIntensity],
                "CoastalVulnerability": [CoastalVulnerability],
                "EnvironmentalDegradationScore": [EnvironmentalDegradationScore],
                "RiverObstructionRisk": [RiverObstructionRisk],
                "Siltation": [Siltation],
                "Deforestation": [Deforestation],
            }
        )

        # SCALING DATA
        scaled_input = scaler.transform(df_input)
        
        # PREDIKSI
        prediction = model.predict(scaled_input)

        # Ambil nilai prediksi, ubah jadi float
        flood_probability = float(prediction.flatten()[0])
        # UBAH JADI BENTUK PERSENTASE
        flood_probability_percentage = flood_probability * 100

        # Kode untuk hasil prediksi
        st.subheader("Hasil Prediksi")
        st.write(f"Hasil : {flood_probability_percentage:.2f}%")

        if prediction >= 0.8:
            # ALERT WARNING
            st.markdown(
                """
                    <div style="
                        background-color: #fff3cd;
                        color: #856404;
                        padding: 20px;
                        margin: 20px auto;
                        border: 1px solid #ffeeba;
                        border-radius: 5px;
                        max-width: 700px;
                        text-align: center;
                    ">
                        <h4 style="margin-top: 0;">⚠️ WARNING ALERT!!!</h4>
                        <p style="text-align: justify;">
                            Lorem ipsum dolor sit amet consectetur. In ultrices scelerisque tortor amet. Turpis eget id et luctus in.
                            Sagittis pulvinar aliquam senectus semper urna vitae pellentesque vestibulum. Elit pulvinar id porta
                            scelerisque nibh nisl. Non feugiat id duis et ornare duis nunc in.
                        </p>
                    </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            # ALERT AMAN
            st.markdown(
                """
                    <div style="
                        background-color: #d4edda;
                        color: #155724;
                        padding: 20px;
                        margin: 20px auto;
                        border: 1px solid #c3e6cb;
                        border-radius: 5px;
                        max-width: 700px;
                        text-align: center;
                    ">
                        <h4 style="margin-top: 0;">✅ AMAN</h4>
                        <p style="text-align: justify;">
                            Lorem ipsum dolor sit amet consectetur. In ultrices scelerisque tortor amet. Turpis eget id et luctus in.
                            Sagittis pulvinar aliquam senectus semper urna vitae pellentesque vestibulum. Elit pulvinar id porta
                            scelerisque nibh nisl. Non feugiat id duis et ornare duis nunc in.
                        </p>
                    </div>
                """,
                unsafe_allow_html=True,
            )

        # KODE UNTUK SOSIALISASI
        st.markdown("---")
        st.subheader("Sosialisasi")

        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            st.image("saran.jpg")
            st.write(
                "lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
            )
        with col2:
            st.image("saran.jpg")
            st.write(
                "lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
            )
        with col3:
            st.image("saran.jpg")
            st.write(
                "lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
            )

    else:
        st.info(
            "🔎 Masukkan nilai fitur di atas, lalu klik **Predict** untuk melihat hasil."
        )

# —————— FOOTER ——————
st.markdown("---")

st.markdown(
    "<p style='text-align: center; color: gray;'>"
    "© 2025 Flood Prediction Capstone"
    "</p>",
    unsafe_allow_html=True,
)
