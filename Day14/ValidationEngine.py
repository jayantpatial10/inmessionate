import pandas as pd

def file_loader():
    try:
        print('Enter actual file path:')
        actual_path = input()
        actual_data = pd.read_csv(actual_path)
        print('Actual data loaded sucessfully')

        print('Enter expected file path:')
        expected_path = input()
        expected_data = pd.read_csv(expected_path)
        print('Expected data loaded sucessfully')

        print('Enter reference file path:')
        reference_path = input()
        reference_data = pd.read_csv(reference_path)
        print('Reference data loaded sucessfully')
        
        return actual_data,expected_data,reference_data
    
    except Exception as e:

        print('File loading failed, please check the paths and try again') 
        return None, None, None   

def merge_expected_actual(df1,df2):
    try:
        if(df1 is not None and df2 is not None):
            validation_df = pd.merge(df1,df2, on = 'Department', how = 'outer' ,suffixes=('_Expected','_Actual')) 
            validation_df['Difference'] = (validation_df['LeadCount_Actual'] - validation_df['LeadCount_Expected'])
            #print(validation_df)
            return validation_df
        else :
            print('Dataframe empty')        
    except Exception as e :
        print('Merging tables failed, please check columns')  

def find_missing_departments(df4):
    #print('Missing Departments : \n')
    missing_departments = df4[df4['LeadCount_Actual'].isnull()]
    #print(missing_departments['Department'])
    return missing_departments

def find_new_departments(df4):
   # print('New Departments : \n')
    new_departments = df4[df4['LeadCount_Expected'].isnull()]
    #print(new_departments['Department'])
    return new_departments

def find_count_mismatch(df4):
    #print('Count Mismatches :\n')
    mismatch_departments = df4[(df4['Difference'] !=0) & (df4['Difference'].notna())]
    #print(mismatch_departments[df4['Department']])
    return mismatch_departments
          
    
def generate_report(df4,df5,df6,df7):
    print('VALIDATION ENGINE REPORT :\n')
    print('\n Departments Checked : ',len(df4))
    print('\n Missing Departments : ',len(df5) )
    print('\n New Departments : ', len(df6))
    print('\n Count mismatches : ', len(df7))
    print('\n ----------------------------------------- \n')
    print('Missing Departments \n',df5['Department'] )
    print('\n ----------------------------------------- \n')
    print('New Departments \n',df6['Department'] )
    print('\n ----------------------------------------- \n')
    print('\n Count Mismatches\n')
    for index,row in df7.iterrows():
        print(row['Department'])
        print('\n Expected : ',row['LeadCount_Expected'])
        print('\n Actual : ', row['LeadCount_Actual'])
        print('\n Difference :',row['Difference'])
        print('\n-------------------------------------------')

def main():
    df1,df2,df3 = file_loader()
    df4 = merge_expected_actual(df1,df2)
    df5 = find_missing_departments(df4)
    df6 = find_new_departments(df4)
    df7 = find_count_mismatch(df4)
    generate_report(df4,df5,df6,df7)



if __name__ == '__main__':
    main()              