import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Use pandas to create a Series named fruits from the following list:
# ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
# Use Series attributes and methods to explore your fruits Series.
fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

type(fruits)
fruits.shape
# Pandas to Determine the number of elements in fruits.

fruits.size

# Pandas Output only the index from fruits.

fruits.index

list(fruits.index)


# Pandas Output only the values from fruits.

list(fruits.values)

fruits.values

set(fruits.values)

# Pandas Confirm the data type of the values in fruits.

fruits.dtype

# dtype('O')


# Pandas Output only the first five values from fruits. Output the last three values. Output two random values from fruits.

pd.Series.head?
pd.Series.head(fruits, n=5)
pd.Series.tail?
pd.Series.tail(fruits, n=3)

fruits.head(5)


# Pandas Run the .describe() on fruits to see what information it returns when called on a Series with string values.

fruits.describe()

fruits.sample()
fruits._indexed_same()

# Pandas Run the code necessary to produce only the unique string values from fruits.


fruits.unique()

fruits.nunique()



# Pandas Determine how many times each unique string value occurs in fruits.


fruits.value_counts()


# Pandas Determine the string value that occurs most frequently in fruits.

fruits.value_counts().head(1)


# Pandas Determine the string value that occurs least frequently in fruits.


fruits.value_counts().tail(1)

fruits.value_counts()nsmallest()

fruits.value_counts()nlargest()



# PART 2
# Pandas Capitalize all the string values in fruits.

fruits.str.capitalize()

fruits.str.lower()

fruits.str.upper()


# Pandas Count the letter "a" in all the string values (use string vectorization).


fruits.str.count("a")

    # lamda is a function in a single line with both the execution and return in one line.
fruits.apply(lambda x: x + "count of a: " + str(x.count("a")), axis=1)


# Pandas Output the number of vowels in each and every string value.

vowel_counts = 0
    for i in range(len(fruits.str.lower())):
        if fruits.str.count(fruits.str.lower()[i]) > 0:
            vowel_counts += 1
    print(vowel_counts)

fruits.str.count("a") + fruits.str.count("e") + fruits.str.count("i") + fruits.str.count("o") + fruits.str.count("u")

fruits.str.count("[aeiou]")



# Pandas Write the code to get the longest string value from fruits.


fruits.apply(lambda x: len(x), axis=1)

str.len().max()


# Pandas Write the code to get the string values with 5 or more letters in the name.


fruits.str.len() >= 5

fruits.str.len().max()

fruits_bool_mask = fruits.str.len() == fruits.str.len().max()

fruits[fruits_bool_mask] = False
fruits[fruits_bool_mask] = True
fruits[fruits_bool_mask]


# Pandas Find the fruit(s) containing the letter "o" two or more times.


fruits.str.count("o") >= 2


# Pandas Write the code to get only the string values containing the substring "berry".


fruits.str.contains("berry")

fruits[fruits.apply(lambda x: "berry" in x.split())]


# Pandas Write the code to get only the string values containing the substring "apple".


fruits.str.contains("apple")

apple_bool_mask = fruits.str.contains("apple")


# Pandas Which string value contains the most vowels?

fruits.str.contains("apple")

fruits_bool_mask = fruits.str.contains("apple")


fruits[fruits_bool_mask] = False
count("[aeiou]") == fruits.str.count("[aeiou]").max()

# PART 3

# Pandas series use a list and convert each individual letter into a single string on a basic Python list.


letters = pd.Series(list(letters))


# Pandas Which letter occurs the most frequently in the letters Series?



letters = pd.Series(letters)




# Pandas Which letter occurs the Least frequently?

letters.value_counts().tail(1)

letters.value_counts().nsmallest(n=1, keep='all')


# Pandas How many vowels are in the Series?

letters.str.count("[aeiou]").sum()

def is_vowel()
    return fruits.str.contains("[aeiou]").sum() > 0


# Pandas How many consonants are in the Series?


letters.str.count("[bcdfghjklmnpqrstvwxyz]").sum()

letters.str.lower().apply(is_vowel)

(~letters.str.lower().apply(is_vowel)).sum()



# Pandas Create a Series that has all of the same letters but uppercased.

letters.str.upper()

# Pandas Create a bar plot of the frequencies of the 6 most commonly occuring letters.

letters.value_counts().head(6).plot.bar()

letters.value_counts().head(6).plot(kind='barh')
plt.title('Top 6 Letters')
plt.xlabel('Letter')
plt.show()

#  Pandas create a Series named numbers from the following list:

numbers = pd.Series['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']


#  Pandas What is the data type of the numbers Series?

numbers.dtype


#  Pandas How many elements are in the number Series?

numbers.size



#  Pandas accessing Series attributes and methods to
#  Convert the numbers Series to a numeric data type.

numbers = numbers.str.replace("$", "").str.replace(",", "").astype(float)


#  Pandas Run the code to discover the maximum value from the Series.

numbers.max()

#  Pandas Run the code to discover the minimum value from the Series.

numbers.min()

#  Pandas What is the range of the values in the Series?

numbers.describe()

numbers.max() - numbers.min()

#  Pandas Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.
pd.cut(numbers, 4).value_counts().sort_index()


numbers.value_counts(bins=4)

#  Pandas Plot the binned data in a meaningful way. Be sure to include a title and axis labels



numbers.value_counts(bins=4).plot.bar()

# Pandas create a Series named exam_scores from the following list:


exam_scores = pd.Series[60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]

#  Pandas How many elements are in the exam_scores Series?


exam_scores.size


#  Pandas Run the code to discover the minimum, the maximum, the mean, and the median scores for the exam_scores Series.


exam_scores.min()


#  Pandas Plot the Series in a meaningful way and make sure your chart has a title and axis labels.


exam_scores.plot.hist()


#  Pandas Write the code necessary to implement a curve for your exam_grades Series and save this as curved_gradess

#  Add the necessary points to the highest grade to make it 100, and add the same number of points to every other score in the Series as well.


curved_grades = exam_scores + (100 - exam_scores.max())



#  Pandas Use a method to convert each of the numeric values in the curved_grades Series into a categorical value of letter grades.
#  For example, 86 should be a 'B' and 95 should be an 'A'. Save this as a Series named letter_grades.


letter_grades = pd.cut(curved_grades, bins=[0, 60, 70, 80, 90, 100], labels=["F", "D", "C", "B", "A"])

# make a map from letter grades to numeric grades

letter_grades = letter_grades.map({"F": 0, "D": 1, "C": 2, "B": 3, "A": 4})
if number >= 90:
    return "A"
elif number >= 80:
    return "B"
elif number >= 70:
    return "C"
elif number >= 60:
    return "D"

#  Pandas Plot your new categorical letter_grades Series in a meaninful way and include a title and axis labels.


letter_grades.value_counts().sort_index().plot.bar()



#--------



