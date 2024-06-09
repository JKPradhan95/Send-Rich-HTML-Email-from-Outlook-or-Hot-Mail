import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = "senderdemo@gmail.com"
receiver = "receiverdemo@gmail.com"
password = "password123"

message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = "Hello Again!"

body = """
<h2>Hi there!</h2>
There are only a few things you need to do to get this email to you.
"""
mimetext = MIMEText(body, 'html')
message.attach(mimetext)

server = None

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(sender, password)

    message_text = message.as_string()
    server.sendmail(sender, receiver, message_text)
    print("Email sent successfully")

except smtplib.SMTPAuthenticationError:
    print("Failed to login. Check your username and password.")
except smtplib.SMTPConnectError:
    print("Failed to connect to the SMTP server. Check the server address and port.")
except smtplib.SMTPException as e:
    print(f"An error occurred: {e}")
finally:
  if server is not None:
    server.quit()
