__author__ = 'dungdt'

from extractor import Extractor
from bs4 import BeautifulSoup

class Dailymail(Extractor):
    def extractArticle(self, article):
        soup = BeautifulSoup(article.html)

        articleContainer = soup.find(id='js-article-text')
        metaImage = soup.find(name='meta', attrs={'property': 'og:image'})

        if 'content' in metaImage.attrs:
            article.set('image', metaImage.attrs['content'])

        for el in articleContainer.findAll(['script', 'style']):
            el.extract()

        ignoredTags = ['h1', 'script', 'style']
        article.content = article.contentHtml = ''

        for content in articleContainer.contents:
            if content.name != None:
                if content.name in ignoredTags:
                    continue

                if 'id' in content.attrs and content.attrs['id'] == 'taboola-below-main-column':
                    break
                article.content += ' ' + self.clean(content.text.strip())
                article.contentHtml += '\n' + self.clean(str(content))

        return article