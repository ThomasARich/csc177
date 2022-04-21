import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
import graphviz 
from sklearn.tree import export_graphviz
from six import StringIO  
from IPython.display import Image  
import pydotplus
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC 

dataset = pd.read_csv('Churn_Modelling.csv')

# Drop columns not selected as features.
dataset.drop(dataset.iloc[:, 0:3], inplace = True, axis = 1) # Drops RowNumber, CustomerId, and Surname.
dataset.drop(dataset.iloc[:, 1:4], inplace = True, axis = 1) # Drops Geography, Gender, and Age.

x = dataset[['CreditScore', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'IsActiveMember', 'EstimatedSalary']]  # Independent Variables
y = dataset['Exited']  # Dependent Variable

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, shuffle=True) # 70% training and 30% test

# Decision Tree Classifier
clf = tree.DecisionTreeClassifier(criterion='entropy',max_depth=3)
clf = clf.fit(x_test, y_test)
dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data)
dot_data = StringIO()
export_graphviz(clf, out_file=dot_data, filled=True, rounded=True, special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('churn_decisiontree.png')
Image(graph.create_png())

# Naive Bayes Classifier
clf_NB = GaussianNB()
clf_NB.fit(x,y)
NB_pred = clf_NB.predict(x_test)

print('Accuracy on test data is %.2f' % (accuracy_score(y_test, NB_pred)))

# SVM Classifier - TBD

# KNN Classifier - TBD