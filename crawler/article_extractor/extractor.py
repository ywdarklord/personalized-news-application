__author__ = 'dungdt'

import re
from crawler.data.article import Article

class Extractor:
    wsPattern = re.compile(r'\s+')

    def __init__(self):
        ''

    def process(self, webpage):
        webpage.html = self.clean(webpage.html)

        article = self.createArticle(webpage)
        article = self.extractArticle(article)

        return article

    # clean html
    def clean(self, html):
        html = self.wsPattern.sub(' ', html)

        return html

    def createArticle(self, webpage):
        article = Article()

        article.set('uniqueId', webpage.uniqueId)
        article.set('publisher', webpage.publisher)
        article.set('title', webpage.title)
        article.set('url', webpage.url)
        article.set('image', webpage.image)
        article.published = str(webpage.published)
        article.html = webpage.html

        return article

    def extractArticle(self, article):
        return article
