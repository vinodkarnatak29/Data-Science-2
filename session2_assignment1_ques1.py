
# coding: utf-8

# #### Program which accepts a sequence of comma-separated numbers from console and generate a list.

# In[7]:


# @data variable for user input
# @listValue variable for the values return by split('seprator') method (ie.split breakup a string and add the data to a string array using a defined separator.)
data = input("Enter comma seprated numbers: ")
listValue = data.split(",")
print('List : ',listValue)

