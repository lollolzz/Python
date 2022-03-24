#!/usr/bin/env python
# coding: utf-8

# # 8. 데이터 선택(iloc)
# 위치를 이용하여 원하는 row에서 원하는 col선택

# In[1]:


import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df


# In[3]:


df.iloc[0] # 0번째 위치의 데이터 


# In[4]:


df.iloc[4] # 4번째 위치의 데이터


# In[5]:


df.iloc[0:5] # 0 - 4 번째 위치의 데이터


# In[7]:


df.iloc[0, 1] # 0번째 위치의 1번째('학교') 데이터


# In[8]:


df.iloc[4, 2] # 5번 학생의 키 데이터(4번째 위치의 2번째(키) 데이터)


# In[10]:


df.iloc[[0, 1], 2] # 0, 1번째 위치의 학생의 2번째(키) 데이터


# In[11]:


df.iloc[[0, 1], [3, 4]] # 0, 1번째 위치의 학생의 3,4 번째 데이터(국어, 영어)


# In[12]:


df.iloc[0:5, 3:8] # 0 -4 번째 위치의 학생 중에서, 3 -7번째 데이터 (국어:사회)

