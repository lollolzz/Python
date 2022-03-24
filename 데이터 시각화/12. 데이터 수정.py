#!/usr/bin/env python
# coding: utf-8

# # 12. 데이터 수정

# In[1]:


import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df


# # Column 수정

# In[2]:


df['학교'].replace({'북산고':'상북고', '능남고':'사파고'})


# In[3]:


df['학교'].replace({'북산고':'상북고'}, inplace=True)


# In[4]:


df


# In[5]:


df['SW특기'].str.lower()


# In[6]:


df['SW특기'] = df['SW특기'].str.lower()


# In[7]:


df


# In[8]:


df['SW특기'] = df['SW특기'].str.upper()
df


# In[9]:


df['학교'] = df['학교'] + '등학교' # 학교 데이터 + 등학교
df


# ## Column 추가

# In[10]:


df['총합'] = df['국어'] + df['영어'] + df['수학'] + df['과학'] + df['사회']
df


# In[11]:


df['결과'] = 'Fail' # 결과 Column을 추가하고 전체 데이터는 Fail로 초기화
df


# In[12]:


df.loc[df['총합'] > 400, '결과'] = 'Pass' # 총합이 400보다 큰 데이터에 대해서 결과를 Pass로 업데이트
df


# ## Column 삭제

# In[13]:


df.drop(columns=['총합']) # 총합 Column을 삭제 
df


# In[14]:


df.drop(columns = ['국어', '영어', '수학']) # 국어, 영어, 수학 Column을 삭제


# In[15]:


df


# ## Row 삭제 

# In[16]:


df.drop(index='4번') # 4번 학생 데이터 row를 삭제


# In[17]:


filt = df['수학'] < 80 # 수학 점수 80점 미만 학생 필터링
df[filt]


# In[18]:


df[filt].index


# In[19]:


df.drop(index=df[filt].index)


# In[20]:


df


# ## Row 추가

# In[21]:


df.loc['9번'] = ['이정환', '해남고등학교', 184, 90, 90, 90, 90, 90, 'Kotlin', 450, 'Pass'] # 새로운 row 추가
df


# ## Cell 수정 

# In[22]:


df.loc['4번', 'SW특기'] = 'Python' # 4번 학생의 sw특기 데이터를 python으로 변경
df


# In[23]:


df.loc['5번', ['학교', 'SW특기']] = ['능남고등학교', 'C'] # 5번 학생의 학교는 능남고등학교로, SW특기는 c로 변겨
df


# #  Column 순서 변경

# In[24]:


cols = list(df.columns)
cols


# In[25]:


df = df[[cols[-1]] + cols[0:-1]] # 맨 뒤에 있는 결과 Column을 앞오르 가져오고 나머지 column들과 합쳐서 순서 변경
df


# In[26]:


df = df[['결과', '이름', '학교']]
df


# ## Column 이름 변경 

# In[27]:


df


# In[28]:


df.columns


# In[29]:


df.columns = ['Result', 'Name', 'School']


# In[30]:


df

