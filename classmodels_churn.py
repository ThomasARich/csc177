import pandas as pd
from sklearn.model_selection import train_test_split # Import train_test_split function

dataset = pd.read_csv('Churn_Modelling.csv')

# Drop columns not selected as features
dataset.drop(dataset.iloc[:, 0:3], inplace = True, axis = 1) # Drops RowNumber, CustomerId, and Surname.
dataset.drop(dataset.iloc[:, 1:4], inplace = True, axis = 1) # Drops Geography, Gender, and Age.

x = dataset[['CreditScore', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'IsActiveMember', 'EstimatedSalary']]  # Independent Variables
y = dataset['Exited']  # Dependent Variable

print(dataset)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, shuffle=True) # 70% training and 30% test