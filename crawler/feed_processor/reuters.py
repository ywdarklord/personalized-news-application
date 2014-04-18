__author__ = 'dungdt'

from crawler.feed_processor.processor import Processor
from crawler.data.webpage import Webpage
from dateutil import parser

class Reuters(Processor):
    def process(self):
        root = self.feed.find('channel')

        feedTitle = root.find('title')
        rawCategories = feedTitle.text

        items = root.findall('item')
        webpages = []

        for item in items:
            webpage = Webpage()
            webpage.publisher = 'reuters'
            webpage.rawCategories = rawCategories

            for field in item.iter():
                if 'title' == field.tag:
                    webpage.set('title', field.text)
                elif 'guid' == field.tag:
                    webpage.set('url', field.text[:field.text.rfind('?')])
                elif 'pubDate' == field.tag:
                    webpage.set('published', parser.parse(field.text).strftime('%s'))
                elif 'enclosure' == field.tag:
                    webpage.set('image', field.attrib['url'])

            webpages.append(webpage)

        return webpages
