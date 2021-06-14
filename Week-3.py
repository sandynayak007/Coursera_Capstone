#!/usr/bin/env python
# coding: utf-8

# In[51]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# ### Scrapping Wikipidia data for Toranto neighborhood

# In[52]:


url = "https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"
page=requests.get(url)
soup = BeautifulSoup(page.content,"html.parser")


# In[53]:


table_contents=[]
table = soup.find("table")


# ### Updating the data into list

# In[54]:


for row in table.findAll('td'):
    cell = {}
    if row.span.text=='Not assigned':
        pass
    else:
        cell['PostalCode'] = row.p.text[:3]
        cell['Borough'] = (row.span.text).split('(')[0]
        cell['Neighborhood'] = (((((row.span.text).split('(')[1]).strip(')')).replace(' /',',')).replace(')',' ')).strip(' ')
        table_contents.append(cell)


# In[55]:


df=pd.DataFrame(table_contents)


# ### Checking Not assigned values in the Neighborhood

# In[60]:


(df["Neighborhood"]=="Not assigned").value_counts()


# In[62]:


df.head()


# In[63]:


df.shape

