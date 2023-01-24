import smtplib
import datetime as dt
import random

my_email= 'gowthamyupy@gmail.com'
password= 'puajhrkvgykdrqpd'
now= dt.datetime.now()
weekday= now.weekday()
if weekday==1:
    with open('quotes.txt', 'r') as quote:
        all_quotes = quote.readlines()
        my_quote = random.choice(all_quotes)
        print(my_quote)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs='gowtham.yu@yahoo.com',
                            msg=f'Subject:Monday Motivation\n\n {my_quote}')


