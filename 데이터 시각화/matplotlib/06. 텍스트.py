#!/usr/bin/env python
# coding: utf-8

# # 6. 텍스트

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


# In[14]:


plt.plot(x, y, marker='o')

for idx, txt in enumerate(y):
    plt.text(x[idx], y[idx] + 0.3, txt, ha='center', color='red')


# In[ ]:





# In[ ]:




