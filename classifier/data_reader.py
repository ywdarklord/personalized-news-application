__author__ = 'dungdt'

import glob, os, math
from collections import Counter
import util
from data import document

class DataReader:
    dictionary = None

    def __init__(self, dictionary):
        self.dictionary = dictionary

    #
    def readTrainingData(self, dataPath):
        files = glob.glob(dataPath.rstrip('/') + '/*/*')
        docs = []
        trainingData = []

        for file in files:
            if os.path.isfile(file):
                label = util.extractLabel(file)

                if label:
                    doc = document.Document(text=open(file, 'r').read(), label=label)
                    self.dictionary.addDocument(doc)
                    docs.append(doc)

        # with open(dataPath) as infile:
        #     for line in infile:
        #         tmp = line.split("\t")
        #         if len(tmp) == 2:
        #             doc = document.Document(text=tmp[1].strip(), label=tmp[0].strip())
        #             self.dictionary.addDocument(doc)
        #             docs.append(doc)

        self.dictionary.computeIdf()

        for doc in docs:
            features = self.dictionary.getFeatures(doc)
            trainingData.append((features, doc.label))

        return trainingData

    def readTestData(self, dataPath):
        files = glob.glob(dataPath.rstrip('/') + '/*/*')
        testData = []

        # with open(dataPath) as infile:
        #     for line in infile:
        #         tmp = line.split("\t")
        #         if len(tmp) == 2:
        #             doc = document.Document(text=tmp[1].strip(), label=tmp[0].strip())
        #             features = self.dictionary.getFeatures(doc)
        #             testData.append((features, doc.label))

        for file in files:
            if os.path.isfile(file):
                label = util.extractLabel(file)

                if label:
                    doc = document.Document(text=open(file, 'r').read(), label=label)
                    features = self.dictionary.getFeatures(doc)
                    testData.append((features, doc.label))

        return testData

    # Feature vector: {t1: tf-idf1, t2: tf-idf2, ...}
    def extract(self, document):
        return []

