#!/usr/bin/env python
# coding: utf-8

# # Matplotlib
# 다양한 형태의 그래프를 통해서 데이터 시각화를 할 수 있는 라이브러리 

# In[1]:


import matplotlib.pyplot as plt


# ## 1. 그래프 기본

# In[2]:


x = [1, 2, 3]
y = [2, 4, 8]

plt.plot(x,y)


# In[3]:


print(plt.plot(x, y))


# In[4]:


plt.plot(x,y)
plt.show() # 그래프 위의 글을 보기 싫을 경우 show사용


# ## Title 설정

# In[5]:


plt.plot(x, y)
plt.title('Line Graph')


# In[6]:


plt.plot(x, y)
plt.title('꺽은선 그래프')


# ## 한글 폰트 설정

# In[11]:


import matplotlib
matplotlib.rcParams['font.family'] = 'cmss10' # Mac
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스 글자가 깨지는 현상을 해결 


# In[12]:


import matplotlib.font_manager as fm
fm.fontManager.ttflist # 사용가능한 폰트 목록 확인
[f.name for f in fm.fontManager.ttflist]


# In[13]:


plt.plot(x, y)
plt.title('예시 그래프') # 한글 폰트 설정을 하여 정상 출려된다.


# In[14]:


plt.plot([-1, 0, 1], [-5, -1, 2])


# In[ ]:




