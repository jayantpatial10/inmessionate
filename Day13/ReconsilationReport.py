import pandas as pd

def file_loader():
    try :
        print('Enter the path to employee data file : ')
        employee_path = input()
        employee_data = pd.read_csv(employee_path)
        print('Employee Data loaded successfuly')
        print('Enter the path to orders data file : ')
        orders_path = input()
        orders_data = pd.read_csv(orders_path)
        print('Orders data loaded sucessfuly')

        return employee_data,orders_data
    except Exception as e:
        print('Loading files failed')
        return None, None

def merge_data(df1,df2):

    merged_data = pd.merge(df1,df2, on = 'CustomerID', how= 'left' )
    print(merged_data.head())

    print(type(merged_data))
    return merged_data

def find_missing_orders(df):

    count = df[df['OrderAmount'].isnull()]
    print(f'Customers Missing Orders = {len(count)} \n' )
    print('---------------------------------------')

def reconsilation_report(df):
    print('RECONSILATION REPORT')
    print(f'Total Customers = {len(df)} \n')
    print(f'Customers with Orders = {len(df[df['OrderAmount'].notnull()])} \n')
    print(f'Order Coverage = {len(df[df['OrderAmount'].notnull()]) /len(df)}\n')
    find_missing_orders(df)
    print('Missing Customers\n')
    missing_customers = df[df['OrderAmount'].isnull()]
    
    for index,row in missing_customers[['CustomerID','CustomerName']].iterrows() :    
        print(f'Customer ID : {row['CustomerID']} \n')
        print(f'Customer Nmae : {row['CustomerName']} \n')
        print('-------------------------------------')

def main():
    df1,df2 = file_loader()
    df = merge_data(df1,df2)
    reconsilation_report(df)

if __name__ == '__main__' :
    main()    

    