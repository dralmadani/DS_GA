#13-Python Tools for Data Science - NumPy and SciPy

import numpy as np 
# Create two arrays with different values.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Add the two vectors together.
z = a + b
print(a)
print(b)

print(' Add the two vectors together.' , type(a))
print (z)

print ( '======== Generating Arrays of Random Numbers With NumPy ========' )

np.random.seed() # if we put (123) it will be the same every time
r = np.random.randint(0, 10)
print(r, type(r))


print ( '======== 1D Arrays ========' )
np.random.seed(123)
r = np.random.randint(0,10, size= (3))
print ('get dimensions = ' , r.shape)
print(r, type(r))

print ( '======== 2D Arrays ========' )
np.random.seed(123)
r = np.random.randint(0,10, size= (3,2))
print ('get dimensions = ' , r.shape)
print(r, type(r))


print ( '======== N-Dimensional Arrays size= (4,2,3)========' )
np.random.seed(123)
r = np.random.randint(0,10, size= (4,2,3))
print ('get dimensions = ' , r.shape)
print(r, type(r))

print ("ex: Here, we can sample 10 elements from a normal distribution with a mean of 0, and a standard deviation of 1. The result is a 1-D array of those values.")

mean = 0
std = 1
series_length = 10
r = np.random.normal(mean, std, series_length)
print ('get dimensions = ' , r.shape)
print(r)
print ( '======== Knowledge Check ========' )

d = np.random.rand(3, 1)
print ('get dimensions = ' , r.shape)
print ("my example =" , d) #( 3 rows and 1 column)

print ( '======== Calculate Basic Statistics on an np.Array ========' )

sample = [1, 1, 1, 2, 3, 4, 5]
print ('mean is : ', np.mean(sample))
print ("median is : ", np.median(sample))

print ( '======== SciPy: Going Beyond NumPy to Calculate Stats on Arrays ======== ')
from scipy import stats
sample = [1, 1, 1, 2, 3, 4, 5]
print ("mode is : " , stats.mode(sample))
print (stats.mode(sample).count[1])
