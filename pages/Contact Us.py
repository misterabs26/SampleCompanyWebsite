import streamlit as st
from pathlib import Path
import pandas as pd
import send_email as se

# Get the script's directory
script_dir = Path(__file__).parent
file_path = script_dir.parent / "assets" / "topics.csv"

with open(file_path, "r") as data:
    df = pd.read_csv(data)

with st.form(key="email_forms"):
    sender_email = st.text_input("Enter your email:")
    topic = st.selectbox("Choose a topic",df["topic"])
    message = st.text_area("Enter your message:")
    submit_btn = st.form_submit_button("Submit")

    if submit_btn:
        if sender_email and message:
            se.send_email(sender_email,topic, message)
        else:
            st.warning("Please fill up the form.")