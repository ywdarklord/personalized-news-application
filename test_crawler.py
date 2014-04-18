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

        'http://feeds.reuters.com/news/artsculture?format=xml',
        'http://feeds.reuters.com/reuters/businessNews?format=xml',
        'http://feeds.reuters.com/ReutersBusinessTravel?format=xml',
        'http://feeds.reuters.com/reuters/companyNews?format=xml',
        'http://feeds.reuters.com/Counterparties?format=xml',
        'http://feeds.reuters.com/reuters/Election2012?format=xml',
        'http://feeds.reuters.com/reuters/entertainment?format=xml',
        'http://feeds.reuters.com/reuters/environment?format=xml',
        'http://feeds.reuters.com/reuters/healthNews?format=xml',
        'http://feeds.reuters.com/reuters/lifestyle?format=xml',
        'http://feeds.reuters.com/news/reutersmedia?format=xml',
        'http://feeds.reuters.com/news/wealth?format=xml',
        'http://feeds.reuters.com/reuters/MostRead?format=xml',
        'http://feeds.reuters.com/reuters/oddlyEnoughNews?format=xml',
        'http://feeds.reuters.com/ReutersPictures?format=xml',
        'http://feeds.reuters.com/reuters/peopleNews?format=xml',
        'http://feeds.reuters.com/Reuters/PoliticsNews?format=xml',
        'http://feeds.reuters.com/reuters/scienceNews?format=xml',
        'http://feeds.reuters.com/reuters/sportsNews?format=xml',
        'http://feeds.reuters.com/reuters/technologyNews?format=xml',
        'http://feeds.reuters.com/reuters/topNews?format=xml',
        'http://feeds.reuters.com/Reuters/domesticNews?format=xml',
        'http://feeds.reuters.com/Reuters/worldNews?format=xml',
        'http://feeds.reuters.com/reuters/bankruptcyNews?format=xml',
        'http://feeds.reuters.com/reuters/bondsNews?format=xml',
        'http://feeds.reuters.com/news/deals?format=xml',
        'http://feeds.reuters.com/news/economy?format=xml',
        'http://feeds.reuters.com/reuters/financialServicesrealEstateNews?format=xml',
        'http://feeds.reuters.com/reuters/globalmarketsNews?format=xml',
        'http://feeds.reuters.com/news/hedgefunds?format=xml',
        'http://feeds.reuters.com/reuters/hotStocksNews?format=xml',
        'http://www.reuters.com/rssFeed/newIssuesNews?format=xml',
        'http://feeds.reuters.com/reuters/mergersNews?format=xml',
        'http://feeds.reuters.com/reuters/privateequityNews?format=xml',
        'http://feeds.reuters.com/reuters/governmentfilingsNews?format=xml',
        'http://feeds.reuters.com/reuters/smallBusinessNews?format=xml',
        'http://feeds.reuters.com/reuters/summitNews?format=xml',
        'http://feeds.reuters.com/reuters/USdollarreportNews?format=xml',
        'http://feeds.reuters.com/news/usmarkets?format=xml',
        'http://feeds.reuters.com/reuters/basicmaterialsNews?format=xml',
        'http://feeds.reuters.com/reuters/cyclicalconsumergoodsNews?format=xml',
        'http://feeds.reuters.com/reuters/USenergyNews?format=xml',
        'http://feeds.reuters.com/reuters/environment?format=xml',
        'http://feeds.reuters.com/reuters/financialsNews?format=xml',
        'http://feeds.reuters.com/reuters/UShealthcareNews?format=xml',
        'http://feeds.reuters.com/reuters/industrialsNews?format=xml',
        'http://feeds.reuters.com/reuters/USmediaDiversifiedNews?format=xml',
        'http://feeds.reuters.com/reuters/noncyclicalconsumergoodsNews?format=xml',
        'http://feeds.reuters.com/reuters/technologysectorNews?format=xml',
        'http://feeds.reuters.com/reuters/UStechnologyTelcomNews?format=xml',
        'http://feeds.reuters.com/reuters/telecomsectorNews?format=xml',
        'http://feeds.reuters.com/reuters/utilitiesNews?format=xml',
        'http://feeds.reuters.com/reuters/blogs/AnthonyDerosa?format=xml',
        'http://feeds.reuters.com/reuters/blogs/reuters-dealzone?format=xml',
        'http://feeds.reuters.com/ChrystiaFreeland?format=xml',
        'http://feeds.reuters.com/reuters/reuters/blogs/DavidCayJohnston?format=xml',
        'http://feeds.reuters.com/reuters/blogs/reuters-dealzone?format=xml',
        'http://feeds.reuters.com/reuters/iOWg?format=xml',
        'http://feeds.reuters.com/reuters/blogs/entrepreneurial?format=xml',
        'http://feeds.reuters.com/reuters/blogs/Faithworld?format=xml',
        'http://feeds.reuters.com/reuters/blogs/felix-salmon?format=xml',
        'http://feeds.reuters.com/reuters/blogs/FinancialRegulatoryForum?format=xml',
        'http://feeds.reuters.com/reuters/blogs/for-the-record?format=xml',
        'http://feeds.reuters.com/reuters/blogs/FundsHub?format=xml',
        'http://feeds.reuters.com/reuters/blogs/GeorgeChen?format=xml',
        'http://feeds.reuters.com/reuters/blogs/GeraldineFabrikant?format=xml',
        'http://feeds.reuters.com/reuters/blogs/GlobalInvesting?format=xml',
        'http://feeds.reuters.com/reuters/blogs/HugoDixon?format=xml',
        'http://feeds.reuters.com/reuters/blogs/IanBremmer?format=xml',
        'http://feeds.reuters.com/reuters/blogs/India?format=xml',
        'http://feeds.reuters.com/reuters/blogs/jackshafer?format=xml',
        'http://feeds.reuters.com/reuters/blogs/JamesPethokoukis?format=xml',
        'http://feeds.reuters.com/reuters/blogs/JamesSaft?format=xml',
        'http://feeds.reuters.com/reuters/blogs/JohnCAbell?format=xml',
        'http://feeds.reuters.com/reuters/blogs/JohnWasik?format=xml',
        'http://feeds.reuters.com/LucyMarcus?format=xml',
        'http://feeds.reuters.com/reuters/blogs/LawrenceSummers?format=xml',
        'http://feeds.reuters.com/reuters/blogs/macroscope?format=xml',
        'http://feeds.reuters.com/reuters/blogs/mediafile?format=xml',
        'http://feeds.reuters.com/reuters/blogs/mohamedelerian?format=xml',
        'http://feeds.reuters.com/reuters/blogs/newsmaker?format=xml',
        'http://feeds.reuters.com/reuters/blogs/ReutersBreakingviews?format=xml',
        'http://feeds.reuters.com/reuters/blogs/reuters-editors?format=xml',
        'http://feeds.reuters.com/reuters/blogs/photo?format=xml',
        'http://feeds.reuters.com/reuters/blogs/SummitNotebook?format=xml',
        'http://feeds.reuters.com/reuters/blogs/talesfromthetrail?format=xml',
        'http://feeds.reuters.com/reuters/blogs/the-deep-end?format=xml',
        'http://feeds.reuters.com/reuters/blogs/the-great-debate?format=xml',
        'http://feeds.reuters.com/reuters/blogs/the-human-impact?format=xml',
        'http://feeds.reuters.com/reuters/blogs/taxbreak?format=xml',
        'http://feeds.reuters.com/UnstructuredFinance?format=xml',
        'http://feeds.reuters.com/reuters/USVideoBreakingviews?format=xml',
        'http://feeds.reuters.com/reuters/USVideoBusiness?format=xml',
        'http://feeds.reuters.com/reuters/USVideoBusinessTravel?format=xml',
        'http://feeds.reuters.com/reuters/USVideoChrystiaFreeland?format=xml',
        'http://feeds.reuters.com/reuters/USVideoEntertainment?format=xml',
        'http://feeds.reuters.com/reuters/USVideoEnvironment?format=xml',
        'http://feeds.reuters.com/reuters/USVideoFelixSalmon?format=xml',
        'http://feeds.reuters.com/reuters/USVideoGigaom?format=xml',
        'http://feeds.reuters.com/reuters/USVideoLifestyle?format=xml',
        'http://feeds.reuters.com/reuters/USVideoMostWatched?format=xml',
        'http://feeds.reuters.com/reuters/USVideoLatest?format=xml',
        'http://feeds.reuters.com/reuters/USVideoNewsmakers?format=xml',
        'http://feeds.reuters.com/reuters/USVideoOddlyEnough?format=xml',
        'http://feeds.reuters.com/reuters/USVideoPersonalFinance?format=xml',
        'http://feeds.reuters.com/reuters/USVideoPolitics?format=xml',
        'http://feeds.reuters.com/reuters/USVideoRoughCuts?format=xml',
        'http://feeds.reuters.com/reuters/USVideoSmallBusiness?format=xml',
        'http://feeds.reuters.com/reuters/USVideoTechnology?format=xml',
        'http://feeds.reuters.com/reuters/USVideoTopNews?format=xml',
        'http://feeds.reuters.com/reuters/USVideoWorldNews?format=xml',
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