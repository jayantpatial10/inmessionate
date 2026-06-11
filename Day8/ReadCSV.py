import pandas as pd

df = pd.read_csv(r'C:\Users\jayan\Music\DEJourney\Month1\PythonBasics\Day8\employees.csv')
print(df)

print(df.head())

high_salary = df[df['Salary'] > 50000]
print(high_salary)