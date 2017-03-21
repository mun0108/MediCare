from sklearn.metrics import accuracy_score


class AccuracyCalculation():
    def accuracy(self,y_actual,y_pred):
        return accuracy_score(y_actual,y_pred)

