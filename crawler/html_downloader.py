
__author__ = 'dungdt'

import time
import util
from article_extractor import dailymail, reuteres
from data.webpage import Webpage
from feed_reader import FeedReader

class HtmlDownloader:
    dbConnector = None
    dailymailExtractor = None

    def __init__(self, dbConnector):
        self.dbConnector = dbConnector
        self.dailymailExtractor = dailymail.Dailymail()
        self.reutersExtractor = reuteres.Reuters()

    def run(self):
        while True:
            webpages = self.dbConnector.getUndownloadedWebpages(10)

            if not webpages:
                self.sleep(10)

            print 'Downloading %d articles with IDs: (%s)' % (len(webpages), ','.join([str(webpage.id) for webpage in webpages]))

            for webpage in webpages:
                self.dbConnector.updateWebpageStatus(webpage.id, Webpage.STT_DOWNLOADING)

                print '==Extracting %s' %(webpage.url)
                html = util.downloadUrl(webpage.url)

                if html:
                    webpage.html = html

                    if webpage.publisher == FeedReader.FEED_DAILYMAIL:
                        article = self.dailymailExtractor.process(webpage)
                    elif webpage.publisher == FeedReader.FEED_REUTERS:
                        article = self.reutersExtractor.process(webpage)
                    elif webpage.publisher == FeedReader.FEED_NYTIMES:
                        article = self.dailymailExtractor.process(webpage)

                    if article:
                        self.dbConnector.addArticle(article)
                        self.dbConnector.updateWebpageStatus(webpage.id, Webpage.STT_EXTRACTED)
                else:
                    self.dbConnector.updateWebpageStatus(webpage.id, Webpage.STT_CREATED)

    # sleep for {seconds} seconds
    def sleep(self, seconds):
        print 'HTML Downloader sleeping for %d seconds' % (seconds)
        time.sleep(seconds)

