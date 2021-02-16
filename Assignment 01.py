#!/usr/bin/env python
# coding: utf-8

# <img src="http://cfs22.simplicdn.net/ice9/new_logo.svgz "/>
# 
# # Assignment 01: Evaluate the Ad Budget Dataset of XYZ Firm
# 
# *The comments/sections provided are your cues to perform the assignment. You don't need to limit yourself to the number of rows/cells provided. You can add additional rows in each section to add more lines of code.*
# 
# *If at any point in time you need help on solving this assignment, view our demo video to understand the different steps of the code.*
# 
# **Happy coding!**
# 
# * * *

# #### 1: Import the dataset

# In[64]:


#Import the required libraries
import pandas as pd


# In[65]:


#Import the advertising dataset

df_advert = pd.read_csv(r"C:\Users\user\Documents\IT Courses\Machine Learning\Simplilearning\Lesson 8\Advertising Budget and Sales.csv", index_col=0)


# #### 2: Analyze the dataset

# In[66]:


#View the initial few records of the dataset
df_advert.head()


# In[67]:


#Check the total number of elements in the dataset
df_advert.shape


# In[68]:


df_advert.size


# #### 3: Find the features or media channels used by the firm

# In[69]:


#Check the number of observations (rows) and attributes (columns) in the dataset
df_advert.columns


# In[70]:


#View the names of each of the attributes
df_advert.count()


# #### 4: Create objects to train and test the model; find the sales figures for each channel

# In[88]:


#Create a feature object from the columns
x_feature = df_advert[["Newspaper Ad Budget ($)","Radio Ad Budget ($)","TV Ad Budget ($)"]]


# In[89]:


#View the feature object
X_feature.head()


# In[90]:


#Create a target object (Hint: use the sales column as it is the response of the dataset)
Y_target = df_advert[["Sales ($)"]]


# In[91]:


#View the target object
Y_target.head()


# In[92]:


#Verify if all the observations have been captured in the feature object
X_feature.shape


# In[93]:


#Verify if all the observations have been captured in the target object
Y_target.shape


# #### 5: Split the original dataset into training and testing datasets for the model

# In[94]:


#Split the dataset (by default, 75% is the training data and 25% is the testing data)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test= train_test_split(X_feature, Y_target, random_state=1)


# In[95]:


#Verify if the training and testing datasets are split correctly (Hint: use the shape() method)
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)


# #### 6: Create a model  to predict the sales outcome

# In[96]:


#Create a linear regression model
from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linreg.fit(x_train,y_train)


# In[97]:


#Print the intercept and coefficients 
print(linreg.intercept_)
print(linreg.coef_)


# In[98]:


#Predict the outcome for the testing dataset
y_pred = linreg.predict(x_test)
y_pred


# #### 7: Calculate the Mean Square Error (MSE)

# In[99]:


#Import required libraries for calculating MSE (mean square error)
from sklearn import metrics
import numpy as np


# In[100]:


#Calculate the MSE
print(np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

