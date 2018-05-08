from unittest import TestCase
from src.Classifiers_cluster import Classifiers_cluster


class Classifier_cluster_testMLP(TestCase):
    def setUp(self):
        self.classifier_cluster = Classifiers_cluster()

    def test_breast_cancer(self):
        data = "../data/breast_cancer_svm.txt"
        self.classifier_cluster.MultiLayerPerceptron(data, "10")

    def test_invalid_input(self):
        data = "/dsa"
        self.classifier_cluster.MultiLayerPerceptron(data, "2")

    def test_diabetes(self):
        data = "../data/masBPSVM.txt"
        self.classifier_cluster.MultiLayerPerceptron(data, "10")
