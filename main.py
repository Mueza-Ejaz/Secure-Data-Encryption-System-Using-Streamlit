import streamlit as st # for user-interface
import hashlib # for hashing values
from cryptography.fernet import Fernet # for making secure data like encrypt(lock) and decrypt(unlock)

# --- Page Setup ---
st.set_page_config(page_title="Secure Data System", page_icon="🔐", layout="centered")
st.title(" Encrypt Your Data, Stay Protected")


# Generate and Store Encryption Key in Session ---
if "fernet" not in st.session_state: # store data for temporary 
    key = Fernet.generate_key()
    st.session_state.fernet = Fernet(key)

fernet = st.session_state.fernet


# --- Store Data & Attempts in Session ---
if "stored_data" not in st.session_state:
    st.session_state.stored_data = {}

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "is_logged_in" not in st.session_state:
    st.session_state.is_logged_in = True

if "menu" not in st.session_state:
    st.session_state.menu = "Home"


# --- Dummy Credentials ---
VALID_USERNAME = "admin"
VALID_PASSWORD = "1234"


# --- Helpers ---
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt_text(text):
    return fernet.encrypt(text.encode()).decode()

def decrypt_text(encrypted_text):
    return fernet.decrypt(encrypted_text.encode()).decode()


# --- Login Page ---
def login_page():
    st.subheader(" Login to Continue")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            st.success(" Login successful!")
            st.session_state.is_logged_in = True
            st.session_state.attempts = 0
        else:
            st.error(" Invalid credentials")


# --- Insert Data ---
def insert_data():
    st.subheader(" Store New Data")
    user_key = st.text_input("Enter your passkey", type="password")
    user_text = st.text_area("Enter your secret data")
    if st.button("Store"):
        if user_key and user_text:
            hashed_key = hash_passkey(user_key)
            encrypted = encrypt_text(user_text)
            st.session_state.stored_data[hashed_key] = encrypted
            st.success(" Data stored securely!")
        else:
            st.warning(" Please fill in all fields.")


# --- Retrieve Data ---
def retrieve_data():
    st.subheader(" Retrieve Your Data")
    user_key = st.text_input("Enter your passkey", type="password")
    if st.button("Retrieve"):
        if user_key:
            hashed_key = hash_passkey(user_key)
            if hashed_key in st.session_state.stored_data:
                decrypted = decrypt_text(st.session_state.stored_data[hashed_key])
                st.success(" Data decrypted successfully:")
                st.code(decrypted)
                st.session_state.attempts = 0
            else:
                st.session_state.attempts += 1
                remaining = 3 - st.session_state.attempts
                st.error(f" Incorrect passkey. {remaining} attempts left.")
                if st.session_state.attempts >= 3:
                    st.session_state.is_logged_in = False


# --- Navigation + Interface ---
if st.session_state.is_logged_in:
    st.markdown("###  Choose What You Want To Do")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button(" Home"):
            st.session_state.menu = "Home"
    with col2:
        if st.button(" Insert Data"):
            st.session_state.menu = "Insert Data"
    with col3:
        if st.button(" Retrieve Data"):
            st.session_state.menu = "Retrieve Data"

    # Page Logic
    if st.session_state.menu == "Home":
        st.info(" Use the buttons above to store or retrieve secure data.")
    elif st.session_state.menu == "Insert Data":
        insert_data()
    elif st.session_state.menu == "Retrieve Data":
        retrieve_data()
else:
    login_page()






