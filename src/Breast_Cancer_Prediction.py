from __future__ import print_function
import sys
from pyspark.ml import PipelineModel
from pyspark.ml.feature import StringIndexer, VectorIndexer
from pyspark.sql import SparkSession

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: Breast_Cancer_Prediction <data>", file=sys.stderr)
        exit(-1)

    spark = SparkSession\
        .builder\
        .appName("DecisionTreeClassificationExample")\
        .getOrCreate()

    # Load the data stored in LIBSVM format as a DataFrame.
    data = spark.read.format("libsvm").load(sys.argv[1])
    # data.printSchema()
    # print(data.schema)
    # data = spark.read.csv("hdfs://localhost:9000/user/hadoop/input/csv.txt", sep=' ', header=True)

    # Load the DecisionTree model.
    model = PipelineModel.load("hdfs://localhost:9000/user/hadoop/models/breastcancerDT")   #breast cancer model

    # Make predictions.
    predictions = model.transform(data)

    # Select example rows to display.
    predictions.select("prediction", "features").show(1)

    spark.stop()