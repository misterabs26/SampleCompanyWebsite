import streamlit as st
import os
import ssl, smtplib
from dotenv import load_dotenv
import re
from email.mime.text import MIMEText

load_dotenv()

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def send_email(sender,topic_subj, message):
    host = "smtp.gmail.com"
    port = 465

    admin_email = os.getenv("USER_EMAIL")
    admin_pass = os.getenv("USER_PW")

    if validate_email(sender):
        subject = topic_subj
        sender_email = sender
        body = f"""
            You got a message from {sender_email}:
            
            {message}
        """

        msg = MIMEText(body)
        msg["From"] = sender_email
        msg["To"] = admin_email
        msg["Subject"] = subject
        msg["Reply-To"] = sender_email

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(host,port,context=context) as server:
            server.login(admin_email,admin_pass)
            server.sendmail(admin_email,admin_email,message.as_string())

            st.info("Your email was sent successfully!")
    else:
        st.warning("Invalid Email")