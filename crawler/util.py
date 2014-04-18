__author__ = 'dungdt'

import urllib2, re

validUrlPattern = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

def downloadUrl(url):
    data = None

    if isValidUrl(url):
        try:
            response = urllib2.urlopen(url)
            data = response.read()
        except urllib2.HTTPError as e:
            print e.code
            print e.reason
            pass
        except urllib2.URLError as e:
            print e.message
            pass

    return data

def isValidUrl(url):
    if not validUrlPattern.search(url):
        return False

    return True