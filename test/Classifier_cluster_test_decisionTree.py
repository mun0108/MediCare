from unittest import TestCase
from src.Classifiers_cluster import Classifiers_cluster
class Classifier_cluster_testDT(TestCase):
    def setUp(self):
        self.classifier_cluster=Classifiers_cluster()

    def test_breast_cancer(self):
        data = "../data/breast_cancer_svm.txtnew.txt"
        self.classifier_cluster.Decision_Tree(data,"DT_Breast_Cancer_N")

    def test_invalid_input(self):
        data="/dsa"
        self.classifier_cluster.Decision_Tree(data,"DT_Dsa")

    def test_diabetes(self):
        data="../data/diabetes_svm.txt"
        self.classifier_cluster.Decision_Tree(data,"DT_Diabetes")

    def test_diabetes1(self):
        data="../data/diabetes_svm.txtnew.txt"
        self.classifier_cluster.Decision_Tree(data,"DT_Diabetes_New")

    def test_CKD(self):
        data="../data/CKD_SVM.txt"
        self.classifier_cluster.Decision_Tree(data,"DT_CKD")

    def test_fembpsvm(self):
        data="../data/femBPSVM.txt"
        self.classifier_cluster.Decision_Tree(data,"DT_femBP")

    def test_heartsvm(self):
        data="../data/heart_SVM.txt"
        self.classifier_cluster.Decision_Tree(data,"DT_heart")