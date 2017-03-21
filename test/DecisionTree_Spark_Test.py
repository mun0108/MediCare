from unittest import TestCase
import subprocess

class DecisionTree_Test(TestCase):
    def test_func(self):
        print "hello"

    def runProcess(self,command):
        subprocess.call(command, shell=True)

    def test_run_breast_cancer(self):
        data="../data/breast_cancer_svm.txt"
        master="spark://golum:7077 "
        spark_application="../src/Spark_Decision_Tree.py "
        command="$SPARK_HOME/bin/spark-submit --master "+master+spark_application+data
        self.runProcess(command)

    def test_run_diabetes(self):
        data = "../data/diabetes_svm.txt"
        master = "spark://golum:7077 "
        spark_application = "../src/Spark_Decision_Tree.py "
        command = "$SPARK_HOME/bin/spark-submit --master " + master + spark_application + data
        self.runProcess(command)