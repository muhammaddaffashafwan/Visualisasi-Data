import streamlit as st
import time

st.subheader("Kelompok 19")
st.markdown("""
            1. Muhammad Daffa Shafwan - 0110222275
            2. Dewi Nuraini – 0110122122 
            3. Muhammad Saputra Adi Firmansyah – 0110222105  """)

st.title('Creating a Button')
# Defining a Button
button = st.button('Click Here')
if button:
    st.write('You have clicked the button')
else:
    st.write('You have not clicked the button')


st.title('Creating Radio Button')
# Defining Radio Button
gender = st.radio(
"Select Your Gender",
('Male', 'Female', 'Others'))
if gender == 'Male':
    st.write('You have selected Male.')
elif gender == 'Female':
    st.write("You have selected Female")
else:
    st.write("You have selected Others.")


st.title('Creating Checkboxes')
st.write('Select your Hobies:')
# Defining Checkboxes
check_1 = st.checkbox('Hiking')
check_2 = st.checkbox('Games')
check_3 = st.checkbox('Sports')


st.title('Creating Dropdown')
# Creating Dropdown
hobby = st.selectbox('Choose your hobby: ',
('Hiking', 'Games', 'Sports'))


st.title('Multi-Select')
# Defining Multi_select with Pre-Selection
hobbies = st.multiselect(
'What are your Gobbies',
['Games', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Hiking'],
)


st.title("Download Button")
# Creating Download Button
down_btn = st.download_button(
label="Download Image",
data=open("assets/background.jpg", "rb"),
file_name="assets/background.jpg",
mime="image/jpg"
)


st.title('Progress Bar')
# Defining Progress Bar
download = st.progress(0)
for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage+1)
st.write('Download Complete')


st.title('Spinner')
# Defining Spinner
with st.spinner('Loading...'):
    time.sleep(5)
st.write('Hello Data Scientist')