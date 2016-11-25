import json
from pprint import pprint
from src.classes.BatchWPScanner import BatchWPScanner

# Load configuration files from configuration.json
with open('configuration.json') as configurationFile:
    configuration = json.load(configurationFile)

# Where to send the report mail and from whom
to_mail = configuration['to_mail']
from_mail = configuration['from_mail']

# Get all urls from urls.json file
with open('urls.json') as urlsFile:
    urls = json.load(urlsFile)['urls']

# Just a loop test
for url in urls:
    pprint(url)

# @todo the actual scan and queue
for url in urls:
    pprint('Scanning: ' + url)
    scan = BatchWPScanner(url)
    result = scan.getResult()
    numberOfErrors = scan.getErrorCount(result)

    if numberOfErrors > 0:
        print(str(numberOfErrors) + ' vulnerabilities detected')
    scan.sendReportMail(to_mail, from_mail, result)



