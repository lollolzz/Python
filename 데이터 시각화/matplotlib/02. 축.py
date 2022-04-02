#!/usr/bin/env python
# coding: utf-8

# # 2. 축

# In[6]:


import matplotlib.pyplot as plt

import matplotlib
matplotlib.rcParams['font.family'] = 'Georgia' # Mac
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스 글자가 깨지는 현상을 해결 


# In[7]:


x = [1, 2, 3]
y = [2, 4, 8]


# In[8]:


plt.plot(x, y)
plt.title('꺽은선 그래프', fontdict={'family':'Georgia', 'size':20}) 
# 개별 폰트 설정


# In[11]:


plt.plot(x, y) # x, y에 대한 정보가 없는 상태
plt.xlabel('X축', color='red', loc='right') # left, center, right
plt.ylabel('Y축', color='#00aa00', loc='top') # top, center, bottom


# In[12]:


plt.plot(x, y)
plt.xticks([1, 2, 3])
plt.yticks([3, 6, 9, 12])
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




