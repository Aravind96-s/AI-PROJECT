import smtplib
sever =smtplib.SMTP('smtp@gmail.com',587)
sever.starttls()
sever.login('aravindrudra1996@gmail.com','Aravind@23#')
sever.sendmail('aravindrudra1996@gmail.com','awsdemolearn24@gmail.com','demo mail')