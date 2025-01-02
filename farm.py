

import time
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
import imaplib

import pymysql as mdb
import serial

port = serial.Serial("COM8", baudrate=9600, timeout=1)
port1 = serial.Serial("COM5", baudrate=9600, timeout=1)

def mails(cc):
    print('kk')
    fromaddr = "sur5gk@gmail.com"
    password='dgrb obcg nqjn ntwt'
    toaddr = 'sur5gk@gmail.com'
    msg = MIMEMultipart() 
    msg['From'] = fromaddr 
    msg['To'] = 'sur5gk@gmail.com'
    # storing the subject 
    msg['Subject'] = "Emergency please chk photo"
    # string to store the body of the mail 
    body = cc
    msg.attach(MIMEText(body, 'plain'))
    filename='1.png'
    filename = filename
    attachment = open(filename, "rb") 
    p = MIMEBase('application', 'octet-stream') 

    p.set_payload((attachment).read()) 


    encoders.encode_base64(p) 

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 

    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 

    # start TLS for security 
    s.starttls() 

    # Authentication 
    s.login(fromaddr, password) 

    # Converts the Multipart msg into a string 
    text = msg.as_string() 

    # sending the mail 
    s.sendmail(fromaddr, toaddr, text)
    print('email done')
    
 
def cap():
    import cv2


    video = cv2.VideoCapture('http://192.168.2.4:8080/video') 


    check, frame = video.read()
    print(check)   
    showPic = cv2.imwrite("1.png",frame)
    video.release()
    print('capture image')
    
#mails('')
while True:
     valu=port.readline().decode()
     #print (valu)
     if valu!="":
       try:
           x,lat,lon,temp=valu.split(',')
           print ("temperature",temp,"Latitude",lat,"longitude",lon,"x",x)
           temp=float(temp)
           x=float(x)
           if temp>40 or x<6:
               print('sending email')
               cap()
               mails(lat+'----'+lon)
       except:
           print('r')
     val=port1.readline().decode()
     #print (valu)
     if val!="":
       try:
           sys,dia,pr=val.split(',')
           print ("Systolic",sys,"Diastolic",dia,"Pulserate",pr)
       except:
           print('r')
           
             
    
     
    
       
     
