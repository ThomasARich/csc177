# Linear Regression Using Admission Prediction Data Set
import pandas as pd
import numpy as np
from statistics import mean, stdev
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# reading the csv file
dataset = pd.read_csv('AdmissionPredictionDataSet.csv')

# splitting the dataset into features and predicted values
X = dataset[['CGPA']]  # feature matrix of CGPA
Y = dataset['Chance of Admit ']  # vector of dependent variable (Chance of Admit)

# splitting the dataset into training set and test set
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, shuffle=True)
x_train_graph = x_train
x_test_graph = x_test

print("x_train: \n", x_train)  # Training group - 70%
print("\nx_test: \n", x_test)  # Test group - 30%
print("\ny_train: \n", y_train)  # Target for training group
print("\ny_test: \n", y_test)  # Target for test group

mean_Y = mean(y_train)
sdev_Y = stdev(y_test)

print('\n\nMean - Chance of Admit: ' + str(mean_Y))
print('Standard Dev. - Chance of Admit: ' + str(sdev_Y))

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

pre = preprocessing.LabelEncoder()
y_train = pre.fit_transform(y_train)
y_test = pre.fit_transform(y_test)

# training the machine learning model
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(x_train, y_train)

# predicting the Chance of Admission values using the test set
predicted_chance = regressor.predict(x_test)

# Model evaluation
print("Root mean squared error = %.4f" % np.sqrt(mean_squared_error(y_test, predicted_chance)))
print('R-squared = %.4f' % r2_score(y_test, predicted_chance))

# Display model parameters
print('Slope = ', regressor.coef_)
print('Intercept = ', regressor.intercept_)

# displaying the values of CGPA in the training feature matrix (x_train) and the training Chance of admission values with a scatter plot
plt.scatter(x_train_graph.values, y_train, color='green')

# displaying the regression line of predicted Chance of admission values generated by our model.
plt.plot(x_train_graph.values, regressor.predict(x_train), color='blue')

plt.title('CGPA vs Chance of admit - Training Values')
plt.xlabel('CGPA')
plt.ylabel('Chance of admit')
plt.show()

# displaying the values of CGPA in the test feature matrix (x_test) and the real chance of admission values with a scatter plot
plt.scatter(x_test_graph.values, y_test, color='green')

# displaying the regression line of predicted chance of admission values generated by our model.
plt.plot(x_test_graph.values, predicted_chance, color='blue')

plt.title('CGPA vs Chance of admit - Test Values')
plt.xlabel('CGPA')
plt.ylabel('Chance of admit')
plt.show()
