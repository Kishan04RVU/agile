from openai import OpenAI
from PIL import Image
import streamlit as st
from apikey import apikey

client = OpenAI(api_key=apikey)

def generate_image(image_description, num_images):
    img_description = client.images.generate(
        model="dall-e-3",
        prompt=image_description,
        size="1024x1024",
        quality="standard",
        n=num_images  # Fixed the variable name here
    )
    image_urls = [img_data.url for img_data in img_description.data]  # Fixed the variable name here
    return image_urls

st.set_page_config(page_title="Dalle-Image-Generation", page_icon=":camera:", layout="wide")

st.title("DALL-E-3 Image Generation Tool")
st.subheader("POWERED BY THE World's Most POWERFUL Image Generation API- DALL-E")

img_description = st.text_input("Enter a description for the image you want to generate ")
num_of_images = st.number_input("Select the number of images you want to generate", min_value=1, max_value=5, value=1)

if st.button("Generate Images"):
    generated_images = generate_image(img_description, num_of_images)
    for image_url in generated_images:
        st.image(image_url)
