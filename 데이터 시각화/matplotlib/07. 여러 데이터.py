#!/usr/bin/env python
# coding: utf-8

# ## 7. 여러 데이터

# In[1]:


import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Georgia' # Mac
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스 글자가 깨지는 현상을 해결 


# In[2]:


x = [1, 2, 3]
y = [2, 4, 8]


# In[3]:


plt.plot(x, y)


# ## COVID-19 백신 종류별 접종 인구

# In[4]:


days = [1, 2, 3] # 10월 1일, 2일, 3일 
az = [2, 4, 8] # 단위 만명 1일부터 3일까지 아스트라제네카 접종인구
pfizer = [5, 1, 3] # 화이자
moderna = [1, 2, 3] # 모더나 

plt.plot(days, az)
plt.plot(days, pfizer)
plt.plot(days, moderna)


# In[7]:


plt.plot(days, az, label='az')
plt.plot(days, pfizer, label='pfizer', marker='o', linestyle='--')
plt.plot(days, moderna, label='moderna', marker='s', ls='-.')

plt.legend(ncol=3)

