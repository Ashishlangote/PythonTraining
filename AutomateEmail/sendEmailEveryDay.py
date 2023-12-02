import yagmail
import os
import time
from datetime import datetime as dt
from dotenv import load_dotenv

load_dotenv()

sender = 'ashishlangote2002@gmail.com'
receiver = 'mibek73749@bikedid.com'

subject = """
This is the subject!
"""
contents = """
Here is the content of the email! 
Hi!
"""
while True:
  now = dt.now()
  if now.hour == 13 and now.minute == 18:
    yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email Sent!")
    time.sleep(60)