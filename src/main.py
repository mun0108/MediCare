import os
import subprocess

from src.Classifier_Prediction import  Classifiers_Prediction
if __name__ == "__main__":
    print "hello"
    classifier_prediction=Classifiers_Prediction()

    """
   1. Sample code number            id number
   2. Clump Thickness               1 - 10
   3. Uniformity of Cell Size       1 - 10
   4. Uniformity of Cell Shape      1 - 10
   5. Marginal Adhesion             1 - 10
   6. Single Epithelial Cell Size   1 - 10
   7. Bare Nuclei                   1 - 10
   8. Bland Chromatin               1 - 10
   9. Normal Nucleoli               1 - 10
  10. Mitoses                       1 - 10

    """
    list=[]
    n_features=10
    list.append("0")
    for i in range(1,n_features+1):
        print ("\n\n1. Sample code number            id number\n\
               2. Clump Thickness               1 - 10\n\
               3. Uniformity of Cell Size       1 - 10\n\
               4. Uniformity of Cell Shape      1 - 10\n\
               5. Marginal Adhesion             1 - 10\n\
               6. Single Epithelial Cell Size   1 - 10\n\
               7. Bare 1234"
               "Nuclei                   1 - 10\n\
               8. Bland Chromatin               1 - 10\n\
               9. Normal Nucleoli               1 - 10\n\
              10. Mitoses                       1 - 10\n")
        print("Enter Feature number "+str(i))
        f=""
        f=input()
        feat=str(i)+":"+str(f)
        list.append(feat)

    file_name="do_predictions.txt"
    new_feature_file_to_be_predicted = open(file_name, 'w')
    new_feature_file_to_be_predicted.write(' '.join(list))
    new_feature_file_to_be_predicted.close()
    subprocess.call("hadoop fs -copyFromLocal "+file_name+" hdfs://localhost:9000/user/hadoop/input/", shell=True)
    classifier_prediction.Breast_Cancer_Prediction("hdfs://localhost:9000/user/hadoop/input/"+file_name,True)
  #
    os.remove(file_name)
  #   classifier_prediction.Breast_Cancer_Pred_stream()