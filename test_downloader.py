__author__ = 'dungdt'

from crawler import html_downloader
from crawler.data import db_connector

if __name__ == '__main__':
    dbConnector = db_connector.DbConnector()
    downloader = html_downloader.HtmlDownloader(dbConnector)
    downloader.run()