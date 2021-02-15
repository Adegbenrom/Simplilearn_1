#!/usr/bin/env python
# coding: utf-8

# <img src="http://cfs22.simplicdn.net/ice9/new_logo.svgz "/>
# 
# # Assignment 01: Evaluate the FAA Dataset
# 
# *The comments/sections provided are your cues to perform the assignment. You don't need to limit yourself to the number of rows/cells provided. You can add additional rows in each section to add more lines of code.*
# 
# *If at any point in time you need help on solving this assignment, view our demo video to understand the different steps of the code.*
# 
# **Happy coding!**
# 
# * * *

# #### 1: VIew and import the dataset

# In[360]:


#Import necessary libraries

import pandas as pd


# In[363]:


#Import the FAA (Federal Aviation Authority) dataset
FAA_data=pd.read_csv(r"C:\Users\user\Documents\IT Courses\Machine Learning\Simplilearning\Lesson 7 -1/faa_ai_prelim.csv")


# #### 2: View and understand the dataset

# In[362]:


#View the dataset shape
FAA_data.shape


# In[365]:


#View the first five observations
FAA_data.head()


# In[367]:


#View all the columns present in the dataset
FAA_data.columns


# #### 3: Extract the following attributes from the dataset:
# 1. Aircraft make name
# 2. State name
# 3. Aircraft model name
# 4. Text information
# 5. Flight phase
# 6. Event description type
# 7. Fatal flag

# In[378]:


#Create a new dataframe with only the required columns
New_FAA_data= FAA_data[["ACFT_MAKE_NAME","LOC_STATE_NAME","ACFT_MODEL_NAME","RMK_TEXT",
          "FLT_PHASE","FATAL_FLAG","EVENT_TYPE_DESC"]]


# In[379]:


#Display new dataset
New_FAA_data.head()


# In[380]:


#View the type of the object
type(New_FAA_data)


# In[381]:


#Check if the dataframe contains all the required attributes
New_FAA_data.columns


# #### 4. Clean the dataset and replace the fatal flag NaN with “No”

# In[382]:


#Replace all Fatal Flag missing values with required output and retain same variable 'New_FAA_data'

New_FAA_data['FATAL_FLAG'].fillna(value="No", inplace=True)


# In[384]:


#Verify if the missing values are replaced by "No"
New_FAA_data.head()


# In[388]:


#Check the number of observations
New_FAA_data.shape


# #### 5. Remove all the observations where aircraft names are not available

# In[392]:


#Drop the unwanted values/observations from the dataset
New_FAA_Data=FAA_data.dropna(subset=['ACFT_MAKE_NAME'])


# #### 6. Find the aircraft types and their occurrences in the dataset

# In[393]:


#Check the number of observations now to compare it with the original dataset and see how many values have been dropped
print(f"New_FAA_data Size is: {Final_FAA_Data.shape}")
print(f"FAA_Data Size is: {FAA_data.shape}")


# In[394]:


#Group the dataset by aircraft name
Aircraft_Type=New_FAA_Data.groupby("ACFT_MAKE_NAME")


# In[353]:


#View the number of times each aircraft type appears in the dataset (Hint: use the size() method)
Aircraft_Type.size()


# #### 7: Display the observations where fatal flag is “Yes”

# In[398]:


#Group the dataset by fatal flag
Fatal_Accident= New_FAA_data.groupby("FATAL_FLAG")


# In[399]:


#View the total number of fatal and non-fatal accidents
Fatal_Accident.size()


# In[403]:


#select the accidents with fatality (Fatal Flag values = Yes)

Accident_with_fatality= Fatal_Accident.get_group("Yes")


# In[401]:


#view accident with fatality
Accident_with_fatality


# In[ ]:




