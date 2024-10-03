from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st
import google.generativeai as genai
import pathlib
import textwrap
from IPython.display import display
from IPython.display import Markdown
from PIL import Image

# Load environment variables
os.environ['GOOGLE_API_KEY'] = "AIzaSyAgCaUoVP789xHJg2IrF3rH5X24gw9vNWM"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])


def get_gemini_response(input,image):
    model=genai.GenerativeModel("gemini-1.5-flash") #for images
    if input!="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text


st.set_page_config(page_title="GEMINI VISION PRO BOT")
st.header("GEMINI APPLICATION")

input=st.text_input("Input Prompt:",key="input")
uploaded_file=st.file_uploader("Choose an image...",type=["jpg","jpeg","png"])

if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,"Uploaded Image",use_column_width=True)

submit=st.button("Tell me about the image")
if submit:
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)


