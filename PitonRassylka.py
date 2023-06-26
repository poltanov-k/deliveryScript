import smtplib
import pandas as pd

email = 'k.poltanov@e-promo.ru'
password = '7Ds88u5imPM3J5k16'

df = pd.read_csv('office7.csv', sep=';',
                 names=['email', 'ID'])

df.shape[0]

i=0
for i in range(275):
    server = smtplib.SMTP('smtp.yandex.ru', 587)
    server.ehlo()
    server.starttls()
    server.login(email, password)
    dest_email =df['email'][i]
    subject = 'Your MS Office365 password'
    email_text = 'Hi, your MS Office365 password is ' + str(df['ID'][i]) #', password is '+str(df['pass'][i]) 
    message = 'From: %s\nTo: %s\nSubject: %s\n\n%s' % (email, dest_email, subject, email_text) 
    server.set_debuglevel(1) 
    server.sendmail(email, dest_email, message)
    server.quit()
    i=i+1
