# Pands-project

## Table of Contents

[1. Iris Dataset](#iris-dataset)

[2. About the Project](#about-the-project)

[3. How to get started](#how-to-get-started)

[4. Analysis](#analysis)

[5. Loading Data](#loading-data)

[6. Data Display](#data-display)

[7. Plots](#plots)

- [7.1 Histograms](#histograms)

- [7.2 Scatterplots](#scatterplots)

- [7.3 Pairplot](#pairplot)

[8. Correlation](#correlation)

[9. Conclusion](#conclusion)

[10. References](#references)

## IRIS Dataset

This dataset is available for more exploration on [Github](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv) and [UCI machine Learning Repository](https://archive.ics.uci.edu/dataset/53/iris)

![Image](https://bennycheung.github.io/images/dempster-shafer-theory-for-classification/iris_petal_sepal.jpg)

## About the Project

This project is about Iris dataset, also known as Fisher's Iris dataset. It is a commonly used dataset to understand classification and clustering algorithms in machine learning and statistics.
The data was collected by Dr. Edgar Anderson and made famous by a biologist and statistitian Ronald Fisher. 

It consists of 150 samples of iris flowers, 50 from each of the 3 species:

- Iris setosa
- Iris virginica
- Iris versicolor

Each sample contains four features that are measured in centimeters:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

## How to get started.

To  explore this dataset you need to download python, which can be installed through [anaconda](https://www.anaconda.com/download), and a notebook editor such as Jupiter notebooks, which can be found in [Visual Studio Code](https://code.visualstudio.com/).

## Analysis

 Imported Python libraries to anlyse the data.

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import warnings
import sys
warnings.filterwarnings("ignore")
```

- Pandas - for data manipulation and analysis. It allows us to investigate CSV files, amongst other features.

- Matplotlib - for data visualisation and graphical plotting.

- Seaborn - complements matplotlib and offers a simpler way to plot charts.

- Numpy - to perform  wide variety of mathematical operations on arrays.

- Sys - provides various functions and variables that are used to manipulate Python runtime environment. We use stdout module to send the codes' output onto the 'summary text file'.

- Warnings (filterwarnings("ignore")) - Warning package to ignore warnings ( gives clean result).

## Loading Data

 **pd.read_csv** reads in the dataset and store it as a Dataframe object in the variable **iris**.

```python

iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

```

## Data Display

The summary of the Iris data can be found in the  **summary.txt** file

```python

# To display the whole dataset
print(iris) 

# To look at the first 5 rows of the dataframe
print(iris.head()) 

# To display all the columns and their data types.
print(iris.info()) 

# To show some basic descriptive statistics for all numeric columns
print(iris.describe())

# To show the number of samples per class.
print(iris['species'].value_counts())

# For data cleaning, check for some missing values
print(iris.isnull().sum())

# For correlation we only need numerical values, so we drop the 'species' column
iris = iris.drop(["species"], axis = 1)

#To round up the values to two digits for easy reading.
 print(iris.corr().round (2))

```

# Plots

## Histograms

Histograms are visualisation tools that represent the distribution of variables by counting the number of observation that fall within discrete bins.




We use *histplot()* function to plot histograms for Petal length and width, and sepal length and width.

```python

# Petal length histogram
sns.histplot(x = "petal_length", data = iris, hue="species", multiple="stack")

# Petal width histogram
sns.histplot(x = "petal_width", data = iris, hue="species", multiple="stack")

#Sepal length histogram
sns.histplot(x = "sepal_length", data = iris, hue="species", multiple="stack")

# Sepal width histogram
sns.histplot(x = "sepal_width", data = iris, hue="species", multiple="stack")

```

![alt text](<Petal length.png>)

![alt text](<Petal width.png>)

![alt text](<Sepal length.png>)

![alt text](<Sepal width.png>)

## Scatterplots

Scatterplots demonstrate the linear relationship between all four variables.

```python
#Petal length vs Sepal length plot
sns.scatterplot(x = "sepal_length", y = "petal_length", data = iris, hue = "species")

#Petal width vs Sepal width plot
sns.scatterplot(x = "sepal_width", y = "petal_width", data = iris, hue = "species")

#Petal length vs Petal width plot
sns.scatterplot(x = "petal_width", y = "petal_length", data = iris, hue = ("species"))

# Sepal length vs Sepal width plot
sns.scatterplot(x = "sepal_width", y = "sepal_length", data = iris, hue = "species")

```

![alt text](<Petal length vs Sepal length plot.png>)

The setosas have shorter petal and sepal lengths,
versicolors remain in the middle of both species while virginica has the longest petal and sepal lengths.

_________________________________________________

![alt text](<Petal width vs Sepal width plot.png>)

The setosas have wider sepal widtgs but narrower petal widths.
The versicolors lie in the middle with average bothe sepal width and petal width, while the virginica has the largest petal widths and average to large sepal widths.

_________________________________________________

![alt text](<Petal length vs Petal width plot.png>)

The setosa species have smaller petal widths and lengths.
The versicolor species lie in the middle of both species and the virginica species has the largest petal lengths and widths.

_________________________________________________

![alt text](<Sepal length vs Sepal width plot.png>)

The setosa species has larger sepal widths but shorter sepal lengths.
Virginica species has smaller sepal widths but larger sepal lengths and the versicolor species lies in the middle of both species.

_________________________________________________

## Pairplot

Pairplot is used for plotting pairwise relationships between the variables within the columns. It can be used for multivariate analysis.

```python
# Pairplot
sns.pairplot(iris, hue = "species", diag_kind="hist")

```

![alt text](<Iris dataset pairplot plt.png>)

## Correlation

Correlation analysis shows the linear relationship between numerical features. These relationships help with feature selection and predictive modelling.

```python

# We can only use numerical values to calculate correlation efficient.

iris = iris.drop(["species"], axis = 1) # We first drop the species column.
iris.corr().round (2) # round up the values to two digits for easy reading

# Let's plot the correlation matrix map.
matrix = iris.corr()
sns.heatmap(matrix, annot=True, cmap='coolwarm', fmt=".2f")

```

![alt text](<Correlation Matrix plt.png>)

**Sepal length** has a strong positive correlation with the **Petal length** and **Petal width**, suggesting that longer sepals are associated with wider and longer petals.

**Sepal width** shows a poor negative correlation with all other features (sepal length, petal length and petal width), suggesting the wider or longer they are, the narrower the sepal width is.

**Petal length** and **Petal width** have a very strong correlation, indicating that longer petals are generally also wider.


## Conclusion

When looking at all the graphical demonstrations, setosas seem to be easily distinguishable because of their small features.
The features of virginica and versicolor have more or less same dimensions making it harder to
distinguish from each other.


## References

1. https://realpython.com/pandas-python-explore-dataset/

2. https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/

3. https://www.pycodemates.com/2022/05/iris-dataset-classification-with-python.html?utm_content=cmp-true

4. https://datagy.io/pandas-exploratory-data-analysis/

5. https://www.hackersrealm.net/post/iris-dataset-analysis-using-python 

6. https://en.wikipedia.org/wiki/Iris_flower_data_set

7. https://www.geeksforgeeks.org/iris-dataset/

8. https://stackoverflow.com/questions/9331281/how-can-i-test-what-my-readme-md-file-will-look-like-before-committing-to-github

9. https://stackabuse.com/seaborn-scatter-plot-tutorial-and-examples/

10. https://seaborn.pydata.org/generated/seaborn.scatterplot.html

11. https://stackoverflow.com/questions/11948245/markdown-to-create-pages-and-table-of-contents

12. https://datagy.io/seaborn-heatmap/

13. https://datagy.io/python-seaborn/

14. https://seaborn.pydata.org/tutorial/distributions.html

15. https://matplotlib.org/stable/users/explain/colors/colormaps.html

16. https://www.askpython.com/python/python-stdin-stdout-stderr

17. https://seaborn.pydata.org/generated/seaborn.histplot.html

18. https://www.markdownguide.org/basic-syntax/
