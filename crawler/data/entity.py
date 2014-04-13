__author__ = 'dungdt'

class Entity:
    def set(self, key, value):
        if isinstance(value, str):
            value = value.encode('utf-8')

        setattr(self, key, value)