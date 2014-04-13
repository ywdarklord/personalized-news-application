__author__ = 'dungdt'

from crawler import feed_reader
from crawler.data import db_connector
from crawler import html_downloader

if __name__ == '__main__':
    dbConnector = db_connector.DbConnector()
    feedReader = feed_reader.FeedReader('http://www.dailymail.co.uk/sport/index.rss', dbConnector)

    articles = feedReader.process()
    #
    #
    # articles = dbConnector.getUndownloadedArticles(10)
    # print articles

    # downloader = html_downloader.HtmlDownloader()
    # downloader.run()