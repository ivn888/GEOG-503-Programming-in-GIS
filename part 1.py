#Data Preprocessing for machine learning

#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#show the full array instead of shortened ones
np.set_printoptions(threshold=np.inf)

#import dataset
dataset = pd.read_csv('Data.csv')

## X take all the values except the last line, Y take the last line
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,3].values

#taking care of missing data
from sklearn.preprocessing import Imputer

imputer = Imputer("NaN","mean")
## fit imputer to dataset X
imputer = imputer.fit(X[:,1:3])
### fit the missing data into matrix X by column
X[:,1:3] = imputer.transform(X[:,1:3])

#Encode categorical data (text) to numbers
from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()
X[:,0] = labelencoder_X.fit_transform(X[:,0])

labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y)

#dummy encoders for many categories
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(n_values="auto",categorical_features=[0])
X = onehotencoder.fit_transform(X).toarray()

#splitting the dataset into training and testing set
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.5,
                                                    random_state = 42)

#feature scaling (put independent variables into same range/scale to 
                  #prevent one from being dominated by the other)
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

##no scaling needed for dependent variable Y because range is large.