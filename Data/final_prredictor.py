# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 12:23:48 2018

@author: Akshaj
"""

# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('final_data.csv')
X = dataset.iloc[:,2:4].values
y = dataset.iloc[:,4].values

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
# Predicting the Test set results
y_pred = regressor.predict(X_test)

z=np.zeros((1,2))
z[0,0]=input("Enter opening price")
z[0,1]=input("Enter volume")
print (z)
print("Today's high is" + str(regressor.predict(z)))