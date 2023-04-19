import random, smtplib, schedule, time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

shirt = ['red UNIQLO shirt', 'white full sleve shirt', 'black NYT shirt', 'pink bird shirt', 'green long sleeve shirt', 'red striped button down', 'choice of collared t shirt']
pant = ['GAP blue jeans', 'white jeans', 'black sweatpants', 'black jeans', 'black ripped jeans', 'red sweatpants']
flare = ['black bucket hat', 'other bucket hat', 'anchor flannel shirt', 'unrolled sleeves', 'cuffed ankles', 'visible belt']
jacket = ['blue hoodie', 'green hoodie', 'green down jacket', 'black quarterzip', 'maroon hoodie shirt']

shirtnum = random.randrange(6)
pantnum = random.randrange(5)
flarenum = random.randrange(5)
jacketnum = random.randrange(4)

print(shirt[shirtnum])
print(pant[pantnum])
print(flare[flarenum])
print(jacket[jacketnum])
emailformat = 'Your outfit for today is a %s, %s, %s, and a %s!'

email = 'devingupta.dev@gmail.com'
password = '**********'
send_to_email = 'tsunamidev1@gmail.com'
subject = 'Email sent'
message = (emailformat % (shirt[shirtnum], pant[pantnum], flare[flarenum], jacket[jacketnum]))

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

def send_email_function():
    print("got to the function")
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, send_to_email, text)
    server.close()
    exit()

#schedule.every().day.at("18:32").do(send_email_function)
send_email_function()

while True:
   schedule.run_pending()
   time.sleep(1)
