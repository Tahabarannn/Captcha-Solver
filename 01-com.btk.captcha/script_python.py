"""#!/usr/bin/python2.4
# -*- coding: utf-8 -*-"""

from skpy import Skype
import smtplib

# Mail #

EMAIL_ADRESS = ("murat.betzmark@gmail.com")
EMAIL_PASSWORD = ("htoufixzpimiplar")

# Telegram Send Message Function #

"""def telegram_send_msg(text):
    token = "5214184413:AAGrsAg60zryA2RaQY9Q70hXe95JCs54wMY"
    chat_id = "-615178408"

    url_req = "https://api.telegram.org/bot"+ token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    return results.json()"""

# Skype Send Message Function #

def skype_send_msg():
    sk = Skype("betzmarkdomain@hotmail.com", "Murat.2021") # connect to Skype

    contact = sk.contacts["live:.cid.5e8d43fee02f5d9f"]
    """contact1 = sk.contacts["live:.cid.77ddaa2cf6559d06"]"""
    """contact2 = sk.contacts["live:.cid.5530a8bc7de87fac"]
    contact3 = sk.contacts["live:cakiir.atilla"]"""
    contact.chat.sendMsg("Test")
    """contact1.chat.sendMsg("Test")"""
    """contact2.chat.sendMsg("Test")
    contact3.chat.sendMsg("Test")"""

#Send Mail Function

def notify_user():
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)

        subject = "DOMAINDE HATA ALGILANDI"
        body = "DOMAIN CALISMIYOR!!!"
        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(EMAIL_ADRESS, "tahabarann@hotmail.com", msg)


notify_user()
skype_send_msg()       