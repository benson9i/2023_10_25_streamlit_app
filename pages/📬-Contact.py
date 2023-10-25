# cd /Users/bennson/Desktop/Data\ Science\ Journey/Streamlit/indices_crypto_app/
# streamlit run 💹-Charts.py

# import sys
# import os
# print(sys.executable)


import json
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from prophet import Prophet
from streamlit_lottie import st_lottie

st.set_page_config(layout="centered")
st.header(":mailbox: Get in touch with me:)")

contact = """
<form action="https://formsubmit.co/dominik.bernard98@gmail.com" method="POST">
     <input type="hidden" name="_capcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact, unsafe_allow_html=True)


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("/Users/bennson/Desktop/Data Science Journey/Streamlit/indices_crypto_app/style/style.css")

# ---- widget section ----


def load_lottiefil(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


lottie_email = load_lottiefil(
    "/Users/bennson/Desktop/Data Science Journey/Streamlit/indices_crypto_app/lottie/email_lottie.json")

col3, col4, col5 = st.columns(3, gap="small")
with col3:
    st.write("")

with col4:
    st_lottie(
        lottie_email,
        height=300,
        width=200
    )

with col5:
    st.write("")
