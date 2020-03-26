
# coding: utf-8

# In[2]:


import pandas as pd
# sreies
# data frames


# In[5]:


#obtain series from python dictionaries
# keys of dictionaries act as index or label for values
dcit = {'a': 3, 'b':"cat" , 'c': 2.5}
dict
q= pd.Series(dict)
q


# In[9]:


df = pd.Series([100,'Cat', 310, 'gog', 500], index= ['amy', 'Raz', 'Julia', 'Gregg','Carlo'])
df


# In[10]:


df.loc[['amy','Carlo']]


# In[7]:


oneD = pd.Series([100,'cat', 310, 'gog', 500], index = ['amy','boby', 'cat', 'don', 'emma'])
oneD


# In[14]:


oneD = pd.Series([100,'cat', 310, 'gog', 500], ['amy','boby', 'cat', 'don', 'emma'])
oneD


# In[15]:


oneD.loc[['dog', 'emma']]


# In[13]:


oneD[[0,3,4]] # index value at index 0,3,4


# In[11]:


df[[1,2,3]]


# In[14]:


oneD.iloc[1]


# In[12]:


df.iloc[1]


# In[17]:


'cat' in oneD # search among indexes


# In[17]:


'Raz' in df


# In[18]:


'Dog' in oneD


# In[20]:


# dataframe
d= { 'A': pd.Series([100,200,300], index = ['apple', 'pear', 'orange']),
   'B' : pd.Series([111, 112, 113,114] , index = ['apple',  'pear', 'orange', 'melon'])}


# In[29]:


midterm = { 'W1':pd.Series ([90,95,80,87], index = ['EM224', 'EM225','EM226', 'EM227']),
          'W2': pd.Series([70,85,82], index=  ['EM228', 'EM229','EM223'])
         }


# In[30]:


mt = pd.DataFrame(midterm)
print(mt)


# In[34]:


pd.DataFrame(mt, index = ['EM224', 'EM228','EM229', 'EM227'], columns = ['W2','W1'])


# In[23]:


df = pd.DataFrame(d)
print(df)


# In[24]:


print(type(df))


# In[27]:


print(type(mt))
mt.index
mt.columns


# In[25]:


df.index # rows


# In[26]:


df.columns


# In[29]:


pd.DataFrame(df, index = ['apple', 'pear', 'orange','melon'], columns = ['A']) # specify which row/column we want to see


# #  reading in CSv

# In[35]:


import numpy as np
import pandas as pd


# In[32]:


file = 'Regression Data-1.csv'
df1 = pd.read_csv(file)
df1.head()


# In[53]:


import numpy as np
test= pd.read_csv('Test.csv')
#test = test.fillna(0)
#test = test.dropna()
#test.head(20)
x = test['Frequency']
std = np.std(x)
print(std)


# In[38]:


test.tail()


# In[34]:


df1= pd.read_csv(file,sep =',')# if the data is not clean and has "," between them so we use the seperator
df1.head()


# In[38]:


df1= pd.read_csv('TODO.txt',sep ='\t')# if the data is in text format
df1.head()


# # reading Excel file

# In[50]:


import os
os.getcwd()


# In[51]:


file = 'Regression Data-1.xlsx'
x1 = pd.ExcelFile(file) # open the file
print(x1.sheet_names) # go through different sheets


# In[52]:


df1 = x1.parse('Sheet1') # load a sheet to a data frame
df1.head()


# # Reading JSON

# In[49]:


import json


# In[56]:


df= pd.read_json('skorea.json')
df.head(2)


# In[57]:


df.shape


# In[60]:


web = pd.read_json('https://api.github.com/repos/pydata/pandas/issues?per_page=5')
web.head(4)


# #  reading Webpage

# In[61]:


import html5lib


# In[73]:


uss = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
u = uss[0]
#print(type(uss))
print(u)


# In[68]:


#what if we have more than 1 table in my webpage? instead of [0] we take [1], this meanse eachtable will locate in a new location per t]list

whsPH=pd.read_html('https://en.wikipedia.org/wiki/List_of_World_Heritage_Sites_in_the_Philippines') 


# In[69]:


whs_phl = whsPH[0] #grab dataframe from index 1, table 2 of the tentative WHS sites
print(whs_phl)


# In[70]:


whs_phl = whsPH[1] #grab dataframe from index 1, table 2 of the tentative WHS sites
print(whs_phl)


# In[71]:


whs_phl = whsPH[2] #grab dataframe from index 1, table 2 of the tentative WHS sites
print(whs_phl)

