#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText


msg = MIMEText("This is mail test")
msg["Subject"] = "Test mail"
msg["From"] = "test@test.com"
msg["To"] = "daniel@test.com"

with smtplib.SMTP("127.0.0.1:1025") as t:
    t.login("mailhog", "")
    t.sendmail("test@test.com", "daniel@test.com", msg.as_string())
