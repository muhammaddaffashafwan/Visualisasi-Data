import streamlit as st
import pandas as pd
import numpy as np

st.title("Line Chart")
st.write("Kelompok: 19")
st.markdown("""
            1. Muhammad Daffa Shafwan - 0110222275
            2. Dewi Nuraini – 0110122122 
            3. Muhammad Saputra Adi Firmansyah – 0110222105  """)

df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=["C1", "C2", "C3", "C4"]
)

st.line_chart(df)

