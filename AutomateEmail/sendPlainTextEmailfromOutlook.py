import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

sender = 'ashishlangote@icodexsolutions.com'
receiver = 'ashishlangote2002@gmail.com'
password = os.getenv('PASSWORDI')

message = """\
Subject: Hello Hello

This is Ardit!
Just wanted to say hi!
"""

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, message)
server.quit()
