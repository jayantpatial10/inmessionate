def txt_to_list(file_name):
    data_list = []
    with open(file_name, 'r') as file:
     employee_data = file.read() # this will read the entire file as a single string 

    for line in employee_data.splitlines(): 
        name,salary = line.split(',') # split the data into lines and iterate through them
        data_list.append((name, int(salary)))
    return data_list

def report_generator(data_list):
    highest_salary = max(salary for name, salary in data_list)
    lowest_salary = min(salary for name, salary in data_list)
    average_salary = sum(salary for name, salary in data_list) / len(data_list)
    total_salary = sum(salary for name, salary in data_list)
    print(f'Highest Salary: ${highest_salary}')
    print(f'Lowest Salary: ${lowest_salary}')
    print(f'Average Salary: ${average_salary}')
    print(f'Total Salary: ${total_salary}')

print("Welcome to the Employee Report Generator!")
file_name = input('Enter the file name of the employee data (e.g., employees.txt): ')
data_list = txt_to_list(file_name)
report_generator(data_list)
