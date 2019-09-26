# David Markham
# 29/09/2018
# Working with text in Histograms. 

import matplotlib.pyplot as plt 
import numpy as np 

# Use IQ as an example in this program.
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# Display data on Histogram .
n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)

# Can increase the size of text and colour. 
# Below we changed it on the x axis.
t = plt.xlabel('my data', fontsize=14, color='red')


# Label, title and legends. 
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show() 
