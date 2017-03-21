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