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
        
        return actual_data,expected_data
    
    except Exception as e:

        print('File loading failed, please check the paths and try again') 
        return None, None, None   
    
def file_merge(df1,df2):
    merged = pd.merge(df1,df2, on = 'LeadID', how = 'left',indicator=True) 
    #print(merged)
    extra_rows = merged[merged['_merge'] == 'left_only']
    #print(extra_rows)

    return merged, extra_rows


def generate_report(df1,df2,df3,df4):
    print('ROOT CAUSE REPORT \n')
    print('\nExpected Rows : ', len(df3))
    print('\nActual Rows : ', len(df3) - len(df4))
    difference = len(df2) - len(df1)
    print(f'\nDifference : {difference}')
    print('\n--------------------------------------------\n')
    if difference < 0:
        print('Extra rows found \n')
        for LeadID in df4['LeadID']:
            print('LeadID : ',LeadID)
    elif difference > 0 :
        print('Rows Missing')   
    else :
        print('No Mismatch')    

    print('\n Possible Causes\n')    

    if difference < 0 :
        print('Missing Filter')
    elif difference > 0 & difference < 10 :
        print('Duplicate Join')  
    else :
        print('Incorrect Mapping')      



    




def  main():
    df1,df2 = file_loader()
    df3,df4 = file_merge(df1,df2)
    generate_report(df1,df2,df3,df4)

if __name__ == '__main__' :
    main()