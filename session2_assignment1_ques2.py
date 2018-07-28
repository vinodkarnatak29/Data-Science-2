
# coding: utf-8

# ###### Program to print below pattern using nested for loop.
# 
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# In[17]:


# @column for number of cloumn to print in pattern.
column=5;
 
# first nested loop for first half.
# The end=' ' is just to say that you want a space after the end of the statement instead of a new line character.
for i in range(column):
    for j in range(i):
        print ('*', end=' ')
    print('')

# second nested loop for second half
for i in range(column,0,-1):
    for j in range(i):
        print('*', end=' ')
    print('')

