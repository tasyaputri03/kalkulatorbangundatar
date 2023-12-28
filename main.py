import streamlit as st



st.title('Hitung Luas Persegi Panjang')
    
panjang = st.number_input ("Masukkan Nilai panjang", 0)
lebar = st.number_input ("Masukkan Nilai Lebar", 0)
hitung = st.button ("hitung luas")
    
if hitung :
        luas = panjang * lebar
        st.write ("Luas persegi panjang adalah = ", luas)
        st.success (f"Luas Persegi panjang adalah = {luas}")
