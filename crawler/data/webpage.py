__author__ = 'dungdt'

from entity import Entity

class Webpage(Entity):
    STT_CREATED = 0
    STT_DOWNLOADING = 1
    STT_DOWNLOADED = 2
    STT_EXTRACTED = 3

    id = None
    uniqueId = None
    status = None
    url = None
    title = None
    image = None
    publisher = None
    created = None
    published = None
    tries = None
    rawCategories = None

    def __init__(self, data = {}):
        self.status = self.STT_CREATED

        if 'id' in data:
            self.id = data['id']

        if 'unique_id' in data:
            self.uniqueId = data['unique_id']

        if 'status' in data:
            self.status = data['status']

        if 'url' in data:
            self.url = data['url']

        if 'title' in data:
            self.title = data['title']

        if 'image' in data:
            self.image = data['image']

        if 'publisher' in data:
            self.publisher = data['publisher']

        if 'tries' in data:
            self.tries = data['tries']

        if 'published' in data:
            self.published = data['published']

        if 'raw_categories' in data:
            self.rawCategories = data['raw_categories']


    def __str__(self):
        return '("%s", "%s", "%s", "%s", "%s")' % (self.title, self.url, self.publisher, self.published, self.image)
