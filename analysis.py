# Import Python Libraries

# For data manipulation and analysis
import pandas as pd

# For plotting
import matplotlib.pyplot as plt
import seaborn as sns

# For numerical arrays
import numpy as np

# Warning package to ignore warning messages
import warnings
warnings.filterwarnings("ignore")


# Load the csv data into dataframe
iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# Read in data
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

# Histograms

# Petal length histogram
#sns.histplot(x = "petal_length", data = iris, hue="species", multiple="stack")
#plt.title("Petal Length", size=10, color="red")
#plt.savefig("Petal length")

# Petal width histogram
sns.histplot(x = "petal_width", data = iris, hue="species", multiple="stack")
plt.title("Petal Width", size=10, color="red")
plt.savefig("Petal width")

'''
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


# Scatterplots

#Petal length vs Sepal length plot
sns.scatterplot(x = "sepal_length", y = "petal_length", data = iris, hue = "species")                
plt.title(("Petal length vs Sepal length plot"), color = "red") # Title
plt.savefig("Petal length vs Sepal length plot.png") # Save plot as png file

#Petal width vs Sepal width plot
sns.scatterplot(x = "sepal_width", y = "petal_width", data = iris, hue = "species")
plt.title(("Petal width vs Sepal width plot"), color = "red") # Tile
plt.savefig("Petal width vs Sepal width plot.png") # Save plot as png file.

#Petal length vs Petal width plot
sns.scatterplot(x = "petal_width", y = "petal_length", data = iris, hue = ("species"))
plt.title(("Petal length vs Petal width plot"), color = "red") # Title
plt.savefig("Petal length vs Petal width plot.png") # Save plot as png file

# Sepal length vs Sepal width plot
sns.scatterplot(x = "sepal_width", y = "sepal_length", data = iris, hue = "species")
plt.title(("Sepal length vs Sepal width plot"), color = "red") # Title
plt.savefig("Sepal length vs Sepal width plot.png") # Save plot as png file.

# Pairplot
sns.pairplot(iris, hue = "species", diag_kind="hist")
plt.savefig("Iris dataset pairplot plt.png") # Save plot as png file.
'''

#Correlation coefficient to assess the relationship between variables.

iris = iris.drop(["species"], axis = 1) #We must first drop the species column.
iris.corr().round (2) # round up the values to two digits for easy reading

# Let's plot the correlation matrix map.
matrix = iris.corr().round (2)
sns.heatmap(matrix, annot=True, vmax=1, vmin=-1, center=0,cmap='vlag' )
plt.title("Correlation Matrix")
plt.savefig("Correlation Matrix plt.png") # Save plot as png file.
