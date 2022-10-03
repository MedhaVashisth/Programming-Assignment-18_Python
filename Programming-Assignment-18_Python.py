#!/usr/bin/env python
# coding: utf-8

# In[3]:


def larger_string(str, n):
   result = ""
   for i in range(n):
      result = result + str
   return result

print(larger_string('abc', 2))
print(larger_string('.py', 3))


# In[4]:


def string_reverse(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse('1234abcd'))


# In[5]:


# Factorial of a number using recursion

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 7

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))


# In[6]:


# Factorial of a number using recursion

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 7

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))


# In[8]:


# Python3 code to demonstrate
# moving element to end
# using append() + pop() + index()

# initializing list
test_list = ['3', '5', '7', '9', '11']

# printing original list
print ("The original list is : " + str(test_list))

# using append() + pop() + index()
# moving element to end
test_list.append(test_list.pop(test_list.index(5)))

# printing result
print ("The modified element moved list is : " + str(test_list))


# In[9]:


test_list = ['3', '5', '7', '9', '11']


# In[10]:


print ("The original list is : " + str(test_list))


# In[12]:


test_list.append(test_list.pop(test_list.index('5')))


# In[13]:


print ("The modified element moved list is : " + str(test_list))


# In[ ]:




