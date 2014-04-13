__author__ = 'dungdt'

import urllib2

def downloadUrl(url):
    data = None
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