__author__ = 'dungdt'

from extractor import Extractor
from bs4 import BeautifulSoup

class Reuters(Extractor):
    def extractArticle(self, article):
        soup = BeautifulSoup(article.html)

        articleImageContainer = soup.find(id='articleImage')

        if articleImageContainer:
            article.set('image', articleImageContainer.find(name='img').attrs['src'])

        articleContent = soup.find(id='articleText')

        if articleContent:
            article.contentHtml = self.clean(str(articleContent))
            article.content = self.clean(articleContent.text)


        return article