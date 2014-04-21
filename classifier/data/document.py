__author__ = 'dungdt'

import math
from classifier import util
from collections import defaultdict

class Document:
    id = None
    terms = None
    features = None
    label = None

    # Construction
    def __init__(self, text, label = None, docId = None):
        self.features = defaultdict(list)
        self.terms = util.tokenize(text)
        self.label = label
        self.id = docId

        for term, termFrequency in self.terms.items():
            self.features[term] = 1 + math.log10(termFrequency)

    # Set label
    def setLabel(self, label):
        self.label = label

