import streamlit as st
import pandas as pd
import numpy as np

st.title("Map")
st.write("Kelompok: 19")
st.markdown("""
            1. Muhammad Daffa Shafwan - 0110222275
            2. Dewi Nuraini – 0110122122 
            3. Muhammad Saputra Adi Firmansyah – 0110222105  """)

df= pd.DataFrame(
    np.random.randn(50, 2) / [10,10] + [15.4589, 75.0078],
    columns=["latitude", "longitude"]
)

st.map(df)