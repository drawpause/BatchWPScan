import subprocess
import smtplib
from email.mime.text import MIMEText

class BatchWPScanner:
    """
    A helper class for BatchWPScan
    """

    def __init__(self, url):
        """
        Constructor
        :type url: string
        :type execLocation: string
        :return:
        """
        self.url = url


    def getResult(self):
        """
        Do the actual scan
        :return: string
        """
        proc = subprocess.Popen(
            ['docker', 'run', '--rm', 'wpscanteam/wpscan', '--update', '-u', self.url, '--enumerate', 'vt,vp,u'],
            stdout=subprocess.PIPE
        )
        result = proc.communicate()[0]
        return(result)

    def getErrorCount(self, result):
        """
        Count the errors in the scan (exclamation marks)
        :param result:
        :return: int
        """
        result = str(result)
        return (result.count('[!]'))

    def sendReportMail(self, to_mail, from_mail, body, subject='Scan results'):
        """
        Send the report via email
        :param to_mail: Receiver address
        :param from_mail: Sender address
        :param body: Scanner output text
        :param subject: Subject line
        :return:
        """
        msg = MIMEText(body, 'plain', 'UTF-8')
        msg['Subject'] = subject
        s = smtplib.SMTP('localhost')
        s.sendmail(from_mail, to_mail, msg.as_string())
        s.quit()

