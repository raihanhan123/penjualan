import streamlit as st
import numpy as np
import joblib

# Memuat model yang sudah dilatih
model = joblib.load('penjualan_mobil_toyota (1).pkl')

st.title("Prediksi Penjualan Mobil Toyota")

# Form input
with st.form("form_penjualan"):
    st.header("Masukkan Data Bulan yang Akan Diprediksi:")

    tahun = st.number_input("Tahun", min_value=2010, max_value=2030, step=1)
    bulan_ke = st.selectbox("Bulan ke-", list(range(1, 13)))

    # Tombol submit
    submit = st.form_submit_button("Prediksi")

# Jika tombol diklik
if submit:
    # Format input menjadi array 2D
    fitur = np.array([[tahun, bulan_ke]])

    # Prediksi menggunakan model
    hasil_prediksi = model.predict(fitur)[0]

    # Tampilkan hasil
    st.subheader("Hasil Prediksi Penjualan")
    st.success(f"Prediksi Penjualan Mobil: {int(hasil_prediksi)} unit")
