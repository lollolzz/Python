#!/usr/bin/env python
# coding: utf-8

# # 11. 데이터 정렬

# In[1]:


import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df


# In[2]:


df.sort_values('키') # 키 기준으로 오름차순 정렬 


# In[3]:


df.sort_values('키', ascending=False) # 키 기준으로 내림차순 정렬 


# In[6]:


df.sort_values(['수학', '영어']) # 수학, 영어 점수 기준으로 오름차순


# In[7]:


df.sort_values(['수학', '영어'], ascending=False) # 수학, 영어 점수 기준으로 내림차수


# In[8]:


df.sort_values(['수학', '영어'], ascending=[True, False]) # 수학 점수는 오름차순으로, 영어점수는 내림차순으로 정렬


# In[9]:


df['키'].sort_values()


# In[10]:


df['키'].sort_values(ascending=False)


# In[11]:


df.sort_index()


# In[12]:


df.sort_index(ascending=False)


# In[ ]:





# In[ ]:





# In[ ]:




