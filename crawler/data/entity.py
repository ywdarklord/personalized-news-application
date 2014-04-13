__author__ = 'dungdt'

class Entity:
    def set(self, key, value):
        setattr(self, key, value.encode('utf-8'))