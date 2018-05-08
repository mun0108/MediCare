from __future__ import print_function
import sys
from pyspark.ml import PipelineModel
from pyspark.ml.feature import StringIndexer, VectorIndexer
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import *
from pyspark.ml.linalg import VectorUDT

if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("DecisionTreeClassificationExample")\
        .getOrCreate()
    spark.conf.set("spark.sql.streaming.checkpointLocation", \
                          "hdfs://localhost:9000/user/hadoop/input/");

    Schema=StructType((StructField("label",DoubleType(),True),\
                       StructField("features",VectorUDT(),True)))
    # Load the data stored in LIBSVM format as a DataFrame.
    data = spark.readStream.format("libsvm").schema(Schema)\
        .load("hdfs://localhost:9000/user/hadoop/input/")

    # Load the DecisionTree model.
    model = PipelineModel.load("hdfs://localhost:9000/user/hadoop/models/breastcancerDT")   #breast cancer model

    # Make predictions.
    predictions = model.transform(data)

    pred=predictions.select("prediction", "features")

    query = pred \
        .writeStream \
        .start("hdfs://localhost:9000/user/hadoop/output/")

    query.awaitTermination()