import json
from pprint import pprint
from BatchWPScannerHelper import BatchWPScannerHelper

# Load configuration files from configuration.json
with open('configuration.json') as configurationFile:
    configuration = json.load(configurationFile)

# Where to send the report mail and from whom
to_mail = configuration['to_mail']
from_mail = configuration['from_mail']

# Get all urls from urls.json file
with open('urls.json') as urlsFile:
    urls = json.load(urlsFile)['urls']

# Loop through urls and send a simple email if vulns are detected
for url in urls:
    pprint('Scanning: ' + url)
    scan = BatchWPScannerHelper(url)
    result = scan.getResult()
    numberOfErrors = scan.getErrorCount(result)

    if numberOfErrors > 0:
        print(str(numberOfErrors) + ' vulnerabilities detected')
    scan.sendReportMail(to_mail, from_mail, result, 'Vulnerabilities detected on ' + url)



