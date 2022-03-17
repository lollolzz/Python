#!/usr/bin/env python
# coding: utf-8

# ## 5.데이터 확인

# In[2]:


import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df


# ## DataFrame 확인
# 계산 가능한 데이터에 대해 Column 별로 데이터 갯수, 평균, 표준편차, 최소/최대값 등의 정보를 보여줌

# In[3]:


df.describe()


# In[4]:


df.info()


# In[5]:


df.head() # 처음 5개의 row를 가져옴 


# In[6]:


df.head(7) #처음 7개의 row를 가져옴 


# In[7]:


df.tail() # 마지막 5개 row를 가져옴 


# In[8]:


df.tail(3) #마지막 3개 row를 가져옴 


# In[9]:


df.values


# In[10]:


df.index


# In[12]:


df.columns


# In[16]:


df.shape # row, column 갯수 확인 


# ## Series확인

# In[18]:


df['키'].describe()


# In[19]:


df['키'].min()


# In[20]:


df['키'].max()


# In[21]:


df['키'].nlargest(3) # 키 큰 사람 순서대로 3명 데이터 


# In[22]:


df['키'].mean()


# In[23]:


df['키'].sum()


# In[25]:


df['SW특기'].count()


# In[27]:


df['학교'].unique() # unique 중복 제거 


# In[29]:


df['학교'].nunique() # 중복을 제거하고 학교가 몇개가 있는지를 나타탬 

