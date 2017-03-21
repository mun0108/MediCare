from unittest import TestCase
from src.DataOperations import DataOperations
class DataOperationsTest(TestCase):
    def setUp(self):
        self.dataoperations=DataOperations()

    def test_diabetes(self):
        self.dataoperations.diabetes_svm_preprocessing()
