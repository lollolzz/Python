#!/usr/bin/env python
# coding: utf-8

# # 9. 데이터 선택(조건)
# 조건에 해당하는 데이터 선택

# In[1]:


import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df


# In[2]:


df['키'] >= 185 # 학생들의 키가 185 이상인지 여부를 true/false


# In[3]:


filt = (df['키'] >= 185)
df[filt]


# In[4]:


df[~filt] # filter를 역으로 적용 


# In[5]:


df[df['키'] >= 185]


# In[6]:


df.loc[df['키'] >= 185, '수학'] # 키가 185 이상인 학생들의 수학 데이터


# In[7]:


df.loc[df['키'] >= 185, ['이름', '수학', '과학']] # 키가 185 이상인 학생들의 이름, 수학, 과학 데이터를 가져옴


# # 다양한 조건

# ### & 그리고

# In[8]:


df.loc[(df['키'] >= 185) & (df['학교'] == '북산고')] # 키가 185 이상인 북산고 학생 데이터


# ### 또는 |

# In[9]:


df.loc[(df['키'] < 170) | (df['키'] > 200)] # 키가 170 보다 작거나, 200 보다 큰 학생 데이터


# ## str 함수

# In[10]:


filt = df['이름'].str.startswith('송') # 송씨 성을 가진 사람
df[filt]


# In[12]:


filt = df['이름'].str.contains('태') # 이름에 '태'가 들어가는 사람 
df[filt]


# In[13]:


df[~filt] # 이름에 '태'가 들어가는 사람을 제외 


# In[15]:


langs = ["Python", "Java"]
filt = df['SW특기'].isin(langs) # sw 특기가 python이거나 java인 사람
df[filt]


# In[16]:


df


# In[19]:


langs = ["python", "java"]
filt = df["SW특기"].str.lower().isin(langs)
df[filt]


# In[20]:


filt = df['SW특기'].str.contains('Java')
df[filt]


# In[21]:


df['SW특기'].str.lower().isin(langs)


# In[23]:


df['SW특기'].str.contains('Java', na=True) # Nan 데이터에 대해서 true로 설정 


# In[24]:


df['SW특기'].str.contains('Java', na=False) # Nan 데이터에 대해서 False로 설정 


# In[25]:


filt = df['SW특기'].str.contains('Java', na=False)
df[filt]


# In[ ]:





# In[ ]:





# In[ ]:




