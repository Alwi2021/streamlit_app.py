import streamlit as st
import google.generativeai as genai

# Konfigurasi Google Generative AI dengan kunci API kamu
genai.configure(api_key="AIzaSyCH2yiCqUZoceiJvNo1BycDAfKZPuNGKtw")
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("Sistem Imdigital")
st.caption("Pusat Kendali Nur Makrifat - Indramayu Club")

# Input Chat
if prompt := st.chat_input("Apa perintah Anda hari ini?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Respon dari Gemini
    try:
        response = model.generate_content(prompt)
        with st.chat_message("assistant"):
            st.markdown(response.text)
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
