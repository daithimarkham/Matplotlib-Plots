# David Markham
# 26/09/2019 
# Side by side plots.

# Import libraries
import matplotlib.pyplot as plt 
import numpy as np 

# Add in titles, legends etc if you wish.
# Create a subplot with one row, two columns and this is subplot command 1.
plt.subplot(1, 2, 1)

# Normal generates random numbers in a bell shaped curve. 
# Typically centered around 0 and spreads out.
x = np.random.normal(0.0, 1.0, 10000) 
plt.hist(x)

# Create Subplot command 2.
plt.subplot(1, 2, 2)
# Uniform generates numbers from -3 and 3, generating 10k of them. 
# In uniform we should expect to see a straight line at the top of the histogram.
x = np.random.uniform(-3.0, 3.0, 10000) 
plt.hist(x)

# Shows the histogram.
plt.show() 