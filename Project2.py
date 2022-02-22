#!/usr/bin/env python
# coding: utf-8

# # Numpy
# 
# 

# #### 1. Import the numpy package under the name `np` (★☆☆) 
# (**hint**: import … as …)

# In[8]:


import numpy as np
a = np.array([2,3,4,5])
a


# #### 2. Print the numpy version and the configuration (★☆☆) 
# (**hint**: np.\_\_version\_\_, np.show\_config)

# In[12]:


print(np._version)
print(np.show_config)


# #### 3. Create a null vector of size 10 (★☆☆) 
# (**hint**: np.zeros)

# In[13]:


a = np.zeros(10)
print(a)


# #### 4.  How to find the memory size of any array (★☆☆) 
# (**hint**: size, itemsize)

# In[5]:


import numpy as np
arr = np.array([[1,3,5,7],[2,4,6,8]])
N = arr.itemsize
print(np.size(arr))
print(N)


# #### 5.  How to get the documentation of the numpy add function from the command line? (★☆☆) 
# (**hint**: np.info)

# In[6]:


import numpy as np
print(np.info(np.add))


# #### 6.  Create a null vector of size 10 but the fifth value which is 1 (★☆☆) 
# (**hint**: array\[4\])

# In[7]:


a = np.zeros(10)
a[4] = 1
print(a)


# #### 7.  Create a vector with values ranging from 10 to 49 (★☆☆) 
# (**hint**: np.arange)

# In[16]:



  print( np.arange(10,49))


# #### 8.  Reverse a vector (first element becomes last) (★☆☆) 
# (**hint**: array\[::-1\])

# In[18]:


arr = np.arange(5)
print(arr)
print(arr[::-1])


# #### 9.  Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆) 
# (**hint**: reshape)

# In[21]:


import numpy as np
x = np.arange(0,9).reshape(3,3)
print(x)


# #### 10. Find indices of non-zero elements from \[1,2,0,0,4,0\] (★☆☆) 
# (**hint**: np.nonzero)

# In[22]:


x = [1,2,0,0,4,0]
print(np.nonzero(x))


# #### 11. Create a 3x3 identity matrix (★☆☆) 
# (**hint**: np.eye)

# In[23]:


import numpy as np
x = np.eye(3)
print(x)


# #### 12. Create a 3x3x3 array with random values (★☆☆) 
# (**hint**: np.random.random)

# In[24]:


import numpy as np
x = np.random.random((3,3,3))
print(x)


# #### 13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆) 
# (**hint**: min, max)

# In[29]:


import numpy as np
x = np.random.random((10,10))
max_value = np.max(x)
print(max_value)
min_value = np.min(x)
print(min_value)


# #### 14. Create a random vector of size 30 and find the mean value (★☆☆) 
# (**hint**: mean)

# In[34]:


import numpy as np
x = np.random.rand(30)
print(x)
print("the mean value of x is",np.mean(x))


# #### 15. Create a 2d array with 1 on the border and 0 inside (★☆☆) 
# (**hint**: array\[1:-1, 1:-1\])

# In[39]:


import numpy as np
array = np.ones((5,5))
array[1:-1,1:-1] = 0

print(array)


# #### 16. How to add a border (filled with 0's) around an existing array? (★☆☆) 
# (**hint**: np.pad)

# In[ ]:


import mumpy as np
array = np.ones((3,3))


# #### 17. What is the result of the following expression? (★☆☆) 
# (**hint**: NaN = not a number, inf = infinity)

# ```python
# 0 * np.nan
# np.nan == np.nan
# np.inf > np.nan
# np.nan - np.nan
# 0.3 == 3 * 0.1
# ```

# In[109]:


print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(np.nan in set([np.nan]))
print(0.3 == 3 * 0.1)


# #### 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆) 
# (**hint**: np.diag)

# In[110]:


M = np.diag(1+np.arange(4),k=-1)
print(M)


# #### 19. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆) 
# (**hint**: array\[::2\])

# In[3]:


import numpy as np
x = np.ones((3,3))
x = np.zeros((8,8),dtype=int)
x[1::2,::2] = 1
x[::2,1::2] = 1
print(x)


# #### 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element? 
# (**hint**: np.unravel_index)

# In[108]:


import numpy as np
print(np.unravel_index(99,(6,7,8)))


# #### 21. Create a checkerboard 8x8 matrix using the tile function (★☆☆) 
# (**hint**: np.tile)

# In[106]:


import numpy as np 
D = np.tile( np.array([[0,1],[1,0]]), (4,4))
print(D)


# #### 22. Normalize a 5x5 random matrix (★☆☆) 
# (**hint**: (x - min) / (max - min))

# In[9]:


import numpy as np
x= np.random.random((5,5))
x = (x - xmin)/(xmax - xmin)
xmax, xmin = x.max(), x.min()
print(x)


# #### 23. Create a custom dtype that describes a color as four unsigned bytes (RGBA) (★☆☆) 
# (**hint**: np.dtype)

# In[ ]:





# #### 24. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆) 
# (**hint**: np.dot | @)

# In[10]:


import numpy as np
x = np.random.random((5,3))
print(x)
y = np.random.random((3,2))
print(y)
z = np.dot(x, y)
print(z)


# #### 25. Given a 1D array, negate all elements which are between 3 and 8, in place. (★☆☆) 
# (**hint**: >, <=)

# In[11]:


import numpy as np
x = np.arange(11)
x[(3 < x) & (x < 8)] *= -1
print(x)


# #### 26. What is the output of the following script? (★☆☆) 
# (**hint**: np.sum)

# ```python
# # Author: Jake VanderPlas
# 
# print(sum(range(5),-1))
# from numpy import *
# print(sum(range(5),-1))
# ```

# In[40]:


from numpy import *
print(sum(range(5),-1))


# #### 27. Consider an integer vector Z, which of these expressions are legal? (★☆☆)

# ```python
# Z**Z
# 2 << Z >> 2
# Z <- Z
# 1j*Z
# Z/1/1
# Z<Z>Z
# ```

# In[105]:


Z**Z
2 << Z >> 2
Z <- Z
1j*Z
Z/1/1
Z<Z>Z


# #### 28. What are the result of the following expressions?

# ```python
# np.array(0) / np.array(0)
# np.array(0) // np.array(0)
# np.array([np.nan]).astype(int).astype(float)
# ```

# In[26]:


import numpy as np
print(np.array(0) / np.array(0))
print(np.array(0) // np.array(0))
print(np.array([np.nan]).astype(int).astype(float))


# #### 29. How to round away from zero a float array ? (★☆☆) 
# (**hint**: np.uniform, np.copysign, np.ceil, np.abs)

# In[27]:


import numpy as np
C = np.random.uniform(-10,+10,10)
print(np.copysign(np.ceil(np.abs(C)), C))
print(np.where(C>0, np.ceil(C), np.floor(C)))


# #### 30. How to find common values between two arrays? (★☆☆) 
# (**hint**: np.intersect1d)

# In[28]:


import numpy as np
A = np.random.randint(0,10,10)
B = np.random.randint(0,10,10)
print(np.intersect1d(A,B))


# #### 31. How to ignore all numpy warnings (not recommended)? (★☆☆) 
# (**hint**: np.seterr, np.errstate)

# In[ ]:





# #### 32. Is the following expressions true? (★☆☆) 
# (**hint**: imaginary number)

# ```python
# np.sqrt(-1) == np.emath.sqrt(-1)
# ```

# In[41]:


import numpy as np
np.sqrt(-1) == np.emath.sqrt(-1)


# #### 33. How to get the dates of yesterday, today and tomorrow? (★☆☆) 
# (**hint**: np.datetime64, np.timedelta64)

# In[23]:


import numpy as np
yesterday = np.datetime64('today') - np.timedelta64(1)
today     = np.datetime64('today')
tomorrow  = np.datetime64('today') + np.timedelta64(1)


# #### 34. How to get all the dates corresponding to the month of July 2016? (★★☆) 
# (**hint**: np.arange(dtype=datetime64\['D'\]))

# In[15]:


import numpy as np
b = np.arange('2016-07', '2016-08', dtype='datetime64[D]')
print(b)


# #### 35. How to compute ((A+B)\*(-A/2)) in place (without copy)? (★★☆) 
# (**hint**: np.add(out=), np.negative(out=), np.multiply(out=), np.divide(out=))

# In[24]:


import numpy as np
A = np.ones(3)*1
B = np.ones(3)*2
np.add(A,B,out=B)
np.divide(A,2,out=A)
np.negative(A,out=A)
np.multiply(A,B,out=A)


# #### 36. Extract the integer part of a random array using 5 different methods (★★☆) 
# (**hint**: %, np.floor, np.ceil, astype, np.trunc)

# In[25]:


import numpy as np
a = np.random.uniform(0,10,10)

print(a - a%1)
print(a // 1)
print(np.floor(a))
print(a.astype(int))
print(np.trunc(a))


# #### 37. Create a 5x5 matrix with row values ranging from 0 to 4 (★★☆) 
# (**hint**: np.arange)

# In[44]:


import numpy as np
x = np.zeros((5,5))
x+= np.arange(5)
print(x)


# #### 38. Consider a generator function that generates 10 integers and use it to build an array (★☆☆) 
# (**hint**: np.fromiter)

# In[ ]:





# #### 39. Create a vector of size 10 with values ranging from 0 to 1, both excluded (★★☆) 
# (**hint**: np.linspace)

# In[31]:


import numpy as np
x = np.linspace(0,1,11,endpoint=False)[1:]
print(x)


# #### 40. Create a random vector of size 10 and sort it (★★☆) 
# (**hint**: sort)

# In[30]:


import numpy as np
x = np.random.random(10)
x.sort()
print(x)


# #### 41. How to sum a small array faster than np.sum? (★★☆) 
# (**hint**: np.add.reduce)

# In[32]:


import numpy as np
n = np.arange(10)
np.add.reduce(n)


# #### 42. Consider two random array A and B, check if they are equal (★★☆) 
# (**hint**: np.allclose, np.array\_equal)

# In[33]:


import numpy as np
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.allclose(A,B)
print(equal)


# #### 43. Make an array immutable (read-only) (★★☆) 
# (**hint**: flags.writeable)

# In[37]:


import numpy as np
A = np.zeros(10)
A.flags.writeable = False
A[0] = 1


# #### 44. Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates (★★☆) 
# (**hint**: np.sqrt, np.arctan2)

# In[34]:


import numpy as np
A = np.random.random((10,2))
X,Y = A[:,0], A[:,1]
R = np.sqrt(X**2+Y**2)
T = np.arctan2(Y,X)
print(R)
print(T)


# #### 45. Create random vector of size 10 and replace the maximum value by 0 (★★☆) 
# (**hint**: argmax)

# In[38]:


import numpy as np
A = np.random.random(10)
A[A.argmax()] = 0
print(A)


# #### 46. Create a structured array with `x` and `y` coordinates covering the \[0,1\]x\[0,1\] area (★★☆) 
# (**hint**: np.meshgrid)

# In[39]:


import numpy as np
A = np.zeros((5,5), [('x',float),('y',float)])
A['x'], A['y'] = np.meshgrid(np.linspace(0,1,5),
                             np.linspace(0,1,5))
print(A)


# ####  47. Given two arrays, X and Y, construct the Cauchy matrix C (Cij =1/(xi - yj)) 
# (**hint**: np.subtract.outer)

# In[40]:


import numpy as np

X = np.arange(8)
Y = X + 0.5
C = 1.0 / np.subtract.outer(X, Y)
print(np.linalg.det(C))


# #### 48. Print the minimum and maximum representable value for each numpy scalar type (★★☆) 
# (**hint**: np.iinfo, np.finfo, eps)

# In[41]:


import numpy as np
for dtype in [np.int8, np.int32, np.int64]:
    print(np.iinfo(dtype).min)
    print(np.iinfo(dtype).max)
for dtype in [np.float32, np.float64]:
    print(np.finfo(dtype).min)
    print(np.finfo(dtype).max)
    print(np.finfo(dtype).eps)


# #### 49. How to print all the values of an array? (★★☆) 
# (**hint**: np.set\_printoptions)

# In[43]:


import numpy as np
np.set_printoptions(threshold=float("inf"))
A = np.zeros((5,5))
print(A)


# #### 50. How to find the closest value (to a given scalar) in a vector? (★★☆) 
# (**hint**: argmin)

# In[44]:


import numpy as np
A = np.arange(10)
B = np.random.uniform(0,10)
index = (np.abs(A-B)).argmin()
print(A[index])


# #### 51. Create a structured array representing a position (x,y) and a color (r,g,b) (★★☆) 
# (**hint**: dtype)

# In[45]:


import numpy as np
S = np.zeros(10, [ ('position', [ ('x', float, 1),
                                  ('y', float, 1)]),
                   ('color',    [ ('r', float, 1),
                                  ('g', float, 1),
                                  ('b', float, 1)])])
print(S)


# #### 52. Consider a random vector with shape (100,2) representing coordinates, find point by point distances (★★☆) 
# (**hint**: np.atleast\_2d, T, np.sqrt)

# In[ ]:





# #### 53. How to convert a float (32 bits) array into an integer (32 bits) in place? 
# (**hint**: astype(copy=False))

# In[47]:


import numpy as np
N = (np.random.rand(10)*100).astype(np.float32)
Y = N.view(np.int32)
Y[:] = N
print(Y)


# #### 54. How to read the following file? (★★☆) 
# (**hint**: np.genfromtxt)

# ```
# 1, 2, 3, 4, 5
# 6,  ,  , 7, 8
#  ,  , 9,10,11
# ```

# In[49]:


import numpy as np
from io import StringIO
s = StringIO ('''1, 2, 3, 4, 5
                6,  ,  , 7, 8
                 ,  , 9,10,11
''')
N = np.genfromtxt(s, delimiter=",", dtype=np.int)
print(N)


# #### 55. What is the equivalent of enumerate for numpy arrays? (★★☆) 
# (**hint**: np.ndenumerate, np.ndindex)

# In[51]:


import numpy as np
N = np.arange(9).reshape(3,3)
for index, value in np.ndenumerate(N):
    print(index, value)
for index in np.ndindex(N.shape):
    print(index, N[index])


# #### 56. Generate a generic 2D Gaussian-like array (★★☆) 
# (**hint**: np.meshgrid, np.exp)

# In[52]:


import numpy as np
X, Y = np.meshgrid(np.linspace(-1,1,10), np.linspace(-1,1,10))
D = np.sqrt(X*X+Y*Y)
sigma, mu = 1.0, 0.0
G = np.exp(-( (D-mu)**2 / ( 2.0 * sigma**2 ) ) )
print(G)


# #### 57. How to randomly place p elements in a 2D array? (★★☆) 
# (**hint**: np.put, np.random.choice)

# In[53]:


import numpy as np
n = 10
p = 3
A = np.zeros((n,n))
np.put(A, np.random.choice(range(n*n), p, replace=False),1)
print(A)


# #### 58. Subtract the mean of each row of a matrix (★★☆) 
# (**hint**: mean(axis=,keepdims=))

# In[54]:


import numpy as np
X = np.random.rand(5, 10)
Y = X - X.mean(axis=1, keepdims=True)
Y = X - X.mean(axis=1).reshape(-1, 1)

print(Y)


# #### 59. How to sort an array by the nth column? (★★☆) 
# (**hint**: argsort)

# In[55]:


import numpy as np
S = np.random.randint(0,10,(3,3))
print(S)
print(S[S[:,1].argsort()])


# #### 60. How to tell if a given 2D array has null columns? (★★☆) 
# (**hint**: any, ~)

# In[56]:


import numpy as np
A = np.random.randint(0,3,(3,10))
print((~A.any(axis=0)).any())


# #### 61. Find the nearest value from a given value in an array (★★☆) 
# (**hint**: np.abs, argmin, flat)

# In[57]:


import numpy as np
A = np.random.uniform(0,1,10)
z = 0.5
m = A.flat[np.abs(A - z).argmin()]
print(m)


# #### 62. Considering two arrays with shape (1,3) and (3,1), how to compute their sum using an iterator? (★★☆) 
# (**hint**: np.nditer)

# In[58]:


import numpy as np
A = np.arange(3).reshape(1,3)
B = np.arange(3).reshape(3,1)
it = np.nditer([A,B,None])
for x,y,z in it: z[...] = x + y
print(it.operands[2])


# #### 63. Create an array class that has a name attribute (★★☆) 
# (**hint**: class method)

# In[ ]:





# #### 64. Consider a given vector, how to add 1 to each element indexed by a second vector (be careful with repeated indices)? (★★★) 
# (**hint**: np.bincount | np.add.at)

# In[61]:


import numpy as np
Z = np.ones(10)
I = np.random.randint(0,len(Z),20)
Z += np.bincount(I, minlength=len(Z))
print(Z)


# #### 65. How to accumulate elements of a vector (X) to an array (F) based on an index list (I)? (★★★) 
# (**hint**: np.bincount)

# In[62]:


import numpy as np
X = [1,2,3,4,5,6]
I = [2,4,6,8,12,14]
F = np.bincount(I,X)
print(F)


# #### 66. Considering a (w,h,3) image of (dtype=ubyte), compute the number of unique colors (★★★) 
# (**hint**: np.unique)

# In[70]:


import numpy as np
w, h = 25, 26
I = np.random.randint(0, 2, (h, w, 3)).astype(np.ubyte)
colors = np.unique(I.reshape(-1, 3), axis=0)
n = len(colors)
print(n)


# #### 67. Considering a four dimensions array, how to get sum over the last two axis at once? (★★★) 
# (**hint**: sum(axis=(-2,-1)))

# In[71]:


A = np.random.randint(0,10,(3,4,3,4))

sum = A.sum(axis=(-2,-1))
print(sum)



# #### 68. Considering a one-dimensional vector D, how to compute means of subsets of D using a vector S of same size describing subset  indices? (★★★) 
# (**hint**: np.bincount)

# In[72]:


import numpy as np
D = np.random.uniform(0,1,100)
S = np.random.randint(0,10,100)
D_sums = np.bincount(S, weights=D)
D_counts = np.bincount(S)
D_means = D_sums / D_counts
print(D_means)


# #### 69. How to get the diagonal of a dot product? (★★★) 
# (**hint**: np.diag)

# In[73]:


import numpy as np
A = np.random.uniform(0,1,(5,5))
B = np.random.uniform(0,1,(5,5))
np.diag(np.dot(A, B))


# #### 70. Consider the vector \[1, 2, 3, 4, 5\], how to build a new vector with 3 consecutive zeros interleaved between each value? (★★★) 
# (**hint**: array\[::4\])

# In[74]:


import numpy as np
A = np.array([1,2,3,4,5])
nz = 3
A0 = np.zeros(len(A) + (len(A)-1)*(nz))
A0[::nz+1] = A
print(A0)


# #### 71. Consider an array of dimension (5,5,3), how to mulitply it by an array with dimensions (5,5)? (★★★) 
# (**hint**: array\[:, :, None\])

# In[75]:


import numpy as np
A = np.ones((5,5,3))
B = 2*np.ones((5,5))
print(A * B[:,:,None])


# #### 72. How to swap two rows of an array? (★★★) 
# (**hint**: array\[\[\]\] = array\[\[\]\])

# In[76]:


import numpy as np
A = np.arange(25).reshape(5,5)
A[[0,1]] = A[[1,0]]
print(A)


# #### 73. Consider a set of 10 triplets describing 10 triangles (with shared vertices), find the set of unique line segments composing all the  triangles (★★★) 
# (**hint**: repeat, np.roll, np.sort, view, np.unique)

# In[77]:


import numpy as np
faces = np.random.randint(0,100,(10,3))
F = np.roll(faces.repeat(2,axis=1),-1,axis=1)
F = F.reshape(len(F)*3,2)
F = np.sort(F,axis=1)
G = F.view( dtype=[('p0',F.dtype),('p1',F.dtype)] )
G = np.unique(G)
print(G)


# #### 74. Given an array C that is a bincount, how to produce an array A such that np.bincount(A) == C? (★★★) 
# (**hint**: np.repeat)

# In[78]:


import numpy as np
C = np.bincount([1,1,2,3,4,4,6])
A = np.repeat(np.arange(len(C)), C)
print(A)


# #### 75. How to compute averages using a sliding window over an array? (★★★) 
# (**hint**: np.cumsum)

# In[79]:


import numpy as np
def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n
Z = np.arange(20)
print(moving_average(Z, n=3))
from numpy.lib.stride_tricks import sliding_window_view
A = np.arange(20)
print(sliding_window_view(Z, window_shape=3).mean(axis=-1))


# #### 76. Consider a one-dimensional array Z, build a two-dimensional array whose first row is (Z\[0\],Z\[1\],Z\[2\]) and each subsequent row is  shifted by 1 (last row should be (Z\[-3\],Z\[-2\],Z\[-1\]) (★★★) 
# (**hint**: from numpy.lib import stride_tricks)

# In[81]:


import numpy as np
from numpy.lib import stride_tricks
def rolling(a, window):
    shape = (a.size - window + 1, window)
    strides = (a.strides[0], a.strides[0])
    return stride_tricks.as_strided(a, shape=shape, strides=strides)
A = rolling(np.arange(10), 3)
print(A)
A = np.arange(10)
print(sliding_window_view(A, window_shape=3))


# #### 77. How to negate a boolean, or to change the sign of a float inplace? (★★★) 
# (**hint**: np.logical_not, np.negative)

# In[82]:


import numpy as np
S  = np.random.randint(0,2,100)
np.logical_not(S, out=S)

S = np.random.uniform(-1.0,1.0,100)
np.negative(S, out=S)


# #### 78. Consider 2 sets of points P0,P1 describing lines (2d) and a point p, how to compute distance from p to each line i  (P0\[i\],P1\[i\])? (★★★)

# In[92]:


def distance(P0, P1, p):
    T = P1 - P0
    L = (T**2).sum(axis=1)
    U = -((P0[:,0]-p[...,0])*T[:,0] + (P0[:,1]-p[...,1])*T[:,1]) / L
    U = U.reshape(len(U),1)
    D = P0 + U*T - p
    return np.sqrt((D**2).sum(axis=1))

P0 = np.random.uniform(-10,10,(10,2))
P1 = np.random.uniform(-10,10,(10,2))
p  = np.random.uniform(-10,10,( 1,2))
print(distance(P0, P1, p))


# #### 79. Consider 2 sets of points P0,P1 describing lines (2d) and a set of points P, how to compute distance from each point j (P\[j\]) to each line i (P0\[i\],P1\[i\])? (★★★)

# In[93]:


P0 = np.random.uniform(-10, 10, (10,2))
P1 = np.random.uniform(-10,10,(10,2))
p = np.random.uniform(-10, 10, (10,2))
print(np.array([distance(P0,P1,p_i) for p_i in p]))


# #### 80. Consider an arbitrary array, write a function that extract a subpart with a fixed shape and centered on a given element (pad with a `fill` value when necessary) (★★★) 
# (**hint**: minimum, maximum)

# In[ ]:





# #### 81. Consider an array Z = \[1,2,3,4,5,6,7,8,9,10,11,12,13,14\], how to generate an array R = \[\[1,2,3,4\], \[2,3,4,5\], \[3,4,5,6\], ..., \[11,12,13,14\]\]? (★★★) 
# (**hint**: stride\_tricks.as\_strided)

# In[94]:


import numpy as np
S = np.arange(1,15,dtype=np.uint32)
R = stride_tricks.as_strided(S,(11,4),(4,4))
print(R)


# #### 82. Compute a matrix rank (★★★) 
# (**hint**: np.linalg.svd) (suggestion: np.linalg.svd)

# In[98]:


import numpy as np
N = np.random.uniform(0,1,(10,10))
U, S, V = np.linalg.svd(N) 
rank = np.sum(S > 1e-10)
print(rank)


# #### 83. How to find the most frequent value in an array? 
# (**hint**: np.bincount, argmax)

# In[97]:


import numpy as np
A = np.random.randint(0,10,20)
print(np.bincount(A).argmax())


# #### 84. Extract all the contiguous 3x3 blocks from a random 10x10 matrix (★★★) 
# (**hint**: stride\_tricks.as\_strided)

# In[96]:


import numpy as np
A = np.random.randint(0,5,(10,10))
n = 3
i = 1 + (A.shape[0]-3)
j = 1 + (A.shape[1]-3)
C = stride_tricks.as_strided(A, shape=(i, j, n, n), strides=A.strides + A.strides)
print(C)


# #### 85. Create a 2D array subclass such that Z\[i,j\] == Z\[j,i\] (★★★) 
# (**hint**: class method)

# In[ ]:





# #### 86. Consider a set of p matrices wich shape (n,n) and a set of p vectors with shape (n,1). How to compute the sum of of the p matrix products at once? (result has shape (n,1)) (★★★) 
# (**hint**: np.tensordot)

# In[99]:


p, n = 10, 20
M = np.ones((p,n,n))
V = np.ones((p,n,1))
S = np.tensordot(M, V, axes=[[0, 2], [0, 1]])
print(S)


# #### 87. Consider a 16x16 array, how to get the block-sum (block size is 4x4)? (★★★) 
# (**hint**: np.add.reduceat)

# In[100]:


import numpy as np
N = np.ones((16,16))
k = 4
S = np.add.reduceat(np.add.reduceat(N, np.arange(0, N.shape[0], k), axis=0),
                                       np.arange(0, N.shape[1], k), axis=1)
print(S)


# #### 88. How to implement the Game of Life using numpy arrays? (★★★)

# In[ ]:





# #### 89. How to get the n largest values of an array (★★★) 
# (**hint**: np.argsort | np.argpartition)

# In[101]:


import numpy as np
Z = np.arange(10000)
np.random.shuffle(Z)
n = 5
print (Z[np.argsort(Z)[-n:]])
print (Z[np.argpartition(-Z,n)[:n]])


# #### 90. Given an arbitrary number of vectors, build the cartesian product (every combinations of every item) (★★★) 
# (**hint**: np.indices)

# In[ ]:





# #### 91. How to create a record array from a regular array? (★★★) 
# (**hint**: np.core.records.fromarrays)

# In[91]:


import numpy as np
A = np.array([("Hello", 2.5, 3),
              ("World", 3.6, 2)])
R = np.core.records.fromarrays(A.T,
                               names='col1, col2, col3',
                               formats = 'S8, f8, i8')
print(R)


# #### 92. Consider a large vector Z, compute Z to the power of 3 using 3 different methods (★★★) 
# (**hint**: np.power, \*, np.einsum)

# In[89]:


import numpy as np
x = np.random.rand(int(5e7))
get_ipython().run_line_magic('timeit', 'np.power(x,3)')
get_ipython().run_line_magic('timeit', 'x*x*x')
get_ipython().run_line_magic('timeit', "np.einsum('i,i,i->i',x,x,x)")


# #### 93. Consider two arrays A and B of shape (8,3) and (2,2). How to find rows of A that contain elements of each row of B regardless of the order of the elements in B? (★★★) 
# (**hint**: np.where)

# In[ ]:





# #### 94. Considering a 10x3 matrix, extract rows with unequal values (e.g. \[2,2,3\]) (★★★)

# In[103]:


import numpy as np
D= np.random.randint(0,5,(10,3))
print(D)


# #### 95. Convert a vector of ints into a matrix binary representation (★★★) 
# (**hint**: np.unpackbits)

# In[102]:


import numpy as np
I = np.array([0, 1, 2, 3, 15, 16, 32, 64, 128], dtype=np.uint8)
print(np.unpackbits(I[:, np.newaxis], axis=1))


# #### 96. Given a two dimensional array, how to extract unique rows? (★★★) 
# (**hint**: np.ascontiguousarray)

# In[ ]:





# #### 97. Considering 2 vectors A & B, write the einsum equivalent of inner, outer, sum, and mul function (★★★) 
# (**hint**: np.einsum)

# In[86]:


import numpy as np
A = np.random.uniform(0,1,10)
B = np.random.uniform(0,1,10)

np.einsum('i->', A)       
np.einsum('i,i->i', A, B) 
np.einsum('i,i', A, B)    
np.einsum('i,j->ij', A, B)   


# #### 98. Considering a path described by two vectors (X,Y), how to sample it using equidistant samples (★★★)? 
# (**hint**: np.cumsum, np.interp)

# In[ ]:





# #### 99. Given an integer n and a 2D array X, select from X the rows which can be interpreted as draws from a multinomial distribution with n degrees, i.e., the rows which only contain integers and which sum to n. (★★★) 
# (**hint**: np.logical\_and.reduce, np.mod)

# In[84]:


import numpy as np
X = np.asarray([[1.0, 0.0, 3.0, 8.0],
                [2.0, 0.0, 1.0, 1.0],
                [1.5, 2.5, 1.0, 0.0]])
n = 4
M = np.logical_and.reduce(np.mod(X, 1) == 0, axis=-1)
M &= (X.sum(axis=-1) == n)
print(X[M])


# #### 100. Compute bootstrapped 95% confidence intervals for the mean of a 1D array X (i.e., resample the elements of an array with replacement N times, compute the mean of each sample, and then compute percentiles over the means). (★★★) 
# (**hint**: np.percentile)

# In[83]:


X = np.random.randn(100) 
N = 1000 
idx = np.random.randint(0, X.size, (N, X.size))
means = X[idx].mean(axis=1)
confint = np.percentile(means, [2.5, 97.5])
print(confint)


# In[ ]:




