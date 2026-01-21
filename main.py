import pandas as pd

data = pd.read_csv("students.csv")

data["Average"] = (data["Maths"] + data["Science"] + data["English"] + data["Computer"]) / 4

highest = data["Average"].max()
lowest = data["Average"].min()

def performance(avg):
    if avg >= 90:
       return "Excellent"
    elif avg >= 75:
       return "Very Good"
    elif avg >= 50:
       return "Good"
    elif avg >= 35:
       return "Average"
    else:
       return "Poor"

data["Performance"] = data["Average"].apply(performance)

print("Student Performance Details:\n")
print(data[["Student_Name","Average","Performance"]])

print("\nSummary:")
print("Highest Average:",highest)
print("Lowest Average:",lowest)
