import streamlit as st 
from PIL import Image
img = Image.open("../assets/bulat1.jpeg")

st.title("Padding")
st.write("Kelompok: 19")
st.markdown("""
            1. Muhammad Daffa Shafwan - 0110222275
            2. Dewi Nuraini – 0110122122 
            3. Muhammad Saputra Adi Firmansyah – 0110222105  
""")

col1, padding, col2 = st.columns((10,2,10))
with col1:
    col1.image(img)
with col2:
    col2.image(img)