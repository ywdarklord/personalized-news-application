import xml.etree.ElementTree as ET
import util
from feed_processor import dailymail,reuters, nytimes

class FeedReader:
    FEED_DAILYMAIL  = 'dailymail'
    FEED_REUTERS    = 'reuters'
    FEED_NYTIMES    = 'nytimes'
    feedUrl = None
    feedType = None
    dbConnector = None

    def __init__(self, feedUrl, dbConnector):
        if 0 < feedUrl.find('dailymail.co.uk'):
            self.feedType = FeedReader.FEED_DAILYMAIL
        elif 0 < feedUrl.find('nytimes.com'):
            self.feedType = FeedReader.FEED_NYTIMES
        elif 0 < feedUrl.find('reuters.com'):
            self.feedType = FeedReader.FEED_REUTERS
            raise Exception('Invalid Feed Type')

        self.feedUrl = feedUrl
        self.dbConnector = dbConnector

    # Process feed
    def process(self):
        data = util.downloadUrl(self.feedUrl)
        webpages = []

        try:
            xml = ET.fromstring(data)
            processor = self.getFeedProcessor(xml)
            webpages = processor.process()
            for webpage in webpages:
                self.dbConnector.addWebpage(webpage)
        except ET.ParseError as e:
            pass

        return webpages

    def getFeedProcessor(self, xml):
        processor = None

        if FeedReader.FEED_DAILYMAIL == self.feedType:
            processor = dailymail.Dailymail(xml)
        elif FeedReader.FEED_DAILYMAIL == self.feedType:
            ''
        elif FeedReader.FEED_DAILYMAIL == self.feedType:
            ''

        return processor
