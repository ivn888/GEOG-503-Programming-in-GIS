# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 10:53:53 2017

@author: Li
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("50_Startups.csv")
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,4].values

# Encoding the categorical features
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,3] = labelencoder_X.fit_transform(X[:,3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

# Avoiding dummy variable trap 
## Removing the first column
X = X[:, 1:]

# Spliting the train and test sets
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.5, 
                                                    random_state = 0)

# No need to apply feature scaling to multiple linear regression bc the
# library will take care of that.

# Fitting multiple linear regression to training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

# Predicting the test set results
## Comparing the observation and predicted results
y_pred_test = regressor.predict(X_test)

# Building the optimal model using Backward Elimination
import statsmodels.formula.api as sm

## add a column of '1' as the first column in matrix of features X
X = np.append(arr = np.ones((50,1)).astype(int), values = X, axis = 1)
                           # 50 rows, 1 column
                                    # prevent data type error
                                                       # axis=0 - row
                                                       # axis=1 - column

# initializing a team of optimal independent variables
X_opt = X[:, [0,1,2,3,4,5]]                                                       

# Create a new regressor for ordinary least squares OLS
# Fit regression model to OLS
regressor_OLS = sm.OLS(endog=Y, exog=X_opt).fit()

# Get p value using summary function
regressor_OLS.summary()      

# Remove 2 with the highest p value
X_opt = X[:, [0,1,3,4,5]]
regressor_OLS = sm.OLS(Y,X_opt).fit()
regressor_OLS.summary()      

# 对照 original X table来挨个移除 p-value, 注意不要看错index number
X_opt = X[:, [0,3,4,5]]
regressor_OLS = sm.OLS(Y,X_opt).fit()
regressor_OLS.summary()

X_opt = X[:, [0,3,5]]
regressor_OLS = sm.OLS(Y,X_opt).fit()
regressor_OLS.summary()

X_opt = X[:, [0,3]]
regressor_OLS = sm.OLS(Y,X_opt).fit()
regressor_OLS.summary()                                    