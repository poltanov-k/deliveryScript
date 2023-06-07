#Библиотеки
import smtplib
import pandas as pd

#Логин и пароль от почты
email = 'k.poltanov@e-promo.ru'
password = '7Ds88u5imPM3J5k16'

#Чтение .csv файла, names - задаем названия колонок начиная с первой для скрипта
df = pd.read_csv('office7.csv', sep=';',
                 names=['email', 'ID'])

df.shape[0]

i=0
for i in range(275): #Начало цикла, range - количество строк в файле
    #Авторизация на сервере
    server = smtplib.SMTP('smtp.yandex.ru', 587)
    server.ehlo()
    server.starttls()
    server.login(email, password)
    #
    dest_email =df['email'][i] #Выбор почты
    subject = 'Your MS Office365 password' #Тема сообщения
    email_text = 'Hi, your MS Office365 password is ' + str(df['ID'][i]) #', password is '+str(df['pass'][i]) #Текст письма, подстановка логина и пароля
    message = 'From: %s\nTo: %s\nSubject: %s\n\n%s' % (email, dest_email, subject, email_text) #Составление письма, от кого, кому, тема, текст
    server.set_debuglevel(1) # Необязательно; так будут отображаться данные с сервера в консоли
    server.sendmail(email, dest_email, message) #Отправка
    server.quit() #Завершение коннекта с сервером
    i=i+1 #Следующая строка в файле