import streamlit as st
from PIL import Image
import requests
import pandas as pd
import os
import json
#
image_path = "image.png"
image = Image.open(image_path)

st.set_page_config(page_title="Grammar Correction App", layout="centered")
st.image(image, caption='Grammar Correction')
#
# page header
st.title(f"Grammar Correction App")
with st.form("Extract"):
   text1 = st.text_input("Enter text here")
   submit = st.form_submit_button("Correction")
   #
   if submit:    
        print(text1)
        #
        with open("input.txt", "wb") as f:
            f.write(text1.encode("utf-8"))
        os.chmod("input.txt", 0o777)
        # Keyword Extraction API
        url = "https://app.aimarketplace.co/api/marketplace/models/grammar-correction-0ad9c2c4/predict/"
        payload={'data': open('input.txt','rb')}
        headers = {'Authorization': 'Api-Key fb5JZ12R.nHvRq6WGnAwg2o4fxp7w6UrRk6DixXkR','Cache-Control': 'no-cache'}

        response = requests.request("POST", url, headers=headers, files=payload)
        #
        print(response.text)
        # output header
        st.header("Corrected Text")
        # output results
        st.success(response.text.split('response')[1].split("Corrected Text")[1].replace("}","").replace(']',"").replace('"',"").replace('\\',''))