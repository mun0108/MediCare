import os
from src.Operations import Operations
from src.HadoopOperations import HadoopOperations

class Classifiers_cluster():
    def __init__(self):
        self.operations=Operations()
        self.master="spark://golum:7077 "
        self.hadoopoperations=HadoopOperations()


    def Decision_Tree(self,input_file,hdfs=False):
        if hdfs==False and os.path.exists(input_file) == False:
            print "Invalid input file"
            return False
        if hdfs==True and self.hadoopoperations.file_exist(input_file) == False:
            return False
        spark_application = "../src/Spark_Decision_Tree.py "
        command = "$SPARK_HOME/bin/spark-submit --master " + self.master + spark_application + input_file
        self.operations.runProcess(command)
        return True

    def Naive_Bayes(self,input_file,hdfs=False):
        if hdfs==False and os.path.exists(input_file) == False:
            print "Invalid input file"
            return False
        if hdfs==True and self.hadoopoperations.file_exist(input_file) == False:
            return False
        spark_application = "../src/Spark_Naive_Bayes.py "
        command = "$SPARK_HOME/bin/spark-submit --master " + self.master + spark_application + input_file
        self.operations.runProcess(command)
        return True

    def Gradient_Boosted_Tree(self,input_file,hdfs=False):
        if hdfs==False and os.path.exists(input_file) == False:
            print "Invalid input file"
            return False
        if hdfs==True and self.hadoopoperations.file_exist(input_file) == False:
            return False
        spark_application = "../src/Spark_Gradient_Boosted_Tree.py "
        command = "$SPARK_HOME/bin/spark-submit --master " + self.master + spark_application + input_file
        self.operations.runProcess(command)
        return True