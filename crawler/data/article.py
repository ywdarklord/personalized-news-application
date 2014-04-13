__author__ = 'dungdt'

from entity import Entity

class Article (Entity):
    uniqueId = None
    publisher = None
    categories = None
    title = None
    url = None
    content = None
    contentHtml = None
    image = None
    rawCategories = None
    published = None

    def __str__(self):
        return '("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (self.uniqueId, self.publisher, self.categories, self.title, self.url, self.image, self.rawCategories, self.published)