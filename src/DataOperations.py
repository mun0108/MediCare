###perform operations on data
import pandas as pd
import numpy as np

class DataOperations():
    def read_file(self,location,file_type="csv"):
        if(file_type=="csv"):
            data=pd.read_csv(location)
            return data

    def breast_cancer_preprocessing(self,location,type="csv"):
        data=self.read_file(location,type)
        data.replace('?', -99999, inplace=True)
        data.drop(['id'], 1, inplace=True)
        return data

    def diabetes_svm_preprocessing(self):
        original_file = open("../data/diabetes_svm.txt", 'r')
        content=original_file.readlines()
        new_feature_file=open("../data/diabetes_svm.txt"+"new.txt", 'w')
        for line in content:
            features=line.split()
            relevant_features=list(features[i] for i in [0, 1, 5, 6, 8])
            new_feature_file.write(' '.join(relevant_features))
            new_feature_file.write('\n')
        original_file.close()
        new_feature_file.close()

    def svm_file_feature_select(self,feature_index,file,new_file="new.txt"):
        original_file = open(file, 'r')
        content = original_file.readlines()
        if(new_file=="new.txt"):
            new_file_name = file + "new.txt"
        else:
            new_file_name=new_file

        new_feature_file = open(new_file_name, 'w')
        for line in content:
            features = line.split()
            relevant_features = list(features[i] for i in feature_index)
            new_feature_file.write(' '.join(relevant_features))
            new_feature_file.write('\n')
        original_file.close()
        new_feature_file.close()

