import smtplib
import os

sender = "Private Person <mailtrap@demomailtrap.com>"
receiver = "A Test User <brunoropacheco@gmail.com>"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is a test e-mail message. gadfgdfgfdgfdgadfgdfagdfgadgadf"""

print(message)

with smtplib.SMTP("live.smtp.mailtrap.io", 587) as server:
    server.starttls()
    server.login("api", os.getenv('API_MAILTRAP'))
    server.sendmail(sender, receiver, message)