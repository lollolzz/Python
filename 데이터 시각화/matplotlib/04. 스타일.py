#!/usr/bin/env python
# coding: utf-8

# # 4. 스타일
# 데이터 시각화는 테이블 데이터를 시각화하는거라 스타일 작업도 중요

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


# In[4]:


plt.plot(x, y, linewidth=5)


# In[5]:


plt.plot(x, y, marker='o')


# In[6]:


plt.plot(x, y, marker='o', linestyle='None')


# In[7]:


plt.plot(x, y, marker='v')


# In[8]:


plt.plot(x, y, marker='v', markersize=10)


# In[9]:


plt.plot(x, y, marker='x', markersize=10)


# In[10]:


plt.plot(x, y, marker='x', markersize=10, markeredgecolor='red')


# In[13]:


plt.plot(x, y, marker='o', markersize=20, markeredgecolor='red', markerfacecolor='yellow')


# ## 선 스타일

# In[16]:


plt.plot(x, y, linestyle=':')


# In[17]:


plt.plot(x, y, linestyle='--')


# In[18]:


plt.plot(x, y, linestyle='-.')


# ## 색깔

# In[19]:


plt.plot(x, y, color='pink')


# In[20]:


plt.plot(x, y, color='#ff0000')


# In[21]:


plt.plot(x, y, color='b')


# In[22]:


plt.plot(x, y, color='g')


# ## 포맷

# In[23]:


plt.plot(x, y, 'ro--') # color, marker, linestyle


# In[24]:


plt.plot(x, y, 'bv:')


# In[26]:


plt.plot(x, y, 'go')


# In[27]:


plt.plot(x, y, color='g', marker='o', linestyle='None')


# ## 축약어

# In[29]:


plt.plot(x, y, marker='o', mfc='red', ms=10, mec='blue', ls=':')


# ## 투명도

# In[33]:


plt.plot(x, y, marker='o', mfc='red', ms=10, alpha=0.1) # 투명도 (0-1)


# ## 그래프 크기

# In[34]:


plt.figure(figsize=(10, 5))
plt.plot(x,y)


# In[35]:


plt.figure(figsize=(5, 10))
plt.plot(x, y)


# In[40]:


plt.figure(figsize=(10, 5), dpi=50) # dots per inch 확대
plt.plot(x, y)


# ## 배경색

# In[41]:


plt.figure(facecolor='yellow')
plt.plot(x, y)


# In[46]:


plt.figure(facecolor='#a1c3ff')
plt.plot(x, y)

