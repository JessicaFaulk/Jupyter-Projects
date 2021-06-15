#!/usr/bin/env python
# coding: utf-8

# In[77]:


# import all required libraries
import numpy as np
import plotly
import plotly.graph_objects as go

#should have the same number of colors named as the links (the length of the values list) and in that order
color_link = ['lightcoral', 'red', 'lemonchiffon', 'palegreen', 'yellow', 'lightskyblue', 'thistle', 'violet', 'lightpink']

#color node follows the order of your labels
color_node = ['pink', 'blue', 'green', 'green', 'orange', 'yellow', 'brown', 'orange'] 



#Basic example of a sankey diagram from Geeks for Geeks
fig = go.Figure(data=[go.Sankey(
    node = dict(
        thickness = 20,
        pad = 100,
        line = dict(color = 'black', width = 0.5),
        label = ["Intake", "Holding", "Experiment 1", "Experiment 2", "Drop1", "Pass", "Out-Process", "Drop2"],
        color = color_node
    ),
    link = dict(
          
      # indices correspond to labels
      source = [0,0,1,1,2,2,3,3,5], 
      target = [1,2,3,4,3,5,6,7,6],
      value =  [2,3,1,1,2,1,2,1,1],
        color = color_link
  ))])
  
fig.show()


# In[ ]:





# In[ ]:




