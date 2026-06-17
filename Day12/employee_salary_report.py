import pandas as pd

def file_loader():
    print('Enter path of employee data file :')
    employee_path = input()
    print('Enter path of employee salary data file :')
    salary_path = input()

    try: 
        employee_data = pd.read_csv(employee_path)
        print('Employee data loaded successfuly')
        salary_data = pd.read_csv(salary_path)
        print('Employee salary data loaded successfuly')
        return employee_data, salary_data   
    except Exception as e :
        print('Unabale to load the file, please check path and try again')
        return None,None
    
def table_merge(df1,df2):
    merged_df = pd.merge(df1,df2, on = 'EmployeeID')

    print(merged_df)

    return merged_df


def generate_report(df):
    print('Employee Salary Report :\n')
    print(f'Total Employees = {len(df)}\n')
    print(f'Highest Salary = {df['Salary'].max()}')
    print(f'Lowest Salary ={df['Salary'].min()}')
    print(f'Average Salary = {df['Salary'].mean()}')
    print('\n------------------------------------------')


def department_salary(df):
    print('\nDepartment wise Average Salary :\n')
    d_sal = df.groupby('Department')['Salary'].mean()
    print(d_sal)

def main():

    df1,df2 = file_loader()
    df = table_merge(df1,df2)
    generate_report(df)
    department_salary(df)


if __name__ == '__main__':
    main()