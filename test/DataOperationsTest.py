from unittest import TestCase
from src.DataOperations import DataOperations
import os
class DataOperationsTest(TestCase):
    def setUp(self):
        self.dataoperations=DataOperations()

    def tearDown(self):
        if os.path.exists('../data/diabetes_svm_new.txt'):
            os.remove('../data/diabetes_svm_new.txt')
        if os.path.exists('../data/diabetes_svm.txtnew.txt'):
            os.remove('../data/diabetes_svm.txtnew.txt')

    def test_diabetes(self):
        self.dataoperations.diabetes_svm_preprocessing()

    def test_feature_selection_new_svm_file(self):
        self.dataoperations.svm_file_feature_select([0,1,2,3],"../data/diabetes_svm.txt")
        self.dataoperations.svm_file_feature_select([0,1,2,3,4,5],"../data/diabetes_svm.txt","../data/diabetes_svm_new.txt")
