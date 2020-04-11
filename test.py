import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('Dataset/SalaryData.csv')

# Checking Dataset
print(dataset)
print(type(dataset.columns[0]))
print("***************************")

y = dataset['Salary']
x = dataset['YearsExperience']

X = x.values.reshape(len(x), 1)

# Visualizing Data Here
plt.scatter(X, y, c=X)
plt.ylabel('Salary')
plt.xlabel('Years of Experience')
plt.show()

# Training model here
model = LinearRegression()
model.fit(X, y)

# Predicting Salary
coeffiecient = model.coef_
intercept = model.intercept_

print(f"Maximum Salary : {(coeffiecient * 1.1)[0] + intercept}")
