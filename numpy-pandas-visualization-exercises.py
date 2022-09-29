import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Use matplotlib to plot the following equation:
# y = x^2 - x + 2

# Create the vectors X and Y
x = np.array(range(100))
y = x ** 2 - x + 2

# Create the plot
plt.plot(x,y)

plt.title('y = x^2 - x + 2')

# Show the plot
plt.show()




y = x**2 - x + 2
x = range(-100, 100)

plt.plot(x, y, label='y = x^2 - x + 2')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = x^2 - x + 2')
plt.show()




# Add an anotation for the point 0, 0, the origin.



# Add labels to the axes and give the plot a title.
# Save the plot as a .png file.

plt.savefig('y = x^2 - x + 2.png')

# ------------------------------------------------------------------------------------------------------------------------------
# Matplotlib: Create and label 4 separate charts for the following equations (choose a range for x that makes sense):

# y = √ x

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



# Combine the figures you created in the last step into one large figure with
# 4 subplots.



plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.title('4 combinations')
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(2, 2, 2)
plt.plot(x, y)
plt.title('4 combinations')
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(2, 2, 3)
plt.plot(x, y)
plt.title('4 combinations')
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(2, 2, 4)
plt.plot(x, y)
plt.title('4 combinations')
plt.xlabel('x')
plt.ylabel('y')




# Addd different color for the points, include a legend, and an appropriate title for the figure

x = [x * 0.25 for x in range(-25,26)]
pi = math.pi

y1 = [math.sin(x) for x in x]
y2 = [math.cos(x) for x in x]
y3 = [math.sin(x) * -1 for x in x]
y4 = [math.cos(x) * -1 for x in x]

plt.figure(figsize = (8,8))
plt.suptitle('Some Math Functions')

plt.subplot(221)
plt.plot(x, y1,color = 'r', ls = '--')
plt.title('Sine Function')

plt.subplot(222)
plt.plot(x, y2,color = 'r', ls = '--', marker = '^')

plt.subplot(223)
plt.plot(x, y3,color = 'g', ls = '--', marker = 'o')

plt.subplot(224)
plt.plot(x, y4,color = 'm', ls = '--', marker = 'v')
plt.axhline(0, color = 'm')
plt.fill_between(x, y4, color = 'm', alpha= 0.9)

# alpha = controls transperancy

plt.tight_layout()

plt.show()



