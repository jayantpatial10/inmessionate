import pandas as pd

def file_loader():
    
    print('Enter the expected data file path:')
    expected_data = input()
    print('Enter the actual data file path:')
    actual_data = input()
    try:
        df1 = pd.read_csv(expected_data)
        df2 = pd.read_csv(actual_data)
        return df1, df2
    except Exception as e:
        print(f"Error loading file: {e}")
        return None, None
    
def validate_data(df1, df2):

    if df1 is not None and df2 is not None and df1.columns.equals(df2.columns):
        print("Validation Report:")
        
        expected = df1.groupby('Department')['LeadCount'].sum()
        actual = df2.groupby('Department')['LeadCount'].sum()
        validated_df = pd.DataFrame({'Expected': expected, 'Actual' : actual})
        validated_df['Difference'] = (validated_df['Actual'] - validated_df['Expected'])
        
        for Department, row in validated_df.iterrows():
           if row['Difference'] != 0:
                print(f'Department : {Department}\n')
                print(f'Expected Value : {row['Expected']}\n')
                print(f'Actual Value : {row['Actual']}\n')
            
           
                print(f"Difference: {row['Difference']:+}\n")

                print("--------------------------------\n")
        
    else:
        print("Validation Report: Columns do not match.")


df1, df2 = file_loader()   
validate_data(df1,df2)     