import subprocess
import smtplib
from email.mime.text import MIMEText

class BatchWPScanner:
    '''
    Constructor
    '''
    def __init__(self, url, execLocation):
        self.url = url
        self.execLocation = execLocation

    '''
    Do the actual scan
    '''
    def getResult(self):
        proc = subprocess.Popen(
            ['ruby', self.execLocation],
            stdout=subprocess.PIPE
        )
        result = proc.communicate()[0]
        return(result)

    '''
    How many errors (exclamation marks)
    '''
    def getErrorCount(self, result):
        result = str(result)
        return (result.count('[!]'))

    '''
    Send the report
    '''
    def sendReportMail(self, to_mail, from_mail, body, subject='Scan results'):
        msg = MIMEText(body, 'plain', 'UTF-8')
        msg['Subject'] = 'report'
        s = smtplib.SMTP('localhost')
        s.sendmail(from_mail, to_mail, msg.as_string())
        s.quit()

