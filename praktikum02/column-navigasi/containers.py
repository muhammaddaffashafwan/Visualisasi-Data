import streamlit as st 
import numpy as np

st.title("Containers")
st.write("Kelompok: 19")
st.markdown("""
            1. Muhammad Daffa Shafwan - 0110222275
            2. Dewi Nuraini – 0110122122 
            3. Muhammad Saputra Adi Firmansyah – 0110222105  
""")

with st.container():
    st.write("Element Inside Container")
    st.line_chart(np.random.randn(40, 4))
    st.write("Element Outside Container")