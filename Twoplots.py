# David Markham 
# 26/09/2019
# How to create two plots on one set of axis.

import matplotlib.pyplot as plt 
import numpy as np 

# Create three diff variable, x, y and noise. All are a series of values.
x = np.arange(0.0, 10.0, 0.01)
y = 3.0 * x + 1.0 
noise = np.random.normal(0.0, 1.0, len(x))

# Plot x, y and noise with red dots. 
plt.plot(x, y  + noise, 'r.')
# Plot x and y with blue line.
plt.plot(x, y, 'b-')

plt.show() 
# Can do it in different colours also. 
# By closing down the first window displaying the graph 
# The second coloured graph displays.
plt.plot(x, y  + noise, 'c.')
plt.plot(x, y, 'g-')

plt.show()