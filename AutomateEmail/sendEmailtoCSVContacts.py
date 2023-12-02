import yagmail
import os
import pandas
from dotenv import load_dotenv

load_dotenv()

sender = 'ashishlangote2002@gmail.com'

subject = """
This is the subject!
"""

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))

df = pandas.read_csv('contacts.csv')

for index, row in df.iterrows():
    contents = f"""Hi {row['name']} the content of the email! Hi!"""
    yag.send(to=row['email'], subject=subject, contents=contents)
    print("Email Sent!")
