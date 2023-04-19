import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = 'devingupta.dev@gmail.com'
password = '***********'
send_to_email = 'janhavir90@gmail.com'
subject = 'This is an automated message'
message = 'Hi Janhavi, Because you were mean to me, I am going to spam you with these emails. Thanks, Devin'

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)

text = msg.as_string()
server.sendmail(email, send_to_email, text)
server.quit()
