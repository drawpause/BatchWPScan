import subprocess
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