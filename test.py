import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


dataset = pd.read_csv('Dataset/SalaryData.csv')

# Checking Dataset
print(dataset)
print("***************************")

y = dataset['Salary']

x = dataset['YearsExperience']

X = x.values.reshape(30,1)

#Visualizing Data Here
plt.scatter(X,y,c=X)
plt.ylabel('Salary')
plt.xlabel('Years of Experience')
plt.show()