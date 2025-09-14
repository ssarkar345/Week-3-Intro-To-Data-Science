# Week-3-Intro-To-Data-Science
## Instructions
For all the questions below, submit a PDF file showing all of your code and any corresponding output. Again, you don't have to use both R and Python, just pick one.

This assignment uses two datasets which are already built in to R and can be accessed directly as just the iris and Plantgrowth dataframes. In order to access them using Python, please see the following code:

from sklearn import datasets
iris = datasets.load_iris()

import pandas as pd
data = { "weight": [4.17, 5.58, 5.18, 6.11, 4.50, 4.61, 5.17, 4.53, 5.33, 5.14, 4.81, 4.17, 4.41, 3.59, 5.87, 3.83, 6.03, 4.89, 4.32, 4.69, 6.31, 5.12, 5.54, 5.50, 5.37, 5.29, 4.92, 6.15, 5.80, 5.26], "group": ["ctrl"] * 10 + ["trt1"] * 10 + ["trt2"] * 10}
PlantGrowth = pd.DataFrame(data)

### 1. Using the iris dataset...

Make a histogram of the variable Sepal.Width.
Based on the histogram from #1a, which would you expect to be higher, the mean or the median? Why?
Confirm your answer to #1b by actually finding these values.
Only 27% of the flowers have a Sepal.Width higher than ________ cm.
Make scatterplots of each pair of the numerical variables in iris (There should be 6 pairs/plots).
Based on #1e, which two variables appear to have the strongest relationship? And which two appear to have the weakest relationship?
### 2. Using the PlantGrowth dataset...

Make a histogram of the variable weight with breakpoints (bin edges) at every 0.3 units, starting at 3.3.
Make boxplots of weight separated by group in a single graph.
Based on the boxplots in #2b, approximately what percentage of the "trt1" weights are below the minimum "trt2" weight?
Find the exact percentage of the "trt1" weights that are below the minimum "trt2" weight.
Only including plants with a weight above 5.5, make a barplot of the variable group. Make the barplot colorful using some color palette (in R, try running ?heat.colors and/or check out https://www.r-bloggers.com/palettes-in-r/).
