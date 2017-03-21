from src.Classifiers import Classifier
from unittest import TestCase
from src.DataOperations import DataOperations
import numpy as np
from sklearn import cross_validation,neighbors
from src.AccuracyCalculation import AccuracyCalculation

class ClassifierTest(TestCase):
    def setUp(self):
        self.classifier=Classifier()
        self.dataoperations=DataOperations()
        self.accuracycalculation=AccuracyCalculation()

    def tearDown(self):
        print "Exiting"

    def test_func1(self):
        print "hello"
        self.assertEqual(self.classifier.func(2, 3), 5)

    def test_knntest(self):
        data=self.dataoperations.breast_cancer_preprocessing("../data/breast_cancer_csv.csv","csv")
        X = np.array(data.drop(['class'], 1))
        y = np.array(data['class'])
        X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.1)
        knn=self.classifier.KnnModel(X_train,y_train)
        y_pred=self.classifier.KnnPredict(knn,X_test)
        print self.accuracycalculation.accuracy(y_test,y_pred)

    def test_best_k_knn(self):
        data = self.dataoperations.breast_cancer_preprocessing("../data/breast_cancer_csv.csv", "csv")
        X = np.array(data.drop(['class'], 1))
        y = np.array(data['class'])
        X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.1)
        best_k,best_accuracy=self.classifier.find_best_k_for_knn(1,25,X_train,y_train,X_test,y_test)
        print best_k,best_accuracy



