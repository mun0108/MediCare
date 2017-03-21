import os
from src.Operations import Operations

class Classifiers_cluster():
    def __init__(self):
        self.operations=Operations()
        self.master="spark://golum:7077 "


    def Decision_Tree(self,input_file):
        if os.path.exists(input_file) == False:
            print "Invalid input file"
            return False
        spark_application = "../src/Spark_Decision_Tree.py "
        command = "$SPARK_HOME/bin/spark-submit --master " + self.master + spark_application + input_file
        self.operations.runProcess(command)

    def Naive_Bayes(self,input_file):
        if os.path.exists(input_file) == False:
            print "Invalid input file"
            return False
        spark_application = "../src/Spark_Naive_Bayes.py "
        command = "$SPARK_HOME/bin/spark-submit --master " + self.master + spark_application + input_file
        self.operations.runProcess(command)

    def Gradient_Boosted_Tree(self,input_file):
        if os.path.exists(input_file) == False:
            print "Invalid input file"
            return False
        spark_application = "../src/Spark_Gradient_Boosted_Tree.py "
        command = "$SPARK_HOME/bin/spark-submit --master " + self.master + spark_application + input_file
        self.operations.runProcess(command)