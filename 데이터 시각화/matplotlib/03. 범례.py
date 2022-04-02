#!/usr/bin/env python
# coding: utf-8

# # 3. 범례(legned)

# In[10]:


import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Georgia' # Mac
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스 글자가 깨지는 현상을 해결 


# In[11]:


x = [1, 2, 3]
y = [2, 4, 8]


# In[12]:


plt.plot(x, y, label='무슨 데이터')
plt.legend()


# In[13]:


plt.plot(x, y, label='무슨 데이터')
plt.legend(loc='upper right')


# In[14]:


plt.plot(x, y, label='무슨 데이터')
plt.legend(loc='lower right')


# In[16]:


plt.plot(x, y, label='범례')
plt.legend(loc=(0.7, 0.8)) # x축, y축 (0~1사이)


# In[ ]:





# In[ ]:





# In[ ]:




