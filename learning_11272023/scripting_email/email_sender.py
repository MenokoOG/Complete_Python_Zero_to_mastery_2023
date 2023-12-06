"""Email with python, Menoko OG, 11-2023"""
import smtplib
from email.message import EmailMessage

email = EmailMessage()
email["from"] = "Menoko OG"
email["to"] = "menokoog@gmail"
email["subject"] = "You won the universe dude!!!"

email.set_content("I am a python Lord!")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("menokoog@gmail.com", "LUXgirl24!!andMenoko51@@")
    smtp.send_message(email)
    print("All good here!!!")