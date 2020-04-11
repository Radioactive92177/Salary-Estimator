import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import win32com.client as wc

speak = wc.Dispatch("Sapi.SpVoice")

print("******************************************************")
print("           Welcome to the Salary Estimator            ")
print("******************************************************")
print("\n")

speak.Speak("Please provide the path to your dataset dow below")

dataset = input("Enter path : ")

data = pd.read_csv(dataset)
print("******************************************************")
print(data)
print("******************************************************")







