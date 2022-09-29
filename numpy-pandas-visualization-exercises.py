import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Use matplotlib to plot the following equation:
# y = x^2 - x + 2



# Add an anotation for the point 0, 0, the origin.

plt.annotate('origin', xy=(0, 0), xytext=(0, 0), arrowprops=dict(facecolor='green', shrink=0.05))

# Add labels to the axes and give the plot a title

plt.xlabel('x')
plt.ylabel('y')

# Save the plot as a .png file.

plt.savefig('y = x^2 - x + 2.png')

# ------------------------------------------------------------------------------------------------------------------------------
# Matplotlib: Create and label 4 separate charts for the following equations (choose a range for x that makes sense):
#1 # y = √ x

x = np.array(range(100))
y = np.sqrt(x)

# Create the plot
plt.plot(x,y)
plt.title('y = √ x')
plt.xlabel('x')
plt.ylabel('y')
plt.show()



# y = x**3

x = np.array(range(100))
y = x ** 3

# Create the plot
plt.plot(x,y)
plt.title('y = x**3')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# y = 2^x

x = np.array(range(100))
y = 2**x

# Create the plot
plt.plot(x,y)
plt.title('y = 2^x')
plt.xlabel('x')
plt.ylabel('y')

# y = 1/(x+1)

x = np.array(range(100))
y = 1/(x+1)

# Create the plot
plt.plot(x,y)
plt.title('y = 1/(x+1)')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# Combine the figures you created in the last step into one large figure with
# 4 subplots

x = np.array(range(100))
y1 = x ** 2 - x + 2
y2 = np.sqrt(x)
y3 = x ** 3
y4 = 2**x
y5 = 1/(x+1)

# Create the plot
plt.subplot(2, 2, 1)
plt.plot(x,y1)
plt.title('y = x^2 - x + 2')

plt.subplot(2, 2, 2)
plt.plot(x,y2)
plt.title('y = √ x')

plt.subplot(2, 2, 3)
plt.plot(x,y3)
plt.title('y = x**3')

plt.subplot(2, 2, 4)
plt.plot(x,y4)
plt.title('y = 2^x')

plt.subplot(2, 2, 5)
plt.plot(x,y5)
plt.title('y = 1/(x+1)')

plt.tight_layout()

# Save the plot as a .png

plt.savefig('y = x^2 - x + 2.png')
