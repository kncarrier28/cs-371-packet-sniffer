import pandas as pd
import numpy as np
import csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.datasets import make_classification

# read CSV including header
df = pd.read_csv("data/trainingSet.csv", header=0)
pf = pd.read_csv("data/flows.csv", header=0)
# You might not need this next line if you do not care about losing information about flow_id etc. All you actually need to
# feed your machine learning model are features and output label.
# columns_list = ['proto', 'feature_1', 'feature_2', 'feature_3', 'feature_4', 'label']
# df.columns = columns_list -- read headers from file
# features = ['proto', 'feature_1', 'feature_2', 'feature_3', 'feature_4']

X = df[df.columns[:-1]] # use all columns except last one (type)
y = df['type']

predict = pf[pf.columns]

resultsDT = []
resultsNN = []
resultsSVC = []

acc_scores = 0
for i in range(0, 10):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

    #Decision Trees
    clfDT = tree.DecisionTreeClassifier()
    clfDT.fit(X_train, y_train)
    resultsDT.append(clfDT.score(X_test, y_test))
    print("DT Prediction: ", clfDT.predict(predict))

    # Neural network (MultiPerceptron Classifier)
    clfNN = MLPClassifier()
    clfNN.fit(X_train, y_train)
    resultsNN.append(clfNN.score(X_test, y_test))
    print("NN Prediction: ", clfDT.predict(predict))

    #SVM's
    clfSVC = SVC(gamma='auto')     #SVC USE THIS
    clfSVC = LinearSVC(max_iter = 10000)  #Linear SVC
    clfSVC.fit(X_train, y_train)
    print("SVC Prediction: ", clfDT.predict(predict))

    #here you are supposed to calculate the evaluation measures indicated in the project proposal (accuracy, F-score etc)
    resultsSVC.append(clfSVC.score(X_test, y_test))  #accuracy score -- score has to be output in graph form

print(resultsDT)
print(resultsNN)
print(resultsSVC)

ind = np.arange(len(resultsNN))
width = 0.25

p1 = plt.bar(ind, resultsDT, width)
p2 =  plt.bar(ind, resultsNN, width)
p3 =  plt.bar(ind, resultsSVC, width, bottom = resultsSVC)

plt.title('Evaluation')
plt.xlabel('Executions')
plt.ylabel('Accuracy')
plt.xticks(np.arange(0, 11, 2))
plt.yticks(np.arange(0, 11, 2))
plt.legend(('Decision Trees', 'Neural network', 'SVC'))
plt.show()
