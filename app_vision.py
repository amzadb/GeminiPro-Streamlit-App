from dotenv import load_dotenv
load_dotenv()  # Read variables from .env

import os
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get respone
def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input != "":
       response = model.generate_content([input, image])
    else:
       response = model.generate_content(image)
    return response.text

# Initialize the streamlit app
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Gemini Pro Vision Q&A")
st.header("Gemini Pro Vision Q&A")

# Sidebar content
with st.sidebar:  
    st.markdown('''
        ## About
        This app is Gemini-powered chatbot built using:
        - [Streamlit](https://streamlit.io/)
        - [Gemini Pro Vision](https://cloud.google.com/vertex-ai/docs/generative-ai/multimodal/overview) LLM Model
        ''')
    st.write("Made with ❤️ by Amzad Basha.")

# UI Content        
uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

input = st.text_input("Input Prompt: ", key="input")

submit = st.button("Submit")

# When the button is clicked
if submit:
    response = get_gemini_response(input, image)
    st.subheader("The Response is")
    st.write(response)
