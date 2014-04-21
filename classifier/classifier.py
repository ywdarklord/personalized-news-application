__author__ = 'dungdt'

import os
import nltk
import nltk.classify

class Classifier:
    dataReader = None
    trainingDataPath = None
    testDataPath = None
    classifier = None

    def __init__(self, dataReader, trainingDataPath, testDataPath = ''):
        self.dataReader = dataReader
        self.trainingDataPath = trainingDataPath
        self.testDataPath = testDataPath

    # Train
    def train(self):
        trainingData = self.dataReader.readTrainingData(self.trainingDataPath)

        self.classifier = nltk.NaiveBayesClassifier.train(trainingData)

    def test(self):
        if os.path.isdir(self.testDataPath):
            testData = self.dataReader.readTestData(self.testDataPath)

            return nltk.classify.accuracy(self.classifier, testData)

        return 0.0

    def classify(self, features):
        return self.classifier.classify(features)