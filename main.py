import smtplib

sender = "senderdemo@gmail.com"
receiver = "receiverdemo@gmail.com"
password = "password123"

message = """\
 Subject : Hello Hello 
 
 This is jay
 Just wanted to say hi!"""

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender,password)
server.sendmail(sender, receiver, message)
server.quit()