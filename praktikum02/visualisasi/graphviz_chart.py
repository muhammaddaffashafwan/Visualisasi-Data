import streamlit as st
import graphviz as graphviz

st.title("Graphviz Chart")
st.write("Kelompok: 19")
st.markdown("""
            1. Muhammad Daffa Shafwan - 0110222275
            2. Dewi Nuraini – 0110122122 
            3. Muhammad Saputra Adi Firmansyah – 0110222105  """)

st.graphviz_chart("""
    digraph{
        "Training Data" -> "ML Algorithm"
        "ML Algorithm" -> "Model"
        "Model" -> "Results Forecasting"
        "New Data" -> "Model"}
                  """)