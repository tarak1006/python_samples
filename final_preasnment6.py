import smtplib
import MySQLdb
import click

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
@click.command()
@click.argument('college_acronym',nargs=1)
def cli(college_acronym):
    db = MySQLdb.connect(host="localhost", user="root",
                         passwd="kandula123")

    totalmesg='------REPORT------\n\n'
    c = db.cursor()
    c.execute("USE eswar")
    totalmesg+='list of %s students and their scores\n\n'%college_acronym
    sql="SELECT students.COLLEGE,students.NAME,marks.TOTAL FROM MARKS LEFT JOIN STUDENTS ON MARKS.ID = STUDENTS.ID  HAVING COLLEGE='%s'"%college_acronym
    c.execute(sql)
    result=c.fetchall()
    for row in result:
        totalmesg+='{} {}  {}\n'.format(row[0],row[1],row[2])
    totalmesg+='\n\n%s summary\n'%college_acronym
    sql = "SELECT students.COLLEGE,COUNT(marks.ID),MIN(marks.TOTAL),MAX(marks.TOTAL),AVG(marks.TOTAL)  FROM marks \
    LEFT JOIN students ON marks.ID = students.ID GROUP BY COLLEGE HAVING COLLEGE='%s'"%college_acronym
    c.execute(sql)
    result_marks = c.fetchall()
    print result_marks
    for row in result_marks:
        totalmesg += '{} {}  {} {} {}\n'.format(row[0], row[1], row[2],row[3],row[4])
    #graph





    totalmesg+='\n\nGlobal summary\n'
    totalmesg+='%s college students has done well'%college_acronym
    fromadd = ""
    toadd =""
    msg = MIMEMultipart()
    msg['From'] = fromadd
    msg['To'] = toadd
    msg['Subject'] = "sample message "

    msg.attach(MIMEText(totalmesg, 'plain'))

    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()

    mail.login(fromadd, 'ammulu123')
    text = msg.as_string()
    mail.sendmail(fromadd, toadd, text)

    mail.close()
if __name__=='__main__':
    cli()