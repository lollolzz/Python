#!/usr/bin/env python
# coding: utf-8

# # 10. 결측치
# 비어 있는 데이터

# In[1]:


import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df


# ## 데이터 채우기 fillna

# In[2]:


df.fillna('') # NaN 데이터를 빈 칸으로 채움


# In[3]:


df.fillna('없음')


# In[4]:


import numpy as np
df['학교'] = np.nan # 학교 데이터 전체를 NaN 으로 채움
df


# In[5]:


df.fillna('모름')


# In[8]:


df.fillna('모름', inplace=True)


# In[9]:


df


# In[10]:


import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df


# In[12]:


df['SW특기'].fillna('확인 중', inplace=True) # sw특기 데이터 중에서 NaN에 대해 채움


# In[13]:


df


# ##  데이터 제외하기 dropna

# In[14]:


import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df


# In[17]:


df.dropna(inplace=True) # 전체 데이터 중에서 NaN 을 포함하는 데이터 삭제


# In[18]:


df


# In[20]:


df = pd.read_excel('score.xlsx', index_col='지원번호')
df


# - axis : index or columns
# - how : any or all

# In[ ]:


df.dropna(axis='index', how='any') # NaN가 하나라도 있는 row 삭제 


# In[22]:


df.dropna(axis = 'columns') # NaN이 하나라도 있는 column 삭제


# In[23]:


df['학교'] = np.nan
df


# In[24]:


df.dropna(axis ='columns', how='all') # 데이터 전체가 NaN인 경우에만 Column 삭제

