__author__ = 'dungdt'


import mysql.connector
import datetime, hashlib
from crawler.data.webpage import Webpage


class DbConnector:
    cnx = None

    # constructor
    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', password='dungdt88', database='pnp')

    # destructor
    def __del__(self):
        self.cnx.close()

    # add a new webpage to db
    def addWebpage(self, webpage):
        cursor = self.cnx.cursor()

        insertQuery = (
            "INSERT IGNORE INTO `webpage` (`unique_id`, `status`, `url`, `title`, `image`, `raw_categories`, `publisher`, `created`, `published`) "
            "VALUES (%(uniqueId)s, %(status)s, %(url)s, %(title)s, %(image)s, %(rawCategories)s, %(publisher)s, now(), %(published)s)")

        insertData = {
            'uniqueId': hashlib.sha256(webpage.url).hexdigest(),
            'status': int(webpage.status),
            'title': webpage.title,
            'image': webpage.image,
            'rawCategories': webpage.rawCategories,
            'url': webpage.url,
            'publisher': webpage.publisher,
            'published': datetime.datetime.fromtimestamp(int(webpage.published)).strftime('%Y-%m-%d %H:%M:%S')
        }

        cursor.execute(insertQuery, insertData)
        self.cnx.commit()
        cursor.close()

    # Update html of an webpage
    def updateWebpageHtml(self, id, html):
        cursor = self.cnx.cursor()

        updateQuery = (
            "UPDATE `webpage`"
            "SET `html` = %s,"
            "`tries` = tries + 1,"
            "`status` = %s "
            "WHERE `id` = %s"
        )

        cursor.execute(updateQuery, (html, Webpage.STT_DOWNLOADED, int(id)))
        self.cnx.commit()
        cursor.close()

    #
    def updateWebpageStatus(self, id, status):
        cursor = self.cnx.cursor()

        if status == Webpage.STT_DOWNLOADING:
            updateQuery = (
                "UPDATE `webpage` "
                "SET `status` = %s,"
                "    `tries` = `tries` + 1 "
                "WHERE `id` = %s"
            )
        else:
            updateQuery = (
                "UPDATE `webpage` "
                "SET `status` = %s "
                "WHERE `id` = %s"
            )

        cursor.execute(updateQuery, (int(status), int(id)))


        self.cnx.commit()
        cursor.close()

    #
    def getUndownloadedWebpages(self, limit):
        cursor = self.cnx.cursor()
        query = (
            "SELECT id, unique_id, status, url, title, image, publisher, tries, published, raw_categories "
            "FROM `webpage` "
            "WHERE status = %s AND tries < %s "
            "ORDER BY created ASC "
            "LIMIT 0, %s"
        )

        cursor.execute(query, (Webpage.STT_CREATED, 4, int(limit)))
        webpages = []
        columns = tuple( [d[0].decode('utf8') for d in cursor.description] )

        for row in cursor:
            webpage = Webpage(dict(zip(columns, row)))
            webpages.append(webpage)

        cursor.close()

        return webpages


    def addArticle(self, article):
        cursor = self.cnx.cursor()

        insertQuery = (
            "INSERT IGNORE INTO `article` (`unique_id`, `publisher`, `title`, `url`, `content`, `content_html`, `image`, `raw_categories`, `created`, `published`) "
            "VALUES (%(uniqueId)s, %(publisher)s, %(title)s, %(url)s, %(content)s, %(contentHtml)s, %(image)s, %(rawCategories)s, now(), %(published)s)")

        insertData = {
            'uniqueId': article.uniqueId,
            'publisher': article.publisher,
            'title': article.title,
            'url': article.url,
            'content': article.content,
            'contentHtml': article.contentHtml,
            'image': article.image,
            'rawCategories': article.rawCategories,
            'published': article.published
        }

        cursor.execute(insertQuery, insertData)
        self.cnx.commit()
        cursor.close()