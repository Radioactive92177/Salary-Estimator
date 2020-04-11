import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


dataset = pd.read_csv('Dataset/SalaryData.csv')

# Checking Dataset
print(dataset)
print("***************************")

y = dataset['Salary']
x = dataset['YearsExperience']

X = x.values.reshape(30,1)

# Visualizing Data Here
plt.scatter(X,y,c=X)
plt.ylabel('Salary')
plt.xlabel('Years of Experience')
plt.show()

# Training model here
model = LinearRegression()
model.fit(X,y)

# Predicting Salary
coeffiecient = model.coef_
intercept = model.intercept_

print(f"Maximum Salary : {(coeffiecient*1.1)[0]+intercept}")
