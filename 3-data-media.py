import streamlit as st
from PIL import Image
import base64
st.write("Displaying an Images")
# Displaying Image by specifying path
st.image("assets/bg1.jpeg")
# Image Courtesy by unplash
st.write("assets/bg1.jpeg")


# Image courtesy
st.write("")
# Listing out animal images
animal_images = [
    'assets/harimau.jpeg',
    'assets/panda.jpeg',
    'assets/merak.jpeg'
]
# Displaying Multiple images with width 150
st.image(animal_images, width=150)
# Image Courtesy
st.write("assets/bg1.jpeg")

# Function to set Image as Background
def add_local_background_image_(image):
    with open(image, "rb") as image:
        encoded_string = base64.b64encode(image.read())
    st.write("Image Courtesy: unplash")
    st.markdown(
        f"""
        <style>
        .stApp {{
        background-image: url(data:files/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
st.write("Background Image")
# Calling Image in function
add_local_background_image_('assets/background.jpg')

original_image = Image.open("assets/background.jpg")
# Display Original Image
st.title("Original Image")
st.image(original_image)
# Resizing Image to 600*400
resized_image = original_image.resize((600, 400))
# Displaying Resized Image
st.title("Resized Image")
st.image(resized_image)