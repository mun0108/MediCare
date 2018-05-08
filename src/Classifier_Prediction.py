import os
from src.Operations import Operations
from HadoopOperations import HadoopOperations

class Classifiers_Prediction():
    def __init__(self):
        self.operations=Operations()
        self.master="spark://golum:7077 "
        # hadoopOperation = HadoopOperations()

    def Breast_Cancer_Prediction(self,input_file,hdfs=False):
        if hdfs==False & os.path.exists(input_file) == False:
            print "Invalid input file"
            return False
        spark_application = "../src/Breast_Cancer_Prediction.py "
        command = "$SPARK_HOME/bin/spark-submit --master " + self.master + spark_application + input_file
        self.operations.runProcess(command+" >out.txt")

    def Breast_Cancer_Pred_stream(self):
        spark_application = "../src/Breast_Cancer_Prediction_Streaming.py "
        command = "$SPARK_HOME/bin/spark-submit --master " + self.master + spark_application
        self.operations.runProcess(command)
