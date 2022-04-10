import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from sklearn.tree import export_graphviz
from six import StringIO  
from IPython.display import Image  
import pydotplus
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler

# reading the csv file
dataset = pd.read_csv('AdmissionPredictionDataSet.csv')
pd.cut(dataset['Chance of Admit '], bins = [0, 2, 3, 4], labels = ['bad','satisfactory','great']) # ALERT: Need to implement for Decision tree.

# Splitting the dataset into features and predicted values
x = dataset[['CGPA']]  # feature matrix of CGPA
y = dataset['Chance of Admit ']  # vector of dependent variable (Chance of Admit)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1) # 70% training and 30% test

# Preprocess x and y.
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

pre = preprocessing.LabelEncoder()
y_train = pre.fit_transform(y_train)
y_test = pre.fit_transform(y_test)

# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Test Decision Tree Classifer
clf = clf.fit(x_test,y_test) # 

# Predict the response for test dataset
y_pred = clf.predict(x_test)

# Model Accuracy, how often is the classifier correct?
# print("Accuracy:",metrics.accuracy_score(y_test, y_pred)) --> Not needed for project.

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data, filled=True, rounded=True, special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('admisison_classification.png')
Image(graph.create_png())