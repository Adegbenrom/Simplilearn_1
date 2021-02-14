#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as pd
import pandas as pd


# In[66]:


olympic_series_participation =pd.Series([205,204,201,200,197], index=[2012,2008,2004,2000,1996])
olympic_series_country=pd.Series(["London","Beijing","Athens","Sydney","Atlanta"], 
                                index=[2012,2008,2004,2000,1996])
df_olympic_series= pd.DataFrame({"Participating Countries Number":olympic_series_participation,
                               "Host Cities":olympic_series_country} )


# In[20]:


df_olympic_series


# In[132]:


df_olympic_series= pd.DataFrame({"Participating Countries Number":[205,204,201,200,197],
                               "Host Cities":["London","Beijing","Athens","Sydney","Atlanta"]},
                                              [2012,2008,2004,2000,1996])
df_olympic_series


# In[29]:


df_olympic_series.tail(2)


# In[34]:


df_olympic_series.head(2)


# In[33]:


df_olympic_series[["Host Cities"]]


# In[35]:


df_olympic_series["Host Cities"]


# In[ ]:


# Locate by label


# In[38]:


df_olympic_series.loc[[2004]]


# In[ ]:


# Locate by index 


# In[41]:


df_olympic_series.iloc[[2]]


# In[43]:


df_olympic_series.iloc[0:]


# In[48]:


df_olympic_series.iat[3,1]


# In[ ]:


# using boolean expression for condition


# In[52]:


df_olympic_series[df_olympic_series["Participating Countries Number"]>200]


# In[89]:


df_olympic_series["Host Cities"] =="London"


# In[64]:


df_olympic_series[df_olympic_series["Host Cities"] =="London"]


# In[ ]:


# Missing Values


# In[82]:


import pandas as pd


# In[83]:


first_series=pd.Series([1,2,3,4,5], ["a","b","c","d","e"])
second_series=pd.Series([10,20,30,40,50], ["c","e","f","g","h"])
sum_of_series=first_series+second_series


# In[91]:


sum_of_series


# In[92]:


# drop/remove the NaN from the data
drop_NaN = sum_of_series.dropna()


# In[93]:


drop_NaN


# In[105]:


# fill the NaN of the data 0 or "-"
fill_NaN = sum_of_series.fillna('0.0')


# In[106]:


fill_NaN


# In[108]:


kk=sum_of_series.copy()


# In[109]:


kk


# In[113]:


# declare movie rating dataframe: ratings 1 to 5 (star rating)


# In[123]:


import pandas as pd


# In[125]:


df_movie_rating=pd.DataFrame({"movie 1":[5,4,3,3,2,1], "movie 2":[4,5,2,3,4,2]}, ["Tom","Pete",
                                                                                "Ram","Ted","Sol",
                                                                                  "Kin"])


# In[127]:


df_movie_rating


# In[134]:


def movie_rating(rating):
    if rating==5:
        return "A"
    if rating==4:
        return "B"
    if rating==3:
        return "C"
    else:
        return "D"
    


# In[ ]:


# apply map


# In[135]:


df_movie_rating.applymap(movie_rating)


# In[ ]:


# DataFrame with statistical operations


# In[138]:


df_test_scores = pd.DataFrame({"Test 1":[95,84,73,88,82,61],"Test 2":[74,85,82,73,77,79]}, 
                              ["Jac","Pat","Lew","Ric","Kel","Sol"])


# In[139]:


df_test_scores


# In[144]:


(df_test_scores.tail(2))


# In[146]:


df_test_scores.max()


# In[147]:


df_test_scores.min()


# In[148]:


df_test_scores.mean()


# In[149]:


df_test_scores.std()


# In[154]:


df_test_scores.var()


# In[159]:


df_test_scores.median()


# In[183]:


df_president_name = pd.DataFrame({"First":["Geo","Bil","Ron","Jim","Geo"],"Last":["Bus","Cli","Reg",
                                                                                 "Car","Was"]},
                                                             ["a","b","c","d","e"])


# In[184]:


df_president_name


# In[186]:


grp_data =grouped.get_group("Geo")


# In[187]:


grp_data


# In[220]:


with open("C:/Users/user/Desktop/Data.xlsx","r") as openfile:
    print(openfile.read())


# In[257]:


import pandas as pd


# In[258]:


df = pd.read_excel(r"C:/Users/user/Desktop/Book1.xlsx")


# In[259]:


print(df)


# In[260]:


df.max()


# In[261]:


df.mean()


# In[262]:


df.var()


# In[263]:


df.std()


# In[ ]:


# Data Standardization of the table below


# In[274]:


import pandas as pd


# In[275]:


df_test_scores


# In[296]:


def standardize_data(data):
    return(data-data.mean())/data.std()


# In[297]:


def standardize_tests_scores(datafrm):
    return datafrm.apply(standardize_data)


# In[298]:


standardize_tests_scores(df_test_scores)


# In[ ]:


# Pandas Data Operation:


# In[409]:


import pandas as pd


# In[416]:


student_math=pd.DataFrame({"student":["Tom","Jac","Dan","Ram","Jef","Dav"],"math score":
                           [10,56,31,85,9,22]})
student_science=pd.DataFrame({"student":["Tom","Ram","Dav"], "sci score":[10,12,22]})


# In[417]:


full_table=pd.concat([student_math, student_science], ignore_index=True)


# In[418]:


full_table


# In[420]:


full_table.sort_values(by=['student'], inplace=True, ascending=False)


# In[421]:


full_table


# In[423]:


full_table.fillna("-")


# In[350]:


#marge both data to form one - by defaut, data with same index/key get merged


# In[351]:


pd.merge(student_math, student_science)


# In[352]:


# merge with key on students


# In[353]:


pd.merge(student_math,student_science, on="student")


# In[354]:


pd.merge(student_math,student_science, on="ID", how="left").fillna("x")


# In[362]:


pd.concat([student_math, student_science], ignore_index=True)


# In[ ]:




