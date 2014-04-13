__author__ = 'dungdt'

from crawler import feed_reader
from crawler.data import db_connector
import time

if __name__ == '__main__':
    dbConnector = db_connector.DbConnector()
    feedReader = feed_reader.FeedReader('http://www.dailymail.co.uk/sport/index.rss', dbConnector)

    feedReaders = []
    feedLinks = [
        'http://www.dailymail.co.uk/home/index.rss',
        'http://www.dailymail.co.uk/news/index.rss',
        'http://www.dailymail.co.uk/sport/index.rss',
        'http://www.dailymail.co.uk/tvshowbiz/index.rss',
        'http://www.dailymail.co.uk/femail/index.rss',
        'http://www.dailymail.co.uk/health/index.rss',
        'http://www.dailymail.co.uk/sciencetech/index.rss',
        'http://www.dailymail.co.uk/money/index.rss',
        'http://www.dailymail.co.uk/video/index.rss',
        'http://www.dailymail.co.uk/travel/index.rss',
        'http://www.dailymail.co.uk/femail/fashionfinder/index.rss',
    ]

    # init the feed reader
    for feedLink in feedLinks:
        feedReader = feed_reader.FeedReader(feedLink, dbConnector)
        feedReaders.append(feedReader)

    # process to retrieve the webpage
    while True:
        for feedReader in feedReaders:
            print 'Crawling %s' %(feedReader.feedUrl)
            feedReader.process()

        # sleep for 5 minutes
        print 'Sleeping for %s seconds' %(300)
        time.sleep(300)
    #
    #
    # articles = dbConnector.getUndownloadedArticles(10)
    # print articles

    # downloader = html_downloader.HtmlDownloader()
    # downloader.run()