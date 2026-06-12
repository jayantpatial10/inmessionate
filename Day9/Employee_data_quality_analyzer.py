import pandas as pd

def file_loader():
    
    print('Enter the file path to load the data:')
    file_path = input()
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading file: {e}")
        return None
    
def missing_value_report(df):
    
    if df is not None:
        print(df.isnull())
        print(df.isnull().sum())
        
    else :
        print("No data to analyze for missing values.")

def duplicate_report(df):
    
    if df is not None:
        print(df.duplicated())
        print(df.duplicated().sum())
    else :
        print("No data to analyze for duplicates.")

def display_bad_records(df):
    if df is not None:
        print('Missing salary values:\n', df[df['Salary'].isnull()])
        print('Duplicate records:\n', df[df.duplicated()])
        print('Missing department values:\n', df[df['Department'].isnull()])
    else :
        print("No data to analyze for bad records.")


def summary_report():  
    df = file_loader()
    if df is not None:
        print('Total records:', len(df))
        print('Missing values report:')
        missing_value_report(df)
        print('Duplicate records report:')
        duplicate_report(df)
        display_bad_records(df)
    else :
        print("No data to analyze for summary report.")  

def main():
    summary_report()
main()                        