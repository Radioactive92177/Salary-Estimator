import matplotlib.pyplot as plt
import pandas as pd
import win32com.client as wc
from sklearn.linear_model import LinearRegression

speak = wc.Dispatch("Sapi.SpVoice")
#voice initialized

def showData(X, y, x_name, y_name):
    plt.scatter(X, y, c=X)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.show()


def predictSalary(X, y, x_name):
    model = LinearRegression()
    model.fit(X, y)

    coefficient = model.coef_
    intercept = model.intercept_

    speak.Speak(f"Please provide the the {x_name}")
    exp = float(input(f"Enter {x_name} :"))

    max_salary = (coefficient * exp)[0] + intercept
    max_salary = int(max_salary)

    speak.Speak(f"The maximum salary you should offer is around {max_salary}")

    print(f"* Maximum Salary : {max_salary} *")


print("******************************************************")
print("           Welcome to the Salary Estimator            ")
print("******************************************************")
print("\n")

speak.Speak("Please provide the path to your data-set down below")

dataset = input("Enter path : ")

data = pd.read_csv(dataset)
print("******************************************************")
print(data)
print("******************************************************")

speak.Speak("Enter the field number you want to predict")

print("Which field do you want to predict? ")
print(f"1.{data.columns[0]}")
print(f"2.{data.columns[1]}")

choice = int(input("Enter field no. :"))

if choice == 1:
    y_name = data.columns[0]
    x_name = data.columns[1]
else:
    y_name = data.columns[1]
    x_name = data.columns[0]

x = data[x_name]
y = data[y_name]

X = x.values.reshape(len(x), 1)

speak.Speak("Do you want to see the graph of your data?")
choice_graph = input("Press Y to see Graph and N to ignore and proceed to prediction : ")

choice_graph = choice_graph.lower()

if choice_graph == "y":
    showData(X, y, x_name, y_name)
    predictSalary(X, y, x_name)
else:
    predictSalary(X, y, x_name)
