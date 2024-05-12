# Pands-project

## Iris Dataset

![Image](https://bennycheung.github.io/images/dempster-shafer-theory-for-classification/iris_petal_sepal.jpg)

## About the Project

The Iris dataset is a commonly used dataset to understand classification and clustering algorithms in machine learning and statistics and it was made famous by Ronald Fisher.

It cosists of 150 samples in total, 50 from each of the the 3 species (Iris setosa, Iris virginica, Iris versicolor).
Each sample consists of four features: sepal width, sepal length, petal width and petal length.

These four features are all measured in centimeters:

- Sepal Length: The length of the iris flower’s sepals (the green leaf-like structures that encase the flower bud).
- Sepal Width: The width of the iris flower’s sepals.
- Petal Length: The length of the iris flower’s petals (the colored structures of the flower).
- Petal Width: The width of the iris flower’s petals.

## How to get started.

To further explore this dataset you need to download python, which can be installed through [anaconda](https://www.anaconda.com/download),and notebook editor, which can be found in [Visual Studio Code](https://code.visualstudio.com/)

## Analysis

 Imported Python libraries to anlyse the data.

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
```

- Pandas - for data manipulation and analysis. It allows us to investigate CSV files, amongst other features.

- Matplotlib - for data visualisation and graphical plotting

- Seaborn - built on top of matplotlib with similar functionalities

- Numpy - to perform  wide variety of mathematical operations on arrays

## Loading the CSV data into dataframe

```python
iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
```

## Read in the data
The summary of the Iris data can be found in the  **iris_summary.txt** file

```python
print(iris) # displays the whole dataset
print(iris.head()) # displays the 5 first rows from the dataframe
print(iris.describe()) # diplays stats about the data
print(iris.info()) # displays basic information about datatype
print(iris['species'].value_counts()) # displays number of samples on each class
```

# Plots

## Histograms

![alt text](<Petal length.png>)

![alt text](<Petal width.png>)

## Scatterplots

![alt text](<Petal length vs Petal width plot.png>)

The above plot shows that setosa species have smaller petal widths and lengths.
The versicolor species lie in the middle of both species and the virginica species has the largest petal lengths and widths.



![alt text](<Sepal length vs Sepal width plot.png>)

From the above plot we can see that setosa species has larger sepal widths but smaller sepal lengths.
Virginica species has smaller sepal widths but larger sepal lengths and the versicolor species lies in the middle of both species.



## Pairplot

Pairplot is used for plotting pairwise relationships. It demonstrates the relationship between the variables within the columns. It can be used for multivariate analysis.

![alt text](<Iris dataset pairplot plt.png>)

## Correlation

Correlation heat map demonstrates the correlations between the columns.
It excludes the non numerical values and the missing values.

![alt text](<Correlation Matrix plt.png>)

Petal length and petal width (r= 0.96)
- high positive correlation, meaning the longer the length the wider the width.

Sepal length and sepal width: Weak negative correlation (r = -0,12)
- Weak correlation 

Petal length and sepal length = 0.87
 - have positive good correlations.

Sepal length and Petal width = 0.82
 - have good positive correlations.

Sepal width and petal width =


## Conclusion


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

11. https://www.hackersrealm.net/post/iris-dataset-analysis-using-python

12. https://datagy.io/seaborn-heatmap/

13. https://datagy.io/python-seaborn/

14. https://seaborn.pydata.org/tutorial/distributions.html

