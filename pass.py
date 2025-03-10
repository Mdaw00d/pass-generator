import streamlit as st  # Import Streamlit for creating the web-based UI
import random  # Import random for generating random choices
import string  # Import string to use predefined character sets

# Function to generate a random password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Includes uppercase and lowercase letters

    if use_digits:
        characters += string.digits  # Adds numbers (0-9) if selected

    if use_special:
        characters += string.punctuation  # Adds special characters (!@#$%^&* etc.) if selected

    # Generate a password by randomly selecting characters based on the length provided
    return "".join(random.choice(characters) for _ in range(length))

# Streamlit UI setup with custom styling
st.markdown(
    """
    <style>
    .main-title { color: #4CAF50; text-align: center; font-size: 36px; font-weight: bold; }
    .password-box { font-size: 22px; font-weight: bold; color: #FFFFFF; background-color: #333333; padding: 10px; border-radius: 8px; text-align: center; }
    .slider-label { font-size: 18px; font-weight: bold; color: #333333; }
    .checkbox-label { font-size: 16px; color: #555555; }
    .button-style { background-color: #4CAF50; color: white; font-size: 18px; border-radius: 8px; padding: 10px; text-align: center; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<p class="main-title">🔒 SecurePass Generator</p>', unsafe_allow_html=True)

# User input: password length (slider to select length between 6 and 32 characters)
length = st.slider("Select password length:", min_value=6, max_value=32, value=12)

# Checkbox options for including numbers and special characters in the password
use_digits = st.checkbox("Include numbers")
use_special = st.checkbox("Include special characters")

# Button to generate password
if st.button("Generate Password", key="generate", help="Click to generate a secure password"):
    password = generate_password(length, use_digits, use_special)  # Call the password generation function
    st.markdown(f'<p class="password-box">{password}</p>', unsafe_allow_html=True)  # Display the generated password
