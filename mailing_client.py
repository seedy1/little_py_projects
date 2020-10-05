import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

from secret import EMAIL, PASSWORD # secret file with user email and password

server = smtplib.SMTP('smtp.gmail.com', 25) # replace gmail with your email provider
server.ehlo()
server.login(EMAIL, PASSWORD)

msg = MIMEMultipart()
msg["From"] = "from"
msg["To"] = "info@doamin.com"
msg["Subject"] = "Testing"
msg["Message"] = "A long message"

msg.attach() # to attach a file
file_to_send = ".jpg"
attachment = open(file_to_send, 'rb') # to send 0s and 1s
p_load = MIMEBase("application", "octet-stream")
p_load.set_payload( (attachment.read()) )

encoders.encode_base64(p_load)
p_load.add_header("Content-Disposition", f"attachment; filename={file_to_send}")
msg.attach(p_load)

text = msg.as_string()

server.sendmail("email_from", "email_to", msg)
