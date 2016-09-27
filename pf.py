
# Model training and testing

from __future__ import print_function

import sys

from pyspark import SparkContext
from pyspark.mllib.tree import RandomForest, RandomForestModel
from pyspark.mllib.util import MLUtils

def predict(sc, data):

    #sc = SparkContext(appName="PythonRandomForestClassificationExample")
    # $example on$
    # Load and parse the data file into an RDD of LabeledPoint.
    #data = MLUtils.loadLibSVMFile(sc, 'deathproject/test1.txt')
    #data = [1, 0, 5, 1, 1, 65, 1, 2, 0, 1, 0, 6, 3450]
    # Split the data into training and test sets (30% held out for testing)
    # (trainingData, testData) = data.randomSplit([0.7, 0.3])

    # Train a RandomForest model.
    #  Empty categoricalFeaturesInfo indicates all features are continuous.
    #  Note: Use larger numTrees in practice.
    #  Setting featureSubsetStrategy="auto" lets the algorithm choose.
    print('Starting...')

    #model = RandomForest.trainClassifier(trainingData, numClasses=8, categoricalFeaturesInfo={},
    #                                     numTrees=5, featureSubsetStrategy="auto",
    #                                     impurity='gini', maxDepth=4, maxBins=32)



    sameModel = RandomForestModel.load(sc, "target/tmp/myRandomForestClassificationModel2")

    print('Predicting...')
    # Evaluate model on test instances and compute test error
   
    #predictions = sameModel.predict(data.map(lambda x: x.features))
    predictions = sameModel.predict(data)

    #labelsAndPredictions = data.map(lambda lp: lp.label).zip(predictions)
    #testErr = labelsAndPredictions.filter(lambda (v, p): v != p).count() / float(testData.count())
    #print('Test Error = ' + str(testErr))
    #print('Learned classification forest model:')
    #print(sameModel.toDebugString())
    print(predictions)
    return int(predictions)
    #print(labelsAndPredictions)
    # Save and load model
    # model.save(sc, "target/tmp/myRandomForestClassificationModel")
    # sameModel = RandomForestModel.load(sc, "target/tmp/myRandomForestClassificationModel")
    # $example off$
