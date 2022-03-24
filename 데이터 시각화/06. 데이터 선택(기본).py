#!/usr/bin/env python
# coding: utf-8

# # 6. 데이터 선택(기본)

# In[1]:


import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df


# ## Column 선택(label)

# In[3]:


df['이름']


# In[4]:


df['키']


# In[5]:


df[['이름', '키']]


# ## Column 선택(정수 index)

# In[6]:


df.columns


# In[7]:


df.columns[0]


# In[9]:


df.columns[2]


# In[10]:


df[df.columns[0]] # df['이름'] 과 동일한 동작 


# In[11]:


df[df.columns[-1]] # 맨 끝에 있는 값을 가져옴


# # 슬라이싱

# In[12]:


df


# In[13]:


df['영어'][0:5] # 0 - 4 까지 영어 점수 데이터 가져옴 


# In[14]:


df[['이름', '키']][:3] # 처음 3명의 이름, 키 정보를 가져옴


# In[15]:


df[3:]

