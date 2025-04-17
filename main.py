import streamlit as st # for web-interface
from cryptography.fernet import Fernet # for making secure data like encrypt(lock) and decrypt(unlock)

st.set_page_config(
    page_title="DataVault ", 
    page_icon="🔐",  # This sets a small favicon icon (optional)
    layout="centered"    # Options: "centered" (default) or "wide"
)

def custom_css():
    st.markdown(
        """
        <style>

        </style>

        """,

        unsafe_allow_html=True,
    )

custom_css()

st.header(" Encrypt Your Data, Stay Protected ")

