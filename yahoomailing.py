import smtplib

my_email = "bendzandu117@yahoo.com"
password = "diqhloagrvjkibci"

with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="bendzandu117@gmail.com",
                        msg="Subject:Again\n\nThis is the body of the email")










