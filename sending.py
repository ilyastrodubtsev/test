import smtplib as smtp
from getpass import getpass
import requests
import time
import datetime

def sendmail():
	email = "kent-brokmen4@yandex.ru"#input('введите почту: \n')
	password = "HaCker1996_1997_2012_2013"#getpass('введите пароль: ')
	dest_email = "trytoaccept@yandex.ru"#input('введите адрес получателя: \n')
	subject = "CRASH"#input('тема письма: \n')
	email_text = "Something's broken now"#input('текст письма: \n' )

	message = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format(email,
		                                               dest_email, 
		                                               subject, 
		                                               email_text)

	server = smtp.SMTP_SSL('smtp.yandex.com')
	server.set_debuglevel(1)
	server.ehlo(email)
	server.login(email, password)
	server.auth_plain()
	server.sendmail(email, dest_email, message)
	server.quit()


def writefile(s):
	f = open('log.txt', 'a')
	f.write(s + '\n')
	f.close()

while True:
	request = requests.get('https://app.scanz.com')
	#request = requests.get('https://raspberrypi.local/', verify=False)
	if request.status_code == 200:
		#print('Web site exists')
		s = "Web site exists " + str(datetime.datetime.now())
		writefile(s)
		time.sleep(15)
	else:
		print('Web site does not exist')
		s = "NOT exists " + str(datetime.datetime.now())
		writefile(s)
		sendmail()
		time.sleep(600)
