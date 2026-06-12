import pandas as pd


df = pd.read_csv(r"C:\Users\jayan\Music\DEJourney\Month1\PythonBasics\Day9\Employees_dirty.csv")

print(df.head())
print(df.info())
print(df.describe())