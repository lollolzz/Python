#!/usr/bin/env python
# coding: utf-8

# ## Jupyter Notebook
# 
# 쥬피터 노트북은 웹 브라우저 상에서 개발을 할 수 있는 도구이며, 코드를 cell 단위로 묶어서 실행하고 그래프나 표, 그리고 이미지나 영상 등을 쉽게 볼 수 있어서 특히 데이터 관련 작업을 할 때 많이 활용됩니다.
# 
# > 교육을 위한 강의 노트로도 아주 훌륭해요!

# ![%E1%84%86%E1%85%A6%E1%84%8B%E1%85%B5%E1%86%AB.png](attachment:%E1%84%86%E1%85%A6%E1%84%8B%E1%85%B5%E1%86%AB.png)

# ## 특징
# 
# 1. 코드를 cell 단위로 작성 및 실행 
# 1. 마크다운을 통한 문서화
# 1. 그래프나 표 등을 실시간으로 확인 
# 1. html.pdf 등 파일로 저장

# ## 사전 학습 자료
# 
# 다음 링크에서 파이썬 기본편에 대한 학습을 하실 수 있습니다.  
# [나도 코딩 블로그](https://nadocoding.tistory.com)

# In[1]:


get_ipython().run_cell_magic('HTML', '', '<iframe width="800" height="400" src="https://www.youtube.com/embed/8dCy_-IvrTs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')


# ## 파이썬 기본 문법

# In[2]:


print("Hello World")


# In[3]:


print("환영합니다")


# In[4]:


name = "연탄이"
print(name)


# In[5]:


print("Ctrl + Enter : 현재 Cell 실행")


# In[6]:


print("Shift + Enter : 현재 Cell 실행 후 다음 Cell 선택")


# In[7]:


print("Alt + Enter : 현재 Cell 실행 후 다음 위치에 Cell 삽입")


# In[8]:


print(1)
print(2)
print(3)


# ## 모듈 사용

# In[9]:


import random
print(random.randint(1, 45))


# In[10]:


# rnadom.randint??


# In[11]:


num = 3


# In[12]:


num *= 2


# In[13]:


num += 4


# In[14]:


print(num)


# In[15]:


# import time
# for i in range(100):
#     print(i)
#     time.sleep(1)


# ---
# 
# ## 시각화 예제 1 : 그래프
# 
# - matplot lib 를 이용하면 다양한 그래프를 그릴 수 있으며 수행 결과를 바로 확인 할 수 있습니다.

# In[16]:


import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3]);  # Plot some data on the axes.


# ## 시각화 예제 2: 테이블
# 
# - pandas는 복잡한 데이터를 분석할 때 아주 유용합니다.

# In[17]:


import pandas as pd
import numpy as np
import matplotlib as mpl

df = pd.DataFrame([[38.0, 2.0, 18.0, 22.0, 21, np.nan],[19, 439, 6, 452, 226,232]],
                  index=pd.Index(['Tumour (Positive)', 'Non-Tumour (Negative)'], name='Actual Label:'),
                  columns=pd.MultiIndex.from_product([['Decision Tree', 'Regression', 'Random'],['Tumour', 'Non-Tumour']], names=['Model:', 'Predicted:']))
df.style

