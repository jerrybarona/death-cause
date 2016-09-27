
# Model training and testing

from __future__ import print_function

import sys

from pyspark import SparkContext
# $example on$
from pyspark.mllib.tree import RandomForest, RandomForestModel
from pyspark.mllib.util import MLUtils
# $example off$

if __name__ == "__main__":
    sc = SparkContext(appName="PythonRandomForestClassificationExample")
    # $example on$
    # Load and parse the data file into an RDD of LabeledPoint.
    data = MLUtils.loadLibSVMFile(sc, 'deathproject/datanew2.txt')
    # Split the data into training and test sets (30% held out for testing)
    (trainingData, testData) = data.randomSplit([0.7, 0.3])

    # Train a RandomForest model.
    #  Empty categoricalFeaturesInfo indicates all features are continuous.
    #  Note: Use larger numTrees in practice.
    #  Setting featureSubsetStrategy="auto" lets the algorithm choose.
    print('Starting...')
    model = RandomForest.trainClassifier(trainingData, numClasses=8, categoricalFeaturesInfo={0: 4, 1: 19, 2: 9, 3: 2, 4: 6, 6: 8, 7: 4, 8: 3, 9: 16, 10: 8, 11: 11},
                                         numTrees=8, featureSubsetStrategy="auto",
                                         impurity='gini', maxDepth=4, maxBins=32)
    #model = RandomForest.trainClassifier(trainingData, numClasses=8, categoricalFeaturesInfo={1: 4, 1},
                                         #numTrees=10, featureSubsetStrategy="auto",
                                         #impurity='gini', maxDepth=4, maxBins=32)


    print('Predicting...')
    # Evaluate model on test instances and compute test error
    predictions = model.predict(testData.map(lambda x: x.features))
    labelsAndPredictions = testData.map(lambda lp: lp.label).zip(predictions)
    testErr = labelsAndPredictions.filter(lambda(v, p): v != p).count() / float(testData.count())
    print('Test Error = ' + str(testErr))
    print('Learned classification forest model:')
    #print(model.toDebugString())

    # Save and load model
    model.save(sc, "target/tmp/myRandomForestClassificationModel2")
    #sameModel = RandomForestModel.load(sc, "target/tmp/myRandomForestClassificationModel")
    # $example off$
