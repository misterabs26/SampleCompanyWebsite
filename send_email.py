import streamlit as st
import ssl, smtplib
from email.mime.text import MIMEText
import re

# from dotenv import load_dotenv
# import os



# load_dotenv()

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def send_email(sender,topic_subj, message):
    host = "smtp.gmail.com"
    port = 465

    # use the code below only if you are using dotenv instead of streamlit secrets
    # admin_email = os.getenv("EMAIL_USER")
    # admin_pass = os.getenv("EMAIL_PASS")

    admin_email = st.secrets["email"]["EMAIL_USER"]
    admin_pass = st.secrets["email"]["EMAIL_PASS"]

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
            server.sendmail(admin_email,admin_email,msg.as_string())

            st.success("Your email was sent successfully!")
    else:
        st.error("Invalid Email")