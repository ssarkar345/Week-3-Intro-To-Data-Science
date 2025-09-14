from sklearn import datasets
iris = datasets.load_iris()



import pandas as pd
data = { "weight": [4.17, 5.58, 5.18, 6.11, 4.50, 4.61, 5.17, 4.53, 5.33, 5.14, 4.81, 4.17, 4.41, 3.59, 5.87, 3.83, 6.03, 4.89, 4.32, 4.69, 6.31, 5.12, 5.54, 5.50, 5.37, 5.29, 4.92, 6.15, 5.80, 5.26], "group": ["ctrl"] * 10 + ["trt1"] * 10 + ["trt2"] * 10}
PlantGrowth = pd.DataFrame(data)

# Iris Data Set
# a. Make a histogram of the variable Sepal.Width.
df = pd.DataFrame(data=iris.data, 
                  columns=iris.feature_names)
df.head()

import matplotlib.pyplot as plt

plt.hist(df['sepal width (cm)'])
plt.show()
import seaborn as sns
sns.histplot(df['sepal width (cm)'],kde=True)
plt.show()

# b. Based on the histogram from #1a, which would you expect to be higher, the mean or the median? Why?

print("I expect the mean to be higher because there appears to be a very slight right skew")

# c. Confirm your answer to #1b by actually finding these values.

sepal= df["sepal width (cm)"]

import numpy as np
np.mean(sepal)
np.median(sepal)

# d. Only 27% of the flowers have a Sepal.Width higher than ________ cm.

np.percentile(sepal,[73])

# Only 27% of the flowers have a Sepal.Width higher than 3.3 cm.

# e. Make scatterplots of each pair of the numerical variables in iris (There should be 6 pairs/plots).
sns.pairplot(df)
plt.show()

# f. Based on #1e, which two variables appear to have the strongest relationship? And which two appear to have the weakest relationship?
# Petal Length and Petal Width seem to have a strong positive correlation.
# Sepal Length and Sepal Width Seem to have no correlation at all

# PlantGrowth DataSet

#Histogram
PlantGrowth.head()

weight=PlantGrowth['weight']
bins = np.arange(3.3, weight.max() + 0.3, 0.3)
sns.histplot(data=PlantGrowth, x='weight', bins=bins)
plt.show()

#Boxplot

sns.boxplot(x='group', y='weight', data=PlantGrowth)
plt.show()

# Almost all the Trt1 weights are below the TRT2 Minimum

T2 = PlantGrowth[PlantGrowth['group'] == "trt2"]
T2.head()
T2['weight'].min()

# min trt2 is 4.92

T1=PlantGrowth[PlantGrowth['group'] == "trt1"]
T1['weight'].max()

np.percentile(T1['weight'],[79])

# about 78 to 79% of the weights in the trt1 group are below the minimum trt 2 weight.


# Only including plants with a weight above 5.5, make a barplot of the variable group. Make the barplot colorful using some color palette
filtered = PlantGrowth[PlantGrowth['weight'] > 5.5]
groupcounts = filtered['group'].value_counts().reset_index()
groupcounts.columns = ['group', 'count']
sns.barplot(x='group', y='count', data=groupcounts, palette='viridis')
plt.show()