__author__ = 'dungdt'

import mysql.connector

class DbConnector:
    cnx = None

    # constructor
    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', password='dungdt88', database='pnp')

    # destructor
    def __del__(self):
        self.cnx.close()

