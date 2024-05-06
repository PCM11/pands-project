# Pands-project

## Iris Dataset

![Image](https://bennycheung.github.io/images/dempster-shafer-theory-for-classification/iris_petal_sepal.jpg)

## About the Project

The Iris dataset is a commonly used dataset to understand classification and clustering algorithms in machine learning and statistics, made famous by Ronald Fisher.

It cosists of 150 samples, 50 from each of the the 3 species (Iris setosa, Iris virginica, Iris versicolor). Each sample consists of four features: sepal width, sepal length, petal width and petal length.

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

## Plots

### Histograms

![alt text](<Petal length.png>)
![alt text](<Petal width.png>)

### Scatterplots

![alt text](<Petal length vs Petal width plot.png>)
![alt text](<Sepal length vs Sepal width plot.png>)

### Pairplot

![alt text](<Iris dataset pairplot plt.png>)


## References

1. https://realpython.com/pandas-python-explore-dataset/
2. https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
3. https://www.pycodemates.com/2022/05/iris-dataset-classification-with-python.html?utm_content=cmp-true
4. https://datagy.io/pandas-exploratory-data-analysis/
5. https://www.hackersrealm.net/post/iris-dataset-analysis-using-python 
6. https://en.wikipedia.org/wiki/Iris_flower_data_set
7. https://www.geeksforgeeks.org/iris-dataset/
8. https://stackoverflow.com/questions/9331281/how-can-i-test-what-my-readme-md-file-will-look-like-before-committing-to-github