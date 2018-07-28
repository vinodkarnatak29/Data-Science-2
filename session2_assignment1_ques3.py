
# coding: utf-8

# #### Python program to reverse a word after accepting the input from the user.

# In[3]:


# @userInput for user input.
userInput = input("Enter a word to reverse: ")

# loop for reading character of string.
# The end='' is just to say that you want nothing no space after the end of the statement instead of a new line character.
for i in range(len(userInput) - 1, -1, -1):
  print(userInput[i], end="")

