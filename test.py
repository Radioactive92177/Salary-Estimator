import pandas as pd
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('Dataset/SalaryData.csv')

# Checking Dataset
print(dataset)
print("***************************")

y = dataset['Salary']

x = dataset['YearsExperience']

X = x.values.reshape(30,1)

print(X)