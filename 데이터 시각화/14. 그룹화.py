#!/usr/bin/env python
# coding: utf-8

# # 14. 그룹화
# 동일한 값을 가진 것들끼리 합쳐서 통계 또는 평균 등의 값을 계산하기 위해 사용

# In[1]:


import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df


# In[2]:


df.groupby('학교')


# In[3]:


df.groupby('학교').get_group('북산고')


# In[4]:


df.groupby('학교').get_group('능남고')


# In[5]:


df.groupby('학교').mean() # 계산 가능한 데이터들의 평균값


# In[6]:


df.groupby('학교').size() # 각 그룹의 크기


# In[7]:


df.groupby('학교').size()['능남고'] # 학교로 그룹화를 한 뒤에 능남고에 해당하는 데이터 수


# In[8]:


df.groupby('학교')['키'].mean() # 학교로 그룹화를 한 뒤에 키의 평균 데이터


# In[10]:


df.groupby('학교')[['국어', '영어', '수학']].mean() # 학교로 그룹화를 한 뒤에 영어, 국어, 수학 평균 데이터


# In[11]:


df['학년'] = [3, 3, 2, 1, 1, 3, 2, 2] # 학년 Column을 추가
df


# In[13]:


df.groupby(['학교', '학년']).mean() # 학교별, 학년별 평균 데이터


# In[14]:


df.groupby('학년').mean() # 학년별 평균 데이터


# In[15]:


df.groupby('학년').mean().sort_values('키')


# In[16]:


df.groupby(['학교', '학년']).sum()


# In[19]:


df.groupby('학교')[['이름', 'SW특기']].count() # 학교로 그룹화를 한 뒤에 각 학교별 데이터의 수를 가져옴


# In[21]:


school = df.groupby('학교')
school['학년'].value_counts() # 학교로 그룹화를 한 뒤에 학년별 학생 수를 가져옴


# In[24]:


school['학년'].value_counts().loc['북산고'] # 학교로 그룹화를 한 뒤에 북산고에 대해서 학년별 학생 수를 가져옴


# In[25]:


school['학년'].value_counts().loc['능남고']# 학교로 그룹화를 한 뒤에 능남고에 대해서 학년별 학생 수를 가져옴


# In[26]:


school['학년'].value_counts(normalize=True).loc['북산고'] # 학생들의 수 데이터를 퍼센트로 비교하여 가져옴


# In[ ]:




