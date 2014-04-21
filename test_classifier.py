__author__ = 'dungdt'

import time
from classifier.classifier import Classifier
from classifier.data.dictionary import Dictionary
from classifier.data_reader import DataReader

if __name__ == '__main__':
    dictionary = Dictionary()
    dataReader = DataReader(dictionary)
    classifier = Classifier(dataReader, trainingDataPath='data/training',
                            testDataPath='data/test')

    print 'Training...'
    t = time.time()
    classifier.train()
    print 'Training time: %d' %(time.time() - t)

    t = time.time()
    print 'Testing...'
    print 'Accuracy: %s%%' % ('{:4.2f}'.format(classifier.test() * 100))
    print 'Testing time: %d' %(time.time() - t)

    testData = classifier.dataReader.readTestData(classifier.testDataPath)
    print classifier.classify(testData[0][0])
