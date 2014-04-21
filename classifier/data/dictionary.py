__author__ = 'dungdt'

from collections import Counter, defaultdict
import math

class Dictionary:
    terms = None
    totalDocuments = None
    idf = None

    # Constructor
    def __init__(self):
        self.terms = Counter()
        self.totalDocuments = 0
        self.idf = {}

    # Add a new document
    def addDocument(self, doc):
        self.totalDocuments += 1

        # add terms to dictionary
        for term in doc.terms:
            self.terms[term] += 1

    # Compute the inverse document frequency
    def computeIdf(self):
        N = float(self.totalDocuments)
        for term, documentFrequency in self.terms.items():
            self.idf[term] = math.log10(N / documentFrequency)

    #
    def getIdf(self, term):
        if term in self.idf:
            return self.idf[term]

        return math.log10(float(self.totalDocuments))

    def getFeatures(self, doc):
        features = defaultdict(list)
        for term, feature in doc.features.iteritems():
            if term in self.idf:
                features[term] = feature * self.idf[term]
            else:
                features[term] = feature * math.log10(self.totalDocuments)

        return features