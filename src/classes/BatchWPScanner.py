import subprocess
import smtplib
from email.mime.text import MIMEText
class BatchWPScanner:
    '''
    Constructor
    '''
    def __init__(self, url):
        self.url = url

    def getResult(self):
        proc = subprocess.Popen(
            'ruby /home/wtfh4x/Sources/wpscan/wpscan.rb'.split(),
            stdout=subprocess.PIPE
        )
        result = proc.communicate()[0]
        return(result)

    def getErrorCount(self, result):
        result = str(result)
        return (result.count('[!]'))

    def sendReportMail(self, receiver, body):
        # me == the sender's email address
        # you == the recipient's email address
        msg = MIMEText(body, 'plain', 'UTF-8')
        msg['Subject'] = 'report'
        msg['From'] = 'henri.kuittinen@icloud.com'
        msg['To'] = 'nitret@gmail.com'

        # Send the message via our own SMTP server, but don't include the
        # envelope header.
        s = smtplib.SMTP('localhost')
        s.sendmail('henri.kuittinen@icloud.com', 'nitret@gmail.com', msg.as_string())
        s.quit()

