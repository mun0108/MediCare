from __future__ import print_function
import sys
# $example on$
from pyspark.ml.classification import MultilayerPerceptronClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.feature import StringIndexer
# $example off$
from pyspark.sql import SparkSession

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: Spark_Multilayer_Perceptron <file> <features>", file=sys.stderr)
        exit(-1)

    spark = SparkSession\
        .builder.appName("multilayer_perceptron_classification_example").getOrCreate()

    # $example on$
    # Load training data
    data = spark.read.format("libsvm")\
        .load(sys.argv[1])

    indexer = StringIndexer(inputCol="label", outputCol="indexedLabel")
    indexed_df = indexer.fit(data).transform(data)

    # Split the data into train and test
    splits = indexed_df.randomSplit([0.6, 0.4], 1234)
    train = splits[0]
    test = splits[1]

    features_num=int(sys.argv[2])

    # specify layers for the neural network:
    # input layer of size 4 (features), two intermediate of size 5 and 4
    # and output of size 2 (classes)
    layers = [10,11,6,2]

    # create the trainer and set its parameters
    trainer = MultilayerPerceptronClassifier(labelCol="indexedLabel",maxIter=100, layers=layers, blockSize=128, seed=1234)

    # train the model
    model = trainer.fit(train)

    # compute accuracy on the test set
    result = model.transform(test)
    result.show(5)
    evaluator = MulticlassClassificationEvaluator(labelCol="indexedLabel", predictionCol="prediction",
                                                  metricName="accuracy")
    accuracy = evaluator.evaluate(result)
    print("Test set accuracy = " + str(accuracy))
    # $example off$

    spark.stop()