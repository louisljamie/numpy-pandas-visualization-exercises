import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests

# requests is a library for making HTTP requests in Python3
#.readfile("data/file_name.csv") is a method of the requests library
# other ways of imorting data: .read_csv(), .read_excel(), .read_sql()

# datframe.columns = ['col1', 'col2', 'col3', 'col4']
# dataframe['col1'] = dataframe['col1'].astype('int64')
# datframe.dtypes # returns the data types of each column
# dataframe.info() # returns the data types of each column and the number of non-null values
# dataframe.describe() # returns the count, mean, std, min, max, and quartiles of each column
# dataframe.size # returns the number of elements in the dataframe
# dataframe.shape # returns the number of rows and columns in the dataframe
# dataframe.head() # returns the first 5 rows of the dataframe
# dataframe.tail() # returns the last 5 rows of the dataframe
# datafram.info() # returns the data types of each column and the number of non-null values
#


# pd.Datframe.to_csv('data/new_file.csv', index=False)
# pd.Datframe.to_excel('data/new_file.xlsx', index=False)
# pd.Datframe.to_sql('data/new_file.sql', index=False)
# pd.DataFrame.to_csv('data/new_file.csv', index=False)
# pd.Datframe.to_sql('data/new_file.sql')



# For several of the following exercises, you'll need to load several datasets using the pydataset library. ' \
# '(If you get an error when trying to run the import below, use pip to ' \
# 'install the pydataset package.)

from pydataset import data

# When the instructions say to load a dataset, you can pass the name of the dataset as a string to the data function
# to load the dataset. You can also view the documentation for the data set by passing the show_doc keyword argument.

dataset = data.load_bank()
data.show_doc('bank')


# data('mpg', show_doc=True) # view the documentation for the dataset

data('mpg', show_doc=True)
mpg = data('mpg') # load the dataset and store it in a variable

# All the datasets loaded from the pydataset library will be pandas dataframes.

# Copy the code from the lesson to create a dataframe full of student grades.

df = pd.DataFrame(np.random.randint(60, 101, size=(10, 3)), columns=['Math', 'Science', 'English'])
df['Math'] = mpg.Math.astype('int')
df['Science'] = mpg.Science.astype('int')
df['English'] = mpg.English.astype('int')


# Create a column named passing_english that indicates whether each student has a passing grade in english.

df['passing_english'] = df.English > 70

# Sort the english grades by the passing_english column. How are duplicates handled?

df.sort_values(by='passing_english')


# Sort the english grades first by passing_english and then by student name. All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to the .sort_values method)

df.sort_values(by=['passing_english', 'English'])

# Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.

df.sort_values(by=['passing_english', 'English'], ascending=[True, False])

# Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades.

df['overall_grade'] = (df.Math + df.Science + df.English) / 3

# Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:

df['mpg'] = pd.read_csv(os.path.join(os.))
df = data('mpg')



# How many rows and columns are there?

df.head()


# What are the data types of each column?

df.dtypes


# Summarize the dataframe with .info and .describe

df.info.describe()


# Rename the cty column to city.

df.rename(columns={0: 'cty'}, inplace=True)


# Rename the hwy column to highway.

df.rename(columns={0: 'hwy'}, inplace=True)


# Do any cars have better city mileage than highway mileage?

df[df.cty > df.hwy]


# Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.

df['mileage_difference'] = df.hwy - df.cty



# Which car (or cars) has the highest mileage difference?

df[df.mileage_difference == df.mileage_difference.max()]


# Which compact class car has the lowest highway mileage? The best?

df[df['class'] == 'compact'].sort_values(by='hwy').head(1)


# Create a column named average_mileage that is the mean of the city and highway mileage.

df['average_mileage'] = (df.cty + df.hwy) / 2

# Which dodge car has the best average mileage? The worst?

df[df.manufacturer == 'dodge'].sort_values(by='average_mileage').head(1)


# Which dodge car has the worst?

df[df.manufacturer == 'dodge'].sort_values(by='average_mileage').tail(1)


# Create a column named average_mileage_difference that is the mean of the city and highway mileage.
# and the city and highway mileage.

df['average_mileage_difference'] = (df.average_mileage - df.average_mileage.mean())

# Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:
# How many rows and columns are there?

df = data('Mammals')


# What are the data types?

df.dtypes


# Summarize the dataframe with .info and .describe

df.info.describe()


# What is the weight and the fastest animal?

df.sort_values(by='speed').tail(1)

df.sort_values(by='speed').tail(1)
df.weight.describe()


# What is the overal percentage of specials?

df.specials.describe()


# How many animals are hoppers that are above the median speed? What percentage is this?

df[(df.hoppers == True) & (df.speed > df.speed.median())].count() / df.count()

# What is the avg average speed of the fastest animal?

df.sort_values(by='speed').tail(1).speed.mean()

