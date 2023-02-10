import socket 
import smtplib
from time import sleep


#Obtener IP
i = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
i.connect(("8.8.8.8", 80))
IPAddr = i.getsockname()[0]

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("email login", "password email")

  
# sending the mail
s.sendmail("sender email", "receiver email", IPAddr)
  
# terminating the session
s.quit()

#Chequear constantemente la IP por cambios
while True:
    i = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    i.connect(("8.8.8.8", 80))
    IPAddr2 = i.getsockname()[0]

    if IPAddr2 != IPAddr:
        IPAddr = IPAddr2

        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login("email login", "password email")

        
        # sending the mail
        s.sendmail("sender email", "receiver email", IPAddr)
        
        # terminating the session
        s.quit()

    sleep(1800)