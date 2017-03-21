from src.Classifiers import Classifier
from unittest import TestCase
class ClassifierTest(TestCase):
    def setUp(self):
        self.classifier=Classifier()

    def tearDown(self):
        print "Exiting"

    def test_func1(self):
        self.assertEqual(self.classifier.func(2,3),5)

