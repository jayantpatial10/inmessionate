import pandas as pd

df= pd.read_csv(r'C:\Users\jayan\Music\DEJourney\Month1\PythonBasics\Day8\employees.csv')

def filter_by_salary():
    print("Enter the salary threshold:")
    salary_threshold = float(input())
    filtered_df = df[df['Salary'] > salary_threshold]
    sorted_df = filtered_df.sort_values(by = 'Salary', ascending=False)
    return sorted_df


def display_stats():
    print('Max Salary:', df['Salary'].max())
    print('Min Salary:', df['Salary'].min())
    print('Average Salary:', df['Salary'].mean())   
    print('Total Salary taken by all employees:', df['Salary'].sum())

display_stats()
result = filter_by_salary()
print(result)    