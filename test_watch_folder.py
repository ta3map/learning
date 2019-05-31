#!/usr/bin/env python
# coding: utf-8

# In[1]:


import watch_folder as wf


# In[ ]:


delay = 60
directory = r'D:\Documents'

print('Hello!')
print('looking for changes at ', directory)
print('with delay: ', delay, ' seconds')

wf.watch_and_say(directory, delay)


# In[ ]:




