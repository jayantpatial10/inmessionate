import pandas as pd 

def file_loader():
    try :
        print('Enter the path to expected data file : ')
        expected_path = input()
        expected_data = pd.read_csv(expected_path)
        print('Expected Data loaded successfuly')
        print('Enter the path to actual data file : ')
        actual_path = input()
        actual_data = pd.read_csv(actual_path)
        print('Actual data loaded sucessfuly')

        return expected_data,actual_data
    except Exception as e:
        print('Loading files failed')
        return None, None
    
def merge_data(df1,df2):

    merged_data = pd.merge(
    df1,
    df2,
    on='EmployeeID',
    how='outer',
    suffixes=('_expected', '_actual'),
    indicator=True
)
    print(merged_data.head())

    return merged_data

def validation_summary(df1,df2,df3):

    print('VALIDATION SUMMARY REPORT') 
    print(f'Total Expected Records = {len(df1)} \n')
    print(f'Total Actual Records = {len(df2)} \n')  
    print(f'Expected Records not in Actual = {len(df1[~df1["EmployeeID"].isin(df2["EmployeeID"])])} \n')
    print(f'Actual Records not in Expected = {len(df2[~df2["EmployeeID"].isin(df1["EmployeeID"])])} \n') 
    salary_mismatch = df3[
    (df3["_merge"] == "both") &
    (df3["Salary_expected"] != df3["Salary_actual"])
]
    print('Salary Mismatch Records =',len(salary_mismatch))


def validation_report(df1,df2,df3):
    validation_df = []

    for index,row in df3.iterrows():
        if row['_merge'] == 'left_only':
            validation_df.append({
                'EmployeeID': row['EmployeeID'],
                'ValidationType': 'Missing in Actual',
                'ExpectedSalary': row['Salary_expected'],
                'ActualSalary': None
            })
        elif row['_merge'] == 'right_only':
            validation_df.append({
                'EmployeeID': row['EmployeeID'],
                'ValidationType': 'Missing in Expected',
                'ExpectedSalary': None,
                'ActualSalary': row['Salary_actual']
            })
        elif row['_merge'] == 'both' and row['Salary_expected'] != row['Salary_actual']:
            validation_df.append({
                'EmployeeID': row['EmployeeID'],
                'ValidationType': 'Salary Mismatch',
                'ExpectedSalary': row['Salary_expected'],
                'ActualSalary': row['Salary_actual']
            })

    return pd.DataFrame(validation_df)

def save_validation_report(df):
    print('Enter the path to save validation report : ')
    save_path = input()
    df.to_csv(save_path, index=False)
    print(f'Validation report saved at {save_path}')


def col_mismatch(df3):
    print(df3.columns)
    columns_to_compare = []

    for col in df3.columns:
        if col.endswith('_expected'):
            actual_col = col.replace('_expected', '_actual')
            if actual_col in df3.columns:
                columns_to_compare.append((col, actual_col))

    for index, row in df3.iterrows():

        if row["_merge"] != "both":
            continue
                
            
    for expected_col, actual_col in columns_to_compare:

        if row[expected_col] != row[actual_col]:

            print(
                f"Mismatch found for EmployeeID {row['EmployeeID']}: "
                f"{expected_col} = {row[expected_col]}, "
                f"{actual_col} = {row[actual_col]}"
            )          

def main():
    df1,df2 = file_loader()
    df3 = merge_data(df1,df2)
    validation_summary(df1,df2,df3)
    df4 = validation_report(df1,df2,df3)
    save_validation_report(df4)
    col_mismatch(df3)

if __name__ == '__main__' :
    main()        