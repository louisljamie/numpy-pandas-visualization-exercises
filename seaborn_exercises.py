# Use seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from env import get_db_url as url

# use iris database to answer the following questions:

iris_df = sns.load_dataset("iris")
iris_df.head()

# What does the distribution of petal lengths look like?

sns.histplot(data=iris_df, x="petal_length", kde=True)

# Is there a correlation between petal length and petal width?,

sns.relplot(data=iris_df, x="petal_length", y="petal_width")


# visualize two numeric columns through the lense of a categorical column.

sns.relplot(data=iris_df, x="petal_length", y="petal_width", hue="species")



#  Compare species based on sepal width and sepal length?

sns.pairplot(data=iris_df, x="petal_length", y="petal_width", hue="species")


# Compare features would be best used to predict species?

sns.pairplot(iris_df, hue="species")

# Use seaborn's load_dataset function to load the anscombe data set.

anscombe_df = sns.load_dataset("anscombe")

# Use pandas to group the data by the dataset column, and
# calculate summary statistics for each dataset. What do you notice?

anscombe_df.groupby("dataset").describe()

# Plot the x and y values from the anscombe data. Each dataset should be in a separate column.

sns.relplot(data=anscombe_df, x="x", y="y", col="dataset")

# Load the InsectSprays dataset and read it's documentation. Create a boxplot that shows the ' \
# effectiveness of the different insect sprays.

insect_sprays = data("InsectSprays")
insect_sprays = data("InsectSprays",show_doc=True)

# Create a boxplot that shows the effectiveness of the different insect sprays.

sns.boxplot(data=insect_sprays, x="spray", y="count")

# Load the swiss dataset and read it's documentation. The swiss dataset is available from pydatset

swiss_df = data("swiss")
swiss_df = data("swiss", show_doc=True)

# Create an attribute named is_catholic that holds a boolean value of whether or not the province is
# Catholic. (Choose a cutoff point for what constitutes catholic)

swiss = data("swiss",show_doc=True)
swiss = data("swiss")
swiss.columns

swiss.head(1) #checking columns

# Create an attribute named is_catholic; a boolean value of whether or not the province is Catholic.

swiss["is_catholic"] = swiss["Catholic"] > 50
swiss.head(1)

# Create a chart that shows whether or not a province is Catholic influence fertility?

sns.relplot(data=swiss, x="Catholic", y="Fertility", hue="is_catholic")

# Create a chart that measures what correlates most strongly with fertility?

sns.pairplot(swiss, hue="is_catholic")


# Use the chipotle dataset from the previous exercise. Create a bar chart that shows the 4 most popular
# items and the revenue produced by each.

sns.barplot(data=chipotle_df, x="item_name", y="item_price")

# Load the sleepstudy data and read it's documentation.

# Load the sleepstudy data and read it's documentation.
# Use seaborn to create a line chart of all the individual subject's reaction times
# and a more prominant line showing the average change in reaction time.

sleepstudy = data("sleepstudy")

#fix subject data type

def change_to_string(integer):
    word = str(integer)
    word_list = []
    for d in word:
        word_list.append(d)
        word_list.append("-")
    word = "".join(word_list)
    return word

change_to_string(308)

sleepstudy["Subject"] = sleepstudy["Subject"].apply(change_to_string)
sleepstudy.dtypes
sleepstudy.head(1)

#plot
sns.lineplot(x="Days", y="Reaction",hue="Subject",data=sleepstudy)
plt.hlines(sleepstudy["Reaction"].mean(), 0, 9, ls=':')

sns.pairplot(sleepstudy, hue="Subject")