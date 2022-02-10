import smtplib


def send_mail(email,password,message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email,email,message)

email = ""
password = ""
message = "hey Elisha how are you doing!!"
send_mail(email, password, message)
