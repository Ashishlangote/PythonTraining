import yagmail
import os
from dotenv import load_dotenv

load_dotenv()

sender = 'ashishlangote2002@gmail.com'
receiver = 'mibek73749@bikedid.com'

subject = "This is the subject!"

contents = """
Here is the content of the email! 
Hi!
"""

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
yag.send(to=receiver, subject=subject, contents=contents)
print("Email Sent!")
