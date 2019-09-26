# David Markham
# 26/09/2019
# Matplotlib Tutorial: Python 2D plotting library.

# Import the library
import matplotlib.pyplot as plt

# Everytime we wan to use something from the package
# We have to type the following: 
 
plt.plot([1, 2, 3, 4]) 
plt.ylabel('Some numbers')
plt.show()

# Can put two lists, to plot the x and y axis, as opposed to the one above as follows: 
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# To get rid of the line joining at the points enter:
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'b.') Plots in blue dots.