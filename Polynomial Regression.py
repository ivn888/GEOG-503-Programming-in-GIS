# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 20:20:09 2017

@author: Li
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("Position_Salaries.csv")

## even X only has one column, it is better to have a matrix, not vector
X = dataset.iloc[:, 1:2].values
Y = dataset.iloc[:, 2].values

# No need to split training and testing set bc too few samples
# No need for feature scaling

# Two models will be built for comparison
## Fitting linear regression model to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,Y)

# Fitting polynomial regression model to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=4)
## this poly_reg is a tool that will transform matrix X into a new 
     # matrix feature X_poly, which will contain X, X^2...
X_poly = poly_reg.fit_transform(X)

# Fit a new linear regression model to X_poly and Y
lin_reg2 = LinearRegression()
lin_reg2.fit(X_poly,Y)

# Visualizing the linear regression results
plt.scatter(X,Y, color = 'red')
plt.plot(X,lin_reg.predict(X), color = 'blue')
plt.title("Linear Regression")
plt.xlabel("Level")
plt.ylabel("Salary")
plt.show()

# Visualizing the polynomial regression results
plt.scatter(X,Y, color = 'red')
plt.plot(X, lin_reg2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.title("Polynomial Regression")
plt.xlabel("Level")
plt.ylabel("Salary")
plt.show()

## 精确到0.1
X_grid = np.arange(min(X),max(X),0.1)
X_grid = X_grid.reshape((len(X_grid), 1))

plt.scatter(X,Y, color = 'red')
plt.plot(X_grid, lin_reg2.predict(poly_reg.fit_transform(X_grid)), color = 'blue')
plt.title("Polynomial Regression")
plt.xlabel("Level")
plt.ylabel("Salary")
plt.show()

# Predicting a new result with linear regression
lin_reg.predict(6.5)

# Predicting a new result with polynomial regression
lin_reg2.predict(poly_reg.fit_transform(6.5))