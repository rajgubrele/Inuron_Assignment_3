#!/usr/bin/env python
# coding: utf-8

# # 1.1 Write a Python Program to implement your own myreduce() function which works exactly like Python's built-in function reduce()#

# In[33]:


# y = [1,2,3,4,5,6,7,8,9]
def sum_two(x):
    a = 0
    for i in x:
        a+=i
    return a
def myreduce(x1,x2):
    A = a
    if x1=="sum_two":
        sum_two(x2)
        
    return A
pp = [1,2,3,4,5,6,7,8]
sum_two(pp)

print(myreduce(sum_two,pp))

    
    


# ##1.2 Write a Python program to implement your own myfilter() function which works exactlylike Python's built-in function filter()#

# In[ ]:


def myfilter()


# #2. Implement List comprehensions to produce the following lists.#
# Write List comprehensions to produce the following Lists#
# 
# #['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]#
# 
# #['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']#
# 
# #['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']#
# 
# #[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
# 
# #[[2, 3, 4, 5], [3, 4, 5, 6],[4, 5, 6, 7], [5, 6, 7, 8]]#
# 
# #[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]##

# In[51]:


a = [i for i in "ACADGILD"]
print(a)

apfa = "xyz"
b = []
for i in apfa:
    for j in range(4):
        b.append(i*(j+1))
print(b)

c = []
for i in range(4):
    for j in apfa:
        c.append(j*(i+1))
print(c)

d = []
for i in range(3):
    for j in range(2,5):
        d.append([j+i])
print(d) 

e = [[],[],[],[]]
for j in range(2,6):
    for i in  range(4):
        e[i].append(j+i)
print(e)

f = []
for i in range(1,4):
    for j in range(1,4):
        f.append((j,i))
print(f)
          

