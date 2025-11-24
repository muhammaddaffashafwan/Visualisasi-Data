import streamlit as st
import time

st.title("Empety Containers")
st.write("Kelompok: 19")
st.markdown("""
            1. Muhammad Daffa Shafwan - 0110222275
            2. Dewi Nuraini – 0110122122 
            3. Muhammad Saputra Adi Firmansyah – 0110222105  
""")

with st.empty():
    for seconds in range(5):
        st.write(f" {seconds} seconds have passed")
        time.sleep(1)
        st.write("Timer up!")