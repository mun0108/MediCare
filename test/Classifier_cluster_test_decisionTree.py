from unittest import TestCase
from src.Classifiers_cluster import Classifiers_cluster
class Classifier_cluster_test(TestCase):
    def setUp(self):
        self.classifier_cluster=Classifiers_cluster()

    def test_breast_cancer(self):
        data = "../data/breast_cancer_svm.txt"
        self.classifier_cluster.Decision_Tree(data)

    def test_invalid_input(self):
        data="/dsa"
        self.classifier_cluster.Decision_Tree(data)

    def test_diabetes(self):
        data="../data/new_diabetes_svm.txt"
        self.classifier_cluster.Decision_Tree(data)