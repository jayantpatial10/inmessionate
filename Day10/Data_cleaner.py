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



def clean_data(df):
    if df is not None:
        df_cleaned = df.drop_duplicates()
        df_cleaned['Salary'] = df_cleaned['Salary'].fillna(0)
        df_cleaned['Department'] = df_cleaned['Department'].fillna('Unknown')
        return df_cleaned
    else:
        print("No data to clean.")
        return None
    
def save_cleaned_data(df_cleaned):
    if df_cleaned is not None:
        print('Enter the file path to save the cleaned data:')
        save_path = input()
        try:
            df_cleaned.to_csv(save_path, index=False)
            print(f"Cleaned data saved successfully to {save_path}")
        except Exception as e:
            print(f"Error saving file: {e}")
    else:
        print("No cleaned data to save.")   

def display_data_info(df):
    if df is not None:
        print('Data Information:')
        print('Original records:', len(df))
        print('Missing Records fixed :\n', df['Salary'].isnull().sum())
        print('Missing Departments fixed:\n', df['Department'].isnull().sum())
        print('Duplicate Records fixed:\n', df.duplicated().sum())
        print('Cleaned records:', len(df.drop_duplicates()))
    else:
        print("No data to display information.")        

def main():
    df = file_loader()
    display_data_info(df)
    df_cleaned = clean_data(df)
    save_cleaned_data(df_cleaned)

if __name__ == "__main__":
    main()             
