from unittest import TestCase
from src.Classifiers_cluster import Classifiers_cluster
from src.DataOperations import DataOperations
class Classifier_cluster_test(TestCase):
    def setUp(self):
        self.classifier_cluster=Classifiers_cluster()
        self.dataoperations=DataOperations()

    def test_breast_cancer(self):
        data = "../data/breast_cancer_svm.txt"
        self.classifier_cluster.Naive_Bayes(data)

    def test_invalid_input(self):
        data="/dsa"
        self.classifier_cluster.Naive_Bayes(data)

    def test_diabetes(self):
        # self.dataoperations.svm_file_feature_select([0,1,5,6,8],"../data/diabetes_svm.txt")
        data="../data/diabetes_svm.txt"
        self.classifier_cluster.Naive_Bayes(data)