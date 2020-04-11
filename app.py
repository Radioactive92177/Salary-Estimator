import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import win32com.client as wc

speak = wc.Dispatch("Sapi.SpVoice")

print("******************************************************")
print("           Welcome to the Salary Estimator            ")
print("******************************************************")
print("\n")

speak.Speak("Please provide the path to your data-set dow below")

dataset = input("Enter path : ")

data = pd.read_csv(dataset)
print("******************************************************")
print(data)
print("******************************************************")

speak.Speak("Please provide the Independant and the dependant field name down below")

x_name = input("Enter IV name : ")
y_name = input("Enter DV name : ")

x = data[x_name]
y = data[y_name]

X = x.values.reshape(len(x),1)

plt.scatter(X, y, c=X)
plt.xlabel(x_name)
plt.ylabel(y_name)
plt.show()

model = LinearRegression()
model.fit(X,y)

coeffiecient = model.coef_
intercept = model.intercept_

speak.Speak(f"Please provide the the {x_name}")
exp = float(input(f"Enter {x_name} :"))

max_salary = (coeffiecient*exp)[0]+intercept
max_salary = int(max_salary)

speak.Speak(f"The maximum salary you should offer is around {max_salary}")

print(f"* Maximum Salary : {max_salary} *")










