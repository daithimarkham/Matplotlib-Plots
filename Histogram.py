# David Markham
# 26/09/2019 
# Creating Histograms in Pyplot, one dimensional data. 

# Import libraries
import matplotlib.pyplot as plt 
import numpy as np 

# 1000 x values
x = np.random.normal(0.0, 1.0, 1000) 

# Finds the lowest value of x, -3, then the biggest value of x,
# 3.5, and then chops it into a number of (10) bins/ranges.
# Shows there are 270 ish values in the x variable.
# for eg, in the range .8 to 1.4 there are 130 values.
plt.hist(x)


# Shows the histogram.
plt.show() 
