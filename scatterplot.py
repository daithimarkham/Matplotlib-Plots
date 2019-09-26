# David Markham 
# 26/09/2019
# Looking at extra plots which you could use such as a scatter plot. 
# Values are scattered using colors around the graph.
# Can use 3/4 dimensional data
# X, Y axis, colour of dot and size of the dot.

import matplotlib.pyplot as plt
import numpy as np 



data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('Category a')
plt.ylabel('Category b')
plt.show() 