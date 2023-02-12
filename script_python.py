"""#!/usr/bin/python2.4
# -*- coding: utf-8 -*-"""

from skpy import Skype
import requests
import smtplib

# Mail #

EMAIL_ADRESS = ("example@example.com")
EMAIL_PASSWORD = ("password")

# Telegram Send Message Function #

def telegram_send_msg(text):
    token = "token"
    chat_id = "chat_id"

    url_req = "https://api.telegram.org/bot"+ token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    return results.json()

# Skype Send Message Function #

def skype_send_msg():
    sk = Skype("example@example.com", "password") # connect to Skype

    contact = sk.contacts["Contact Adress"]
    contact.chat.sendMsg("Your Message")

#Send Mail Function

def notify_user():
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)

        subject = "Example Subject"
        body = "Example Body"
        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(EMAIL_ADRESS, "example@example.com", msg)


notify_user()
skype_send_msg()
telegram_send_msg("Your Message")
