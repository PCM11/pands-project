#1. Outputs a summary of each variable to a single text file. 
#2. Saves a histogram of each variable to png files, and 
#4. Perform any other analysis you think is appropriate

# ref: https://realpython.com/pandas-python-explore-dataset/
# ref: https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
# ref: https://www.pycodemates.com/2022/05/iris-dataset-classification-with-python.html?utm_content=cmp-true
# ref: https://datagy.io/pandas-exploratory-data-analysis/
# ref: https://www.hackersrealm.net/post/iris-dataset-analysis-using-python 

# For data manipulation and analysis
import pandas as pd

# For data visualisation and graphical plotting
import matplotlib.pyplot as plt

# For numerical arrays
import numpy as np

# Load the csv data into dataframe
iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

print(iris) # displays the whole dataset
print(iris.head()) # displays the 5 first rows from the dataframe
print(iris.describe()) # diplays stats about the data
print(iris.info()) # displays basic information about datatype
print(iris['species'].value_counts()) # displays number of samples on each class

# Petal Variable
plen = iris['petal_length'] # to get the petal length
plen = plen.to_numpy() # to get the numpy array
print(plen)

pwidth = iris['petal_width']
pwidth =pwidth.to_numpy() # petal width to array
print(pwidth)

# Sepal Variable
slen = iris['sepal_length'] # to get the sepal length
slen = slen.to_numpy() # to get the numpy array
print(slen)

swidth = iris['sepal_width'].to_numpy() # sepal width to array
print(swidth)

#histograms
#iris['petal_length'].hist()
#plt.title('Petal Length')
#plt.show()
#plt.savefig('petal-length.png')

iris['petal_width'].hist()
plt.title('Petal Width')
plt.show()
#plt.savefig('petal-width.png')

iris['sepal_length'].hist()
plt.title('Sepal Length')
plt.show()
#plt.savefig('sepal-length.png')

iris['sepal_width'].hist()
plt.title('Sepal Width')
plt.show()
#plt.savefig('sepal-width.png')

# Petal length vs Petal width plot
# List of colors and class labels
colors = ['red', 'orange', 'blue'] 
species = ['Iris-setosa','Iris-versicolor','Iris-virginica']

for i in range(3): # filter data on each class
    x = iris[iris['species'] == species[i]]

    #Plot the scatter plot
    plt.scatter(x['petal_length'], x['petal_width'], c = colors[i], label = species[i])

#Labels for axes
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.legend()
plt.plot(plen, pwidth, 'o')

plt.title('Petal Width vs Petal Length')
plt.show()

# Sepal length vs Sepal width plot.
for i in range(3): # filter data on each class
    x = iris[iris['species'] == species[i]]

    #Plot the scatter plot
    plt.scatter(x['sepal_length'], x['sepal_width'], c = colors[i], label = species[i])

#Labels for axes
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.legend()
plt.plot(slen, swidth, 'o',)

plt.title('Sepal Width vs Sepal Length')
plt.show()

# Sepal length vs Petal length plot.
for i in range(3): # filter data on each class
    x = iris[iris['species'] == species[i]]

    #Plot the scatter plot
    plt.scatter(x['sepal_length'], x['petal_length'], c = colors[i], label = species[i])

#Labels for axes
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.plot(slen, plen, 'o',)

plt.title('Petal Length vs Sepal Length')
plt.show()

# Petal Width vs Sepal Width plot.
for i in range(3): # filter data on each class
    x = iris[iris['species'] == species[i]]

    #Plot the scatter plot
    plt.scatter(x['sepal_width'], x['petal_width'], c = colors[i], label = species[i])

#Labels for axes
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Petal Width (cm)')
plt.legend()
plt.plot(slen, plen, 'o',)

plt.title('Petal Width vs Sepal Width')
plt.show()
