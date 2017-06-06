# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:43:37 2017

@author: Li
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("Position_Salaries.csv")
X = dataset.iloc[:,1:2].values
Y = dataset.iloc[:,2]

# feature scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_Y = StandardScaler()
X = sc_X.fit_transform(X)
Y = sc_Y.fit_transform(Y)

# fit SVR to dataset
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X,Y)

# predict a new result from regression model
y_pred = sc_Y.inverse_transform(regressor.predict(sc_X.transform(np.array([[6.5]]))))

#Visualizing SVR model
X_grid = np.arange(min(X),max(X),0.1)
X_grid = X_grid.reshape((len(X_grid),1))
plt.scatter(X,Y, color = 'red')
plt.plot(X,Y, color = 'blue')
plt.title("SVR Regression Model")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()