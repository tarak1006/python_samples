import smtplib
SUBJECT='SAMPLE MESSAGE'
TEXT='hii im tarak.you are selected for finals'

mail=smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()

mail.starttls()

mail.login('kandula.tarakaram@gmail.com','ammulu123')
message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
mail.sendmail('kandula.tarakaram@gmail.com','eswarkandula004@gmail.com',message)

mail.close()