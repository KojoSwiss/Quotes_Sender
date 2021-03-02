import smtplib

my_email = "bendzandu117@gmail.com"
password = "ThisIsATest"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="bendzandu117@yahoo.com",
                        msg="Subject:The Second\n\nThis is the body of the email")
