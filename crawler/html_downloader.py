__author__ = 'dungdt'

import time
import util
from data import db_connector
import article_extractor.dailymail
from data.webpage import Webpage

class HtmlDownloader:
    dbConnector = None
    dailymailExtractor = None

    def __init__(self, dbConnector):
        self.dbConnector = dbConnector
        self.dailymailExtractor = article_extractor.dailymail.Dailymail()

    def run(self):
        while True:
            webpages = self.dbConnector.getUndownloadedWebpages(10)

            if not webpages:
                self.sleep(10)

            print 'Downloading %d articles with IDs: (%s)' % (len(webpages), ','.join([str(webpage.id) for webpage in webpages]))

            for webpage in webpages:
                self.dbConnector.updateWebpageStatus(webpage.id, Webpage.STT_DOWNLOADING)
                html = util.downloadUrl(webpage.url)
                webpage.html = html
                article = self.dailymailExtractor.process(webpage)
                self.dbConnector.addArticle(article)
                self.dbConnector.updateWebpageStatus(webpage.id, Webpage.STT_EXTRACTED)

    # sleep for {seconds} seconds
    def sleep(self, seconds):
        print 'HTML Downloader sleeping for %d seconds' % (seconds)
        time.sleep(seconds)

