import random
import smtplib
import datetime as dt

my_email = "bendzandu117@gmail.com"
password = "ThisIsATest"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quote = quote_file.readlines()
        quote = random.choice(all_quote)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="bendzandu117@yahoo.com",
                            msg=f"Subject:Monday Words of Wisdom\n\n{quote}")

