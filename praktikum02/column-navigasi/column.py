import streamlit as st

st.title("Columns")
st.write("Kelompok: 19")
st.markdown("""
            1. Muhammad Daffa Shafwan - 0110222275
            2. Dewi Nuraini – 0110122122 
            3. Muhammad Saputra Adi Firmansyah – 0110222105  
""")

col1, col2 = st.columns(2)

col1.write("Ini adalah kolom pertama")
col1.image("../assets/bulat1.jpeg")
col2.write("Ini adalah kolom kedua")
col2.image("../assets/bulat2.png")