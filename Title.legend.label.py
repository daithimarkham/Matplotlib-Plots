# David Markham 
# 26/09/2019
# How to create two plots on one set of axis.

# Import libraries.
import matplotlib.pyplot as plt 
import numpy as np 

# Create three diff variable, x, y and noise. All are a series of values.
x = np.arange(0.0, 10.0, 0.01)
y = 3.0 * x + 1.0 
noise = np.random.normal(0.0, 1.0, len(x))

# Plot x, y and noise with red dots. 
plt.plot(x, y  + noise, 'r.', label="Actual")
# Plot x and y with blue line.
plt.plot(x, y, 'b-', label="Model")


# Commands to display all the data on the graph. 
plt.title("Simple plot") 
plt.xlabel("Height")
plt.ylabel("weight")


# Add a legend if you've made more than one plot on one set of axis 
# And add labels, like in the above with x, y axis. 
plt.legend()


# Shows the whole plot on a graph
plt.show() 