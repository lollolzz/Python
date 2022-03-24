#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df


# In[5]:


df['학교'] = df['학교'] + '등학교'
df


# In[6]:


df['키'] = df['키'] + 'cm'
df


# ## 데이터 함수 적용(apply)

# In[10]:


# 키 뒤에 cm을 붙이는 역할
def add_cm(height):
    return str(height) + 'cm'

df['키'] = df['키'].apply(add_cm) # 키 데이터에 대해서 add_cm 함수를 호출한 결과 데이터를 반영
df


# In[13]:


def capitalize(lang):
    if pd.notnull(lang): #NaM이 아닌지
        return lang.capitalize() # 첫 글자는 대문자로, 나머지는 소문자로
    return lang

df['SW특기'] = df['SW특기'].apply(capitalize)
df


# In[14]:


df['SW특기'].str.capitalize()


# In[ ]:





# In[ ]:





# In[ ]:




