#!/usr/bin/env python
# coding: utf-8

# # Q.1.Arrays
# 

# In[ ]:


import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
     return(numpy.array(arr[::-1], float))


arr = input().strip().split(' ')
result = arrays(arr)
print(result)


# # Q.2.Shape and Reshape
# 
# 

# In[ ]:


import numpy
print(numpy.array(input().split(), int).reshape(3, 3))


# # Q.3.Transpose and Flatten
# 
# 

# In[ ]:


import numpy

n, m = map(int, input().split())

storage = numpy.array([input().strip().split() for _ in range(n)], int)
print (storage.transpose())
print (storage.flatten())


# # Q.4.Concatenate
# 
# 

# In[ ]:


import numpy
P, N, M = map(int,input().split())
A = numpy.array([input().split() for _ in range(P)],int)
B = numpy.array([input().split() for _ in range(N)],int)
print(numpy.concatenate((A, B), axis = 0))


# # Q.5.Zeros and Ones

# In[ ]:


import numpy
N = tuple(map(int, input().split()))
print(numpy.zeros(N, int))
print(numpy.ones(N, int))


# # Q.6.Eye and Identity

# In[ ]:


import numpy
numpy.set_printoptions(sign=' ')
print(numpy.eye(*map(int, input().split())))


# # Q.7.Array Mathematics
# 
# 

# In[ ]:


import numpy
N, M = map(int, input().split())

A = numpy.array([list(map(int, input().split())) for n in range(N)])
B = numpy.array([list(map(int, input().split())) for n in range(N)])

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)


# # Q.8.Floor, Ceil and Rint

# In[ ]:


import numpy
numpy.set_printoptions(sign=' ')

array = numpy.array(input().split(),float)

print(numpy.floor(array))
print(numpy.ceil(array))
print(numpy.rint(array))


# # Q.9.Sum and Prod

# In[ ]:


import numpy
N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)], int)
print(numpy.prod(numpy.sum(A, axis=0), axis=0))


# # Q.10.Min and Max

# In[ ]:


import numpy
N, M = map(int, input().split())
storage = numpy.array([input().split() for _ in range(N)],int)
print(numpy.max(numpy.min(storage, axis=1), axis=0))


# # Q.11.Mean, Var, and Std

# In[ ]:


import numpy
N,M = map(int, input().split())
l = []

for i in range(N):
    a = list(map(int, input().split()))
    l.append(a)

l = numpy.array(l)

numpy.set_printoptions(legacy='1.13')
print(numpy.mean(l, axis = 1))
print(numpy.var(l, axis = 0))
print(numpy.std(l))


# # Q.12.Dot and Cross

# In[ ]:


import numpy
n = int(input())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)
print(numpy.dot(a, b))


# # Q.13.Inner and Outer

# In[ ]:


import numpy
A = numpy.array(input().split(), int)
B = numpy.array(input().split(), int)
print(numpy.inner(A, B), numpy.outer(A, B), sep='\n')


# # Q.14.Polynomials

# In[ ]:


import numpy
poly = [float(x) for x in input().split()]
x = float(input())

print(numpy.polyval(poly, x))


# # Q.15.Linear Algebra

# In[ ]:


import numpy
N = int(input())
A = numpy.array([input().split() for _ in range(N)], float)
print(round(numpy.linalg.det(A),2))

