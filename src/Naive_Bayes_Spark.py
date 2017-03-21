from __future__ import print_function
import sys

# $example on$
from pyspark.ml.classification import NaiveBayes
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.feature import StringIndexer
from src.Operations import Operations

# $example off$
from pyspark.sql import SparkSession

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: Naive Bayes_Spark <file>", file=sys.stderr)
        exit(-1)

    spark = SparkSession\
        .builder\
        .appName("NaiveBayesExample")\
        .getOrCreate()

    # $example on$
    # Load training data
    data = spark.read.format("libsvm") \
        .load(sys.argv[1])

    indexer = StringIndexer(inputCol="label", outputCol="indexedLabel")
    indexed_df = indexer.fit(data).transform(data)
    operations=Operations()

    operations.stringIndexerMapping(indexed_df,"label","indexedlabel")

    # Split the data into train and test
    splits = indexed_df.randomSplit([0.6, 0.4], 1234)
    train = splits[0]
    test = splits[1]

    # create the trainer and set its parameters
    nb = NaiveBayes(smoothing=1.0, modelType="multinomial")

    # train the model
    model = nb.fit(train)

    # select example rows to display.
    predictions = model.transform(test)
    predictions.show()

    # compute accuracy on the test set
    evaluator = MulticlassClassificationEvaluator(labelCol="indexedLabel", predictionCol="prediction",
                                                  metricName="accuracy")
    accuracy = evaluator.evaluate(predictions)
    print("Test set accuracy = " + str(accuracy))
    # $example off$

    spark.stop()