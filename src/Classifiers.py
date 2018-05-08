from sklearn.neighbors import  KNeighborsClassifier
from src.AccuracyCalculation import AccuracyCalculation
class Classifier():
    def __init__(self):
        self.accuracycalculation=AccuracyCalculation()

    def func(self,a,b):
        return a+b

    def KnnModel(self, x_train, y_train, k=5):
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(x_train, y_train)
        return knn

    def KnnPredict(self,knn_model,data):
        data_pred=knn_model.predict(data)
        return data_pred

    def find_best_k_for_knn(self,min_k,max_k,x_train,y_train,x_test,y_test):
        k_range = range(min_k, max_k)
        cur_score=-1
        best_k_list=[]
        max_score=-1
        for k in k_range:
            knn = self.KnnModel(x_train,y_train,k)
            y_pred = self.KnnPredict(knn,x_test)
            cur_score=self.accuracycalculation.accuracy(y_test, y_pred)
            if cur_score>max_score:
                max_score=cur_score
                best_k_list=[]
                best_k_list.append(k)

            elif cur_score==max_score:
                best_k_list.append(k)

        return best_k_list,max_score
