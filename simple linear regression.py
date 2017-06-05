# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 20:49:15 2017

@author: Li
"""
#simple linear regression

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("Salary_Data.csv")

## index column does not count as column.
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,1].values

# splitting dataset into training and testing sets
from sklearn.cross_validation import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.5, 
                                                    random_state = 0)

# Fitting simple linear regression to training set
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, Y_train) 
                    ## reshape training set to matrix using numpy 
                    
# Predicting the test set results
y_pred_test = regressor.predict(X_test)

# Visualizing the training set results
## make a scatterplot of the observation points in red
plt.scatter(X_train, Y_train, color = 'red')
## plot the regression line in blue
y_pred_train = regressor.predict(X_train)
plt.plot(X_train, y_pred_train, color = 'blue')

plt.title('Salary vs Experience (Training set)')
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()

# Visualizing the testing set results
plt.scatter(X_test, Y_test, color = 'red')
plt.plot(X_test, y_pred_test, color = 'blue')
plt.title('Salary vs Experience (Testing set)')
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()