# Secure-Data-Encryption-System-Using-Streamlit

A user-friendly web application to **safely store and retrieve your secret information** using encryption. This app is built using **Python and Streamlit**, and it's perfect for learning how encryption, hashing, and session management work together to protect data.

---

## 📌 What This Project Does

- Allows users to **login securely**
- Lets users **store secret messages** using a passkey
- The messages are **encrypted** and saved temporarily
- Users can **retrieve their message** using the correct passkey
- If the wrong passkey is entered **3 times**, user gets logged out
- **No database required** — everything is managed in memory using Streamlit session state

---

## 💡 How It Works

1. **Login Page**:  
   Only users with the correct username and password can log in.

2. **Save Secret**:  
   After logging in, users can enter a **passkey** and a **secret message**. The message is encrypted using **Fernet** and stored with a hashed version of the passkey.

3. **Retrieve Secret**:  
   Users enter the same passkey they used earlier. If it's correct, the secret is decrypted and shown. If wrong, an error message appears.

4. **Security Measures**:
   - Passkey is hashed using SHA-256
   - Data is encrypted using **Fernet encryption**
   - 3 wrong attempts = logout for safety

---

## 🔧 Technologies Used

- **Python** 🐍
- **Streamlit** – for the web interface
- **hashlib** – to securely hash passkeys
- **cryptography.fernet** – for encrypting and decrypting data

---

## 🖼️ Screens (App Pages)

- ✅ Login Page  
- 🔐 Save Secret  
- 🔍 Retrieve Secret  
- 🏠 Home Info Section

---

## ▶️ How To Run the App Locally

### Step 1: Clone the Repo

bash
git clone https://github.com/your-username/secure-data-vault.git
cd secure-data-vault

## 📚 Why I Built This
I created this project to:

Practice secure data storage concepts

Understand encryption & hashing

Explore Streamlit for creating interactive apps

Help others learn about data security in a simple wayInstall Required Packages
pip install -r requirements.txt


🛡️ Security Notice
This project stores data in memory only (session state) and is for educational/demo purposes. For real-world usage, always store encrypted data in a secure database.



## 🚀 Live Demo

Try the app live here:  
👉 [Secure Data Vault – Streamlit App]()

> Use the default credentials to log in and test:
> - Username: `mueza`  
> - Password: `862001`


🙌 Author
Developed by: Mueza


