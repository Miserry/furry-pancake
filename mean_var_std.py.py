#!/usr/bin/env python
# coding: utf-8

# ## freeCodeCamp

# In[1]:


import numpy as np


# In[6]:


def calculate():
    nums = list(input())
    if len(nums) != 9:
        print('List must contain nine numbers.')
        return calculate()
    else:
        x = np.array(nums)
        matrix = x.reshape(3,3)
        matrix = matrix.astype(float)
        output = {}
        mean1 = np.mean(matrix)
        mean2 = np.mean(matrix, axis = 0)
        mean3 = np.mean(matrix, axis = 1)
        var1 = np.var(matrix)
        var2 = np.var(matrix, axis = 0)
        var3 = np.var(matrix, axis = 1)
        std1 = np.std(matrix)
        std2 = np.std(matrix, axis = 0)
        std3 = np.std(matrix, axis = 1)
        max1 = np.max(matrix)
        max2 = np.max(matrix, axis = 0)
        max3 = np.max(matrix, axis = 1)
        min1 = np.min(matrix)
        min2 = np.min(matrix, axis = 0)
        min3 = np.min(matrix, axis = 1)
        sum1 = np.sum(matrix)
        sum2 = np.sum(matrix, axis = 0)
        sum3 = np.sum(matrix, axis = 1)
        output['mean'] = mean2, mean3, mean1
        output['variance'] = var2, var3, var1
        output['standard deviation'] = std2, std3, std1
        output['max'] = max2, max3, max1
        output['min'] = min2, min3, min1 
        output['sum'] = sum2, sum3, sum1
        print(output)
        
calculate()


# In[ ]:





# In[ ]:




