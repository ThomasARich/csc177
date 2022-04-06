import pandas as pd
import numpy as np
from statistics import mean, stdev
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# reading the csv file
dataset = pd.read_csv('Height-WeightDataSet.csv')

# splitting the dataset into features and predicted values
X = dataset[['Height']]             # independent variable (single predictor)
Y = dataset['Weight']               # dependent variable 

# splitting the dataset into training set (70%) and test set (30%)
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, shuffle=True)
x_train_graph = x_train
x_test_graph = x_test

print("\nx_train: \n", x_train)     # Training group - 70%
print("\nx_test: \n", x_test)       # Test group - 30%
print("\ny_train: \n", y_train)     # Target for training group
print("\ny_test: \n", y_test)       # Target for test group

x_train_temp = x_train.squeeze()
x_test_temp = x_test.squeeze()

# # mean of training data
# mean_train_X = mean(x_train_temp)
# mean_train_Y = mean(y_train)

# # stdev of training data
# sdev_train_X = mean(x_train_temp)
# sdev_train_Y = mean(y_train)

# # mean of testing data
# mean_test_X = mean(y_test)
# mean_test_Y = mean(x_test_temp)

# # stdev of testing data
# sdev_test_Y = stdev(y_test)
# sdev_test_X = stdev(x_test_temp)

# print('\n\nMean of Training Data:')
# print('Weight: ' + str(mean_train_Y) + ' lbs')
# print('Height: ' + str(mean_train_X) + ' in.')

# print('\nStandard Dev. of Training Data:')
# print('Weight: ' + str(sdev_train_X))
# print('Height: ' + str(sdev_train_Y))

# print('\nMean of Test Data:')
# print('Weight: ' + str(mean_test_Y) + ' lbs')
# print('Height: ' + str(mean_test_X) + ' in.')

# print('\nStandard Dev. of Test Data:')
# print('Weight: ' + str(sdev_test_Y))
# print('Height: ' + str(sdev_test_X))

print('\n')

##################### ASSIGNMENT 2 ######################
# Linear Regression Using Weight-Height data set

# standardizing values
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# training the machine learning model
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(x_train, y_train)

# predicting the weight values using the test set
predicted_weight = regressor.predict(x_test)

# Model evaluation
print("Root mean squared error = %.4f" % np.sqrt(mean_squared_error(y_test, predicted_weight)))
print('R-squared = %.4f' % r2_score(y_test, predicted_weight))

# Display model parameters
print('Slope = ', regressor.coef_)
print('Intercept = ', regressor.intercept_)  ### Step 4: Postprocessing

# displaying the values of height in the training feature matrix (x_train) and the training weight values with a scatter plot
plt.scatter(x_train_graph.values, y_train, color='green')

# displaying the regression line of predicted weight values generated by our model.
plt.plot(x_train_graph.values, regressor.predict(x_train), color='blue')

plt.title('Height vs Weight - Training Values')
plt.xlabel('Height (in.)')
plt.ylabel('Weight (lbs)')
plt.show()

# displaying the values of height in the test feature matrix (x_test) and the real weight values with a scatter plot
plt.scatter(x_test_graph.values, y_test, color='green')

# displaying the regression line of predicted weight values generated by our model.
plt.plot(x_test_graph.values, predicted_weight, color='blue')

plt.title('Height vs Weight - Test Values')
plt.xlabel('Height (in.)')
plt.ylabel('Weight (lbs)')
plt.show()