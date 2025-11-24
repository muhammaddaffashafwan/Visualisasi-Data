import streamlit as st
import datetime
import pandas as pd

st.subheader("Kelompok 19")
st.markdown("""
            1. Muhammad Daffa Shafwan - 0110222275
            2. Dewi Nuraini – 0110122122 
            3. Muhammad Saputra Adi Firmansyah – 0110222105  """)

st.title("Text Box")
# Creating Text Box
name = st.text_input("Enter your Name")
st.write("Your Name is ", name)


st.title("Text Area")
# Create Text Area
input_text = st.text_area("Enter your Review")
# Printing entered text
st.write("""You entered: \n""",input_text)


st.title("Number input")
# Create number input
st.number_input("Enter your Number")
num = st.number_input("Enter your Number", 0, 10, 5, 2)
st.write("Min. Value is 0, \n Max. value is 10")
st.write("Default Value is 5, \n Step Size value is 2")
st.write("Total value after adding Number entered with step value is:", num)


st.title("Time")
# Defining Data Function
st.time_input("Select Your Time")


st.title("Date")
# Defining Data Function
st.date_input("Select your Date", value=datetime.date(1989, 12, 25),
min_value=datetime.date(1987, 1, 1),
max_value=datetime.date(2005, 12, 1))


st.title("Select Color")
# Defining color picker
color_code = st.color_picker("Select your Color")
st.header(color_code)



st.title("CVS Data")
data_file = st.file_uploader("Upload CSV", type=["csv"])
details = st.button("Check Details")
if details:
    if data_file is not None:
        file_details = {"file_name":data_file.name, "file_type": data_file.type,
        "file_size":data_file.size}
        st.write(file_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)
    else:
        st.write("No CSV File is Uploaded")


my_form = st.form(key='form')
a = my_form.text_input(label='Enter any text')
# Defining submit button
submit_button = my_form.form_submit_button(label='Submit')

st.write(a)