
# Use the following code for the questions below:

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# How many negative numbers are therein np.array?

negative_numbers = 0
for number in a:
    if number < 0:
        negative_numbers += 1

print(negative_numbers)

# How many positive numbers are there?

positive_numbers = 0
for number in a:
    if number > 0:
        positive_numbers += 1
print(positive_numbers)

# How many even positive numbers are there?

even_positive_numbers = 0
for number in a:
    if number > 0 and number % 2 == 0:
        even_positive_numbers += 1
print(even_positive_numbers)


#  add 3 to each data point, how many positive numbers would there be?

a_plus_3 = a + 3
print(a_plus_3)



# squared each number, what would the new mean and standard deviation be?

a_squared = a ** 2
print(a_squared)

# A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0.
# This is done by subtracting the mean from each data point. Center the data set. See this link for more on centering.

a_centered = a - a.mean()
print(a_centered)




# Calculate the z-score for each data point. Recall that the z-score is given by:

z = (x - u) / o
