# %matplotlib inline
## Uncomment this if this is in jupyter.

import matplotlib.pyplot as plt
import numpy as np
from numpy import random
from sympy import *

# Sympy approximation

X = symbols('X')

f = exp(-(X**2))

Pi_1 = N((integrate(f, (X, -oo, oo)))**2)

# ----

# Numpy approximation
## Credit to Andrew Dotson with his video "How to Estimate Pi Numerically in Python". <https://www.youtube.com/watch?v=JjfrNc-G-zA>

n = input("Input the number of points. n = ") # Number of points
# print('Input your amount of points. n = ')

circlex = []
circley = []

squarex = []
squarey = []

i = 1

# Approximation for pi
while i<=int(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if (x**2 + y**2 <= 1):
        circlex.append(x)
        circley.append(y)
    else: 
        squarex.append(x)
        squarey.append(y)
    i+=1

    
Pi_2 = 4*len(circlex)/float(n)

plt.plot(circlex,circley,'r.')
plt.plot(squarex,squarey,'b.')
plt.grid
plt.title('Approximation for π')
# Plot the approximation

plt.savefig('pi.png')

# ----

print("According to sympy, π is equal to {0}. However, the circle approximated it as {1}".format(Pi_1, Pi_2))
