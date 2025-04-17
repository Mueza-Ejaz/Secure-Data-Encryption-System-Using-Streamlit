import streamlit as st # for user-interface
import hashlib # for hashing values
from cryptography.fernet import Fernet # for making secure data like encrypt(lock) and decrypt(unlock)

# --- Page Setup ---
st.set_page_config(page_title="Secure Data System", page_icon="🔐", layout="centered")
st.title(" Encrypt Your Data, Stay Protected")


def custom_css():
    st.markdown(
        """
        <style>
          
           @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        /* Applying font to the entire app */
            html, body, [class*="st-"] {
           font-family: Georgia, serif; /* Applying Poppins font */
        }

        .stApp{
            background-image: url("https://plus.unsplash.com/premium_photo-1701179596614-9c64f50cda76?q=80&w=1374&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
            z-index:-1;
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            color: black;
            text-align: center;
        }

        .stApp > div {
        backdrop-filter: blur(5px); /* Prevents blur on text */
    }

        .stheader {
        font-family: Verdana, sans-serif; !important 
        font-size: 30px;
        color: #4CAF50; /* Green */
        text-align: left;
        }


        .stsubheader {
        font-family: 'Courier New', monospace; !important 
        font-size: 30px;
        color: #4CAF50; /* Green */
        text-align: left;
        }

        abel {
        color: black !important; /* Changing label color to green */
        font-size: 18px; /* Increasing font size */
        font-weight: bold; /* Making it bold */
    }
    
   input[type=number] {
        border-radius: 10px 0px 10px 0px !important; /* Rounded corners */
        border: 2px solid #3498db !important; /* Blue border */
        padding: 10px !important;
        font-size: 16px !important;
        background: rgba(255, 255, 255, 0.8) !important; /* Semi-transparent background */
        color: black !important;
        outline: none !important;
    }




    .stButton > button {
        background-color: blue !important; /* Change button background to blue */
        color: white !important; /* Change text color to white */
        font-size: 18px; /* Increase font size */
        border-radius: 10px 0px 10px 0px; /* Rounded corners */
        padding: 10px 20px; /* Add padding */
        border: 2px solid black; /* Black border */
    }

    /* Change button color when hovered */
    .stButton > button:hover {
        background-color: darkblue !important; /* D
    }

    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        font-weight: bold;
        color: #333;
    }
    

        </style>

        """,

        unsafe_allow_html=True,
    )

custom_css()














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
    st.session_state.is_logged_in = False

if "menu" not in st.session_state:
    st.session_state.menu = "Home"


# --- Dummy Credentials ---
VALID_USERNAME = "Mueza"
VALID_PASSWORD = "862001"


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
            st.session_state.menu = "Home"
            st.rerun()
        else:
            st.error(" Invalid username or password")
            st.session_state.menu = "Home"  # Reset menu to show login page


# --- Insert Data ---
def insert_data():
    st.subheader(" Save Your Secret")
    user_key = st.text_input("Create your passkey", type="password")
    user_text = st.text_area("Write your secret data here")
    if st.button("Save"):
        if user_key and user_text:
            hashed_key = hash_passkey(user_key)
            encrypted = encrypt_text(user_text)
            st.session_state.stored_data[hashed_key] = encrypted
            st.success(" Data stored securely!")
        else:
            st.warning(" Please fill in all fields.")


# --- Retrieve Data ---
def retrieve_data():
    st.subheader(" Unlock Your Secret")
    user_key = st.text_input("Enter your passkey", type="password")
    if st.button("Unlock"):
        if user_key:
            hashed_key = hash_passkey(user_key)
            if hashed_key in st.session_state.stored_data:
                decrypted = decrypt_text(st.session_state.stored_data[hashed_key])
                st.success(" Here's your secret data:")
                st.code(decrypted)
                st.session_state.attempts = 0
            else:
                st.session_state.attempts += 1
                remaining = 3 - st.session_state.attempts
                st.error(f" Incorrect passkey. {remaining} attempts left.")
                if st.session_state.attempts >= 3:
                    st.session_state.is_logged_in = False
                    st.session_state.menu = "Home"


# --- Main Interface ---
if st.session_state.is_logged_in:
    st.markdown("###  Choose an Option Below")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button(" Home"):
            st.session_state.menu = "Home"
    with col2:
        if st.button(" Save Secret"):
            st.session_state.menu = "Insert Data"
    with col3:
        if st.button(" View Secret"):
            st.session_state.menu = "Retrieve Data"

    # --- Page Logic ---
    if st.session_state.menu == "Home":
        st.info(" Use the buttons above to securely store or retrieve your private data.")
    elif st.session_state.menu == "Insert Data":
        insert_data()
    elif st.session_state.menu == "Retrieve Data":
        retrieve_data()

else:
    login_page()

st.markdown(
    """
    <div style="text-align: center; padding: 10px; font-size: 14px; font-weight: bold; color: #333;">
        Copyrights Reserved &copy; Mueza Ejaz
    </div>
    """,
    unsafe_allow_html=True
)







