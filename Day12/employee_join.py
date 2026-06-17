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

def filter_salary(df):
    filter_df = df[df['Salary'] > 50000]
    print(filter_df)

def main():
    df1,df2 = file_loader()
    df = table_merge(df1,df2)
    filter_salary(df)

main()  


     