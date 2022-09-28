# I

# Run python -m pip install pymysql from your terminal to install the mysql client (any folder is fine)
# cd into your exercises folder for this module and run echo env.py >> .gitignore

# Create a function named get_db_url. It should accept a
# username, hostname, password, and database name and
# return a url connection string formatted like in the
# example at the start of this lesson.

import pymysql

def get_db_url (username, hostname, password, database):
    return "mysql://{0}:{1}@{2}/{3}".format(username, hostname, password, database)

def get_db_codeup (username = 'mirzakhani',
                   hostname = '',
                   password =
                   database= input('Please enter the name of the database you want to connect to: ')):
    return "mysql://{0}:{1}@{2}/{3}".format(username, hostname, password, database)
get_db_codeup()

# Use your function to obtain a connection to the employees database.

'

#Once you have successfully run a query:
# a. Intentionally make a typo in the database url. What kind of error message do you see?

#b. Intentionally make an error in your SQL query. What does the error message look like?

# Read the employees and titles tables into two separate DataFrames.

# How many rows and columns do you have in each DataFrame? Is that what you expected?

df_t.shape
(443308, 4)

df_e.shape
(300024, 6)
# Display the summary statistics for each DataFrame.

df_t.info()

# How many unique titles are in the titles DataFrame?

df_e.info()

# What is the oldest date in the to_date column?

df_t.describe()

# What is the most recent date in the to_date column?

df_t.to_date.max()
datetime.date(9999, 1, 1)

# II

# Copy the users and roles DataFrames from the examples above.
# What is the result of using a right join on the DataFrames
# What is the result of using an outer join on the DataFrames?
# What happens if you drop the foreign keys from the DataFrames and try to merge them?
# Load the mpg dataset from PyDataset.
# Output and read the documentation for the mpg dataset.
# How many rows and columns are in the dataset?
# Check out your column names and perform any cleanup you may want on them.
# Display the summary statistics for the dataset.
# How many different manufacturers are there?
# How many different models are there?

# Create a column named mileage_difference like you did in the DataFrames exercises; this column
# should contain the difference between highway and city mileage for each car.


# Create a column named average_mileage like you did in the DataFrames exercises; this is the mean
# of the city and highway mileage.

# Create a new column on the mpg dataset named is_automatic that holds boolean values denoting whether
# the car has an automatic transmission.

# Using the mpg dataset, find out which which manufacturer has the best miles per gallon on average?
# Do automatic or manual cars have better miles per gallon?


# III

# Use your get_db_url function to help you explore the data from the chipotle database.

# What is the total price for each order?

# What are the most popular 3 items?

# Which item has produced the most revenue?

# Join the employees and titles DataFrames together.

# For each title, find the hire date of the employee that was hired most recently with that title.

# Write the code necessary to create a cross tabulation of the number of titles by department.
# (Hint: this will involve a combination of SQL code to pull the necessary data and python/pandas
# code to perform the 3 manipulations.)