__author__ = 'dungdt'

from crawler.article_extractor import dailymail
import re
from bs4 import BeautifulSoup

if __name__ == '__main__':
    f = open('test.html', 'r')
    html = f.read()
    html = html
    soup = BeautifulSoup(html)
    articleContainer = soup.find(id='js-article-text')
    metaImage = soup.find(name='meta', attrs={'property': 'og:image'})

    if 'content' in metaImage.attrs:
        image = metaImage.attrs['content']
        print image

    for el in articleContainer.findAll(['script', 'style']):
        el.extract()

    html = ''
    text = ''
    ignoredTags = ['h1', 'script', 'style']

    for content in articleContainer.contents:
        if content.name != None:
            if content.name in ignoredTags:
                continue

            if 'id' in content.attrs and content.attrs['id'] == 'taboola-below-main-column':
                break
            text += ' ' + ' '.join(content.text.strip().encode('utf-8').split())
            html += '\n' + str(content)


    # print html
    # print text


