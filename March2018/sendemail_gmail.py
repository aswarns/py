#!//usr/bin/env python3

#referance from https://github.com/codingforentrepreneurs/30-Days-of-Python/blob/master/Day%2012/day_12_start.py


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


#only for gmail account only
host = "smtp.gmail.com"
port = 587
#username = "USER_NAME@gmail.com"
#password = "PASSWORD"
from_email = username
to_list = "babaji.vines@gmail.com"

email_conn = smtplib.SMTP(host,port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username,password)

the_msg = MIMEMultipart("alternative")
the_msg['Subject'] = "hello There"
the_msg["From"] = from_email
#the_msg["to"] = to_list

plain_txt = "Testing the message"
html_txt = """\
<html>
  <head></head>
  <body>
    <p> hey!<br>
      Testing this email <b>message</b>. Made by Ashish Singh.
    </p>
  </body>
</html>
"""
part_1 = MIMEText(plain_txt,'plain')
part_2 = MIMEText(html_txt,'html')

the_msg.attach(part_1)
the_msg.attach(part_2)

#print(the_msg.as_string())

email_conn.sendmail(from_email,to_list, the_msg.as_string())
email_conn.quit()



