from dotenv import load_dotenv
load_dotenv()  # Read variables from .env

import os
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get respone
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    # response = model.generate_content(question)
    # return response
    response = chat.send_message(question,stream=True)
    return response

# Initialize our streamlit app
import streamlit as st

st.set_page_config(page_title="Gemini Pro Q&A")
st.header("Gemini Pro Q&A")

# Sidebar content
with st.sidebar:  
    st.markdown('''
        ## About
        This app is Gemini-powered chatbot built using:
        - [Streamlit](https://streamlit.io/)
        - [Gemini Pro](https://cloud.google.com/vertex-ai/docs/generative-ai/multimodal/overview) LLM Model
        ''')
    st.write("Made with ❤️ by Amzad Basha.")

# UI content
input = st.text_input("Input: ", key="input")
submit = st.button("Submit")

# When the button is clicked
if submit:
    response=get_gemini_response(input)
    st.subheader("The Response is")
    # st.write(response)
       
    for chunk in response:
        st.write(chunk.text)
    
    # st.write(chat.history)
