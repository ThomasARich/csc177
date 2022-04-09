import pandas as pd
from sklearn.tree import DecisionTreeClassifier                             # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split                        # Import train_test_split function
from sklearn import metrics                                                 # Import scikit-learn metrics module for accuracy calculation
from sklearn.tree import export_graphviz
from six import StringIO  
from IPython.display import Image  
import pydotplus
from sklearn import preprocessing
from sklearn import utils
from sklearn.preprocessing import StandardScaler

col_names = ['Serial No.', 'GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR', 'CGPA', 'Research', 'Chance_of_Admit'] 
admit_in = pd.read_csv('AdmissionPredictionDataSet.csv', header=None, names=col_names, skiprows=1)


feature_cols = ['GRE Score', 'TOEFL Score', 'CGPA']
X = admit_in[feature_cols]
Y = admit_in.Chance_of_Admit

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, shuffle=True)

pre = preprocessing.LabelEncoder()
y_train = pre.fit_transform(y_train)
y_test = pre.fit_transform(y_test)

# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(x_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(x_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names = feature_cols,class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('chanceofadmit.png')
Image(graph.create_png())