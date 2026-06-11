import pandas as pd

def accept_file_path():
    print("Enter the file path of the CSV file:")
    file_path = input()
    return file_path

def read_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
        return None
    
def display_stats(df):
    print('Max Salary:', df['Salary'].max())
    print('Min Salary:', df['Salary'].min())
    print('Average Salary:', df['Salary'].mean())   
    print('Total Salary taken by all employees:', df['Salary'].sum())   
    
def department_avg_salary(df):
    avg_salary_by_department = df.groupby('Department')['Salary'].mean()
    print("\nAverage Salary by Department:")
    print(avg_salary_by_department)    

file = accept_file_path()
dataframe = read_csv(file)
if dataframe is not None:
    display_stats(dataframe)
    department_avg_salary(dataframe)
else:  print("Unable to read the CSV file. Please check the file path and try again.")    