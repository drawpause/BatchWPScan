import json
from pprint import pprint
from src.classes.BatchWPScanner import BatchWPScanner

'''
Load configuration files
'''
with open('configuration.json') as configurationFile:
    configuration = json.load(configurationFile)

to_mail = configuration['to_mail']
from_mail = configuration['from_mail']

with open('urls.json') as urlsFile:
    urls = json.load(urlsFile)['urls']

# Just a loop test
for url in urls:
    pprint(url)

# @todo this stuff here
scan = BatchWPScanner('localhost')
result = scan.getResult()
numberOfErrors = scan.getErrorCount(result)

if numberOfErrors > 0:
    print(str(numberOfErrors) + ' vulnerabilities detected')

scan.sendReportMail(to_mail, from_mail, result)



