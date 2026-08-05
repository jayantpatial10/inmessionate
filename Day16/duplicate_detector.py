import pandas as pd

def file_loader():
    try :
        print('Enter the path to the file :')
        file_path = input()
        leads = pd.read_csv(file_path)
        #print(leads)
        return leads
    except Exception as e:
        print('File Loading Failed')
        return 

     
def basic_stats(df1):
    if df1 is not None :
        print('\n Dataset Overview : \n')
        print('\nTotal Records = ', len(df1))
        print('\nUnique Records = ', df1['LeadID'].nunique())
        print('\nDuplicate Records = ',df1.duplicated().sum())
        print('\n -------------------------------- \n')
    else :
        print('No records to show stats')

def show_duplicates(df1):
    if df1 is not None : 
        duplicates = df1[df1.duplicated()]  
        print('Duplicate Records Sample :\n')
        print(duplicates.head())  
        print('\n -------------------------------- \n')  

        duplicate_counts = df1['LeadID'].value_counts()
        #print(duplicate_counts)

        for x, y in duplicate_counts[duplicate_counts>1].items() :
            print(f' LeadID {x} -> {y} times')

        print('\n -------------------------------- \n')   

        print('Possible Causes for duplicates\n')

        for x, y in duplicate_counts[duplicate_counts>1].items() :
            if (y ==2) :
                print('Source Duplication\n')
            elif (y>2):
                print('Join Multiplication\n')    
            else :
                print('Dupliates need in depth analysis')

    else : 
        print('No data to show duplicates')

        

def main():
    df1 = file_loader()
    basic_stats(df1)
    show_duplicates(df1)


if __name__ == '__main__':
    main()    