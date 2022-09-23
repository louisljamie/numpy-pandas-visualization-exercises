
# Use the following code for the questions below:

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# How many negative numbers are therein np.array?

np.a < 0

a.size

neg_num = len(a[a < 0])

negative_numbers = 0
for number in a:
    if number < 0:
        negative_numbers += 1

print(negative_numbers)

# How many positive numbers are there?

np.a > 0

positive_numbers = 0
for number in a:
    if number > 0:
        positive_numbers += 1
print(positive_numbers)

pos_num = len(a[a > 0])

# How many even positive numbers are there?

pos_num = np.a % 2 == 0


even_positive_numbers = 0
for number in a:
    if number > 0 and number % 2 == 0:
        even_positive_numbers += 1
print(even_positive_numbers)


#  add 3 to each data point, how many positive numbers would there be?

len(a[a + 3 > 0])

np.a + 3

a_plus_3 = a + 3
print(a_plus_3)



# squared each number, what would the new mean and standard deviation be?

len(a[a ** 2])

np.a ** 2

a_squared = a ** 2
print(a_squared)

# Numpy A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0.
# This is done by subtracting the mean from each data point. Center the data set. See this link for more on centering.

np.a - np.mean(a)

a_centered = a - a.mean()
print(a_centered)




# Calculate the z-score for each data point using numpy Recall that the z-score is given by:

np.a - np.mean(a) / np.std(a)

z_scores = (np.a - np.mean(a)) / np.std(a)
print(zscores)



z = (x - u) / o

zscores = (a - a.mean()) / a.std()
print(zscores)


from scipy import stats
stats.zscore(a)


# Life w/o numpy to life with numpy

## Setup 1
a8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

np.a8.sum()

sum_of_a8 = sum(a8)

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

np.a8.min()

min_of_a8 = min(a8)

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

np.a8.max()

max_of_a8 = max(a8)

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

np.a8.mean()

mean_of_a8 = sum(a8) / len(a8)

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

np.a8.prod()

product_of_a8 = 1

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

np.a8 ** 2

squares_of_a8 = [number ** 2 for number in a8]

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

np.a8 % 2 == 1

odds_in_a8 = [number for number in a8 if number % 2 == 1]

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

np.a8 % 2 == 0

evens_in_a8 = [number for number in a8 if number % 2 == 0]


## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

## find the sum

np.b.sum()

sum_of_b = sum([sum(row) for row in b])

## find the min

b.min()

min_of_b = min([min(row) for row in b])

## find the max

b.max()



max_of_b = max([max(row) for row in b])

## find the average

b.mean()

mean_of_b = sum([sum(row) for row in b]) / (len(b) * len(b[0]))

## find the product

b.prod()

product_of_b = 1


## find the list of squares

b ** 2

squares_of_b = [number ** 2 for row in b for number in row]


# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable.
# **Hint, you'll first need to make sure that the "b" variable is a numpy array**

sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

b.sum()



# Exercise 2 - refactor the following to use numpy.
min_of_b = min(b[0]) \
    if min(b[0]) <= min(b[1]) \
    else min(b[1])

b.min()

b.min(axis=1)

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) \
    if max(b[0]) >= \
       max(b[1]) \
    else max(b[1])

b.max()

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

b.mean()

# Exercise 5 - refactor the following to use numpy for
# calculating the product of all numbers multiplied together.

product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number


b * np.b

np.b

# Exercise 6 - refactor the following to use numpy to
# find the list of squares
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

b ** 2

# Exercise 7 - refactor using numpy to
# determine the odds_in_b

odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

b % 2 == 1


# Exercise 8 - refactor the following to use numpy to
# filter only the even numbers

evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

b % 2 == 0

# Exercise 9 - print out the shape of the array b.

b.shape

# Exercise 10 - transpose the array b.

b.T

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

b.reshape(1, 6)

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

b.reshape(6, 1)

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.

c.min()

# Exercise 2 - Determine the standard deviation of c.

c.std()

# Exercise 3 - Determine the variance of c.

c.var()

# Exercise 4 - Print out the shape of the array c

c.shape

# Exercise 5 - Transpose c and print out transposed result.

c.T

# Exercise 6 - Get the dot product of the array c with c.

c.dot(np.c)

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

c.dot(np.c.T).sum()

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.

c.dot(np.c.T).prod()


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

# Exercise 1 - Find the sine of all the numbers in d

d.sin()

# Exercise 2 - Find the cosine of all the numbers in d

d.cos()

# Exercise 3 - Find the tangent of all the numbers in d

d.tan()

# Exercise 4 - Find all the negative numbers in d

d < 0

# Exercise 5 - Find all the positive numbers in d

d > 0

# Exercise 6 - Return an array of only the unique numbers in d.

d.unique()

# Exercise 7 - Determine how many unique numbers there are in d.

d.unique().size


# Exercise 8 - Print out the shape of d.

d.shape

# Exercise 9 - Transpose and then print out the shape of d.

d.T
transpose = d.T
transpose.shape


# Exercise 10 - Reshape d into an array of 9 x 2

d.reshape(9, 2)