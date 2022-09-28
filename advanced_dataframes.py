# I

# Run python -m pip install pymysql from your terminal to install the mysql client (any folder is fine)
# cd into your exercises folder for this module and run echo env.py >> .gitignore

# Create a function named get_db_url. It should accept a
# username, hostname, password, and database name and
# return a url connection string formatted like in the
# example at the start of this lesson.

import pymysql
import pandas as pd
import numpy as np
def get_db_url (username, hostname, password, database):
    return "mysql://{0}:{1}@{2}/{3}".format(username, hostname, password, database)

def get_db_codeup (username = 'mirzakhani',
                   hostname = '',
                   password =
                   database= input('Please enter the name of the database you want to connect to: ')):
    return "mysql://{0}:{1}@{2}/{3}".format(username, hostname, password, database)
get_db_codeup()

# Use your function to obtain a connection to the employees database.

sql = '''
SELECT *
FROM employees
LIMIT 10
'''
df = pd.read_sql(sql, get_db_url('employees'))
df.head()

#Once you have successfully run a query:
# a. Intentionally make a typo in the database url. What kind of error message do you see?
sql_e = 'SELECT * FROM employees'
sql_t = 'SELECT * FROM titles'


#b. Intentionally make an error in your SQL query. What does the error message look like?
df_e = pd.read_sql(sql_e, get_db_url('employees'))


# Read the employees and titles tables into two separate DataFrames.

df_t = pd.read_sql(sql_t, get_db_url('employees'))

# How many rows and columns do you have in each DataFrame? Is that what you expected?

df_t.head()

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

# Copy the users and roles DataFrames from the examples above.
# establish users
users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users

# establish roles

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles

# What is the result of using a right join on the DataFrames

right_join = pd.merge(users, roles,
                      left_on="role_id",
                      right_on='id',
                      how='right',
                      indicator=True)
right_join

#BONUS
left_join = pd.merge(users, roles,
                     left_on="role_id",
                     right_on='id',
                     how='left',
                     indicator=True)
left_join

# What is the result of using an outer join on the DataFrames?

outer_join = pd.merge(users, roles,
                      left_on="role_id",
                      right_on='id',
                      how='outer',
                      indicator=True)
outer_join

# What happens if you drop the foreign keys from the DataFrames and try to merge them?

pd.merge(users, roles,
         how='outer',
         indicator=True)

# Load the mpg dataset from PyDataset.

from pydataset import data
mpg = data('mpg')
mpg.head()

# Output and read the documentation for the mpg dataset.


from pydataset import data
mpg = data('mpg')
mpg.head()


# How many rows and columns are in the dataset?

mpg.shape
(234, 11)


# Check out your column names and perform any cleanup you may want on them.

mpg.head()
mpg.columns = ['manufacturer', 'model', 'displacement', 'year', 'cylinders', 'transmission', 'drive', 'city','highway', 'fuel', 'class']
mpg.head()

# Display the summary statistics for the dataset.
mpg.describe()
mpg.info()


# How many different manufacturers are there?

mpg.manufacturer.nunique()
15


# How many different models are there?

mpg.model.nunique()
38

# Create a column named mileage_difference like you did in the DataFrames exercises; this column
# should contain the difference between highway and city mileage for each car.

mpg['mileage_difference'] = mpg.highway - mpg.city
mpg.head()
# Create a column named average_mileage like you did in the DataFrames exercises; this is the mean
# of the city and highway mileage.


mpg['average_mileage'] = round(2 / ((1/mpg.highway) + (1/mpg.city)), 2)
mpg.head()

# Create a new column on the mpg dataset named is_automatic that holds boolean values denoting whether
# the car has an automatic transmission.



mpg.transmission.unique()
array(['auto(l5)', 'manual(m5)', 'manual(m6)', 'auto(av)', 'auto(s6)',
       'auto(l4)', 'auto(l3)', 'auto(l6)', 'auto(s5)', 'auto(s4)'],
      dtype=object)
#data('mpg', show_doc=True)
mpg['is_automatic'] = mpg.transmission.str.contains('auto')
mpg.head()



# Using the mpg dataset, find out which which manufacturer has the best miles per gallon on average?
# Do automatic or manual cars have better miles per gallon?

mpg.groupby('manufacturer').average_mileage.mean().sort_values(ascending = False)
mpg.groupby('manufacturer').average_mileage.mean().nlargest(5)

mpg['transmission_category'] =np.where
(mpg.transmission.str.contains('auto'),'automatic', 'manual')
mpg.head()

mpg.groupby('transmission_category')[['average_mileage']].mean().round(1)

# III

# Use your get_db_url function to help you explore the data from the chipotle database.

qu = 'SELECT * FROM orders'
orders = pd.read_sql(qu, get_db_url('chipotle'))
orders.head(10)


# What is the total price for each order?

orders['item_price'] =
orders.item_price.str.replace('$', '').astype(float)
orders.info()
orders.head()
order_totals = orders.groupby('order_id').item_price.sum()
order_totals.head()

# What are the most popular 3 items?

orders.groupby('item_name').quantity.sum().sort_values(ascending = False).head(3)
orders.head()


# Which item has produced the most revenue?

orders.groupby('item_name').item_price.sum().sort_values(ascending=False).head(1)



# Join the employees and titles DataFrames together.

qu = 'SELECT * FROM employees'
employees = pd.read_sql(qu, get_db_url('employees'))
employees.head(10)
qu2 = 'SELECT * FROM titles'
titles = pd.read_sql(qu2, get_db_url('employees'))
titles.head(10)

all_emp_titles = employees.merge(titles, on='emp_no')
all_emp_titles.head()



# For each title, find the hire date of the employee that was hired most recently with that title.

all_emp_titles.groupby('title').hire_date.max()



# Write the code necessary to create a cross tabulation of the number of titles by department.
# (Hint: this will involve a combination of SQL code to pull the necessary data and python/pandas
# code to perform the 3 manipulations.)

dept_title_query = '''
                    SELECT t.emp_no,
                    t.title,
                    t.from_date,
                    t.to_date,
                    d.dept_name
                    FROM departments AS d
                    JOIN dept_emp AS de USING(dept_no)
                    JOIN titles AS t USING(emp_no);

'''
dept_titles = pd.read_sql(dept_title_query, get_db_url('employees'))
dept_titles.head()
all_titles_crosstab = pd.crosstab(
    dept_titles.dept_name, dept_titles.title)
all_titles_crosstab

current_titles = dept_titles[dept_titles.to_date == dept_titles.to_date.max()]
current_titles.head()
current_titles_crosstab = pd.crosstab(current_titles.dept_name, current_titles.title)
current_titles_crosstab

