# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 22:27:15 2017

@author: welcome
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 16:34:38 2017

@author: welcome
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets,linear_model

# Function to get data
def get_data(file_name):
 data = pd.read_csv(file_name)
 X_parameter = []
 Y_parameter = []
 for x,y in zip(data['x'],data['y']):
       X_parameter.append([float(x)])
       Y_parameter.append(float(y))
 return X_parameter,Y_parameter

print get_data('egg1.csv')

# Function for Fitting our data to Linear model
def linear_model_main(X_parameters,Y_parameters,predict_value):
 
 # Create linear regression object
 regr = linear_model.LinearRegression()
 regr.fit(X_parameters, Y_parameters)
 predict_outcome = regr.predict(predict_value)
 predictions = {}
 predictions['residuals']=regr.residues_
 predictions['intercept'] = regr.intercept_
 predictions['coefficient'] = regr.coef_
 predictions['predicted_value'] = predict_outcome
 return predictions
 
X,Y = get_data('egg1.csv')
predictvalue = 38.5
result = linear_model_main(X,Y,predictvalue)
print "Residuals",result['residuals']
print "Intercept value " , result['intercept']
print "coefficient" , result['coefficient']
print "Predicted value: ",result['predicted_value']

# Function to show the resutls of linear fit model
def show_linear_line(X_parameters,Y_parameters):
 # Create linear regression object
 regr = linear_model.LinearRegression()
 regr.fit(X_parameters, Y_parameters)
 plt.scatter(X_parameters,Y_parameters,color='blue')
 plt.plot(X_parameters,regr.predict(X_parameters),color='red',linewidth=4)
 xticks=range(int(min(X_parameters)),int(max(X_parameters))+1)
 plt.xticks(X_parameters)
 plt.yticks(regr.predict(X_parameters))
 plt.show()
 
show_linear_line(X,Y)