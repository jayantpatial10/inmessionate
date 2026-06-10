import json

def load_employees():
    try:
        print ('Trying to load employees')
        with open('C:\\Users\\jayan\\Music\\DEJourney\\Month1\\PythonBasics\\Day7\\Employees.json','r') as file:
            employee = json.load(file)
            print('Employees loaded successfully.')
            return employee
    except FileNotFoundError:
        print('No existing employee data found. Starting with an empty database.')
        return []

employee = load_employees()
print(employee)

def save_employees():
    with open('C:\\Users\\jayan\\Music\\DEJourney\\Month1\\PythonBasics\\Day7\\Employees.json','w') as file:
        json.dump(employee,file,indent=4)
    print('Employees saved successfully.')

def main_menu():
    while True:
        print('\nEmployee Database Simulator')
        print('1. Add Employee')
        print('2. Search Employee')
        print('3. Display Employees')
        print('4. Remove Employee')
        print('5. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            add_employee()
        elif choice == '2':
            search_employee()
        elif choice == '3':
            display_employees()
        elif choice == '4':
            remove_employee()
        elif choice == '5':
            print('Exiting the program.')
            break
        else:
            print('Invalid choice. Please try again.')

def add_employee():
    print('Enter name of the employee')
    name = input()
    print('Enter department of the employee')
    department = input()
    print('Enter salary of the employee')
    try :
        salary = float(input())
    except ValueError:
        print('Invalid input. Please enter a valid salary.')
        return main_menu()

    employee.append({
        'name': name,
        'department': department,
        'salary': salary
    })
    save_employees()
    

    print('Employee added successfully.')
    return main_menu()

def search_employee():
    print('Enter name of the employee to search')
    name = input()
    for emp in employee:
        if emp['name'] == name:
            print(f'Employee {name} found in {emp['department']} department with salary {emp['salary']}')
            return
    print(f'Employee {name} not found.')
    return main_menu()

def display_employees():
    print('Employee List')
    sorted_employees = sorted(employee,key=lambda emp: emp['salary'],reverse=True)
    for emp in sorted_employees:
        print(f"Name: {emp['name']}, Department: {emp['department']}, Salary: {emp['salary']}")
    return main_menu()

def remove_employee():
    print('Enter name of the employee to remove')
    name = input()
    for emp in employee:
        if emp['name'] == name:
            print('Enter Y to confirm delete ')
            confirm = input()
            if confirm.upper() == 'Y':
                employee.remove(emp)
                save_employees()
                print(f'Employee {name} removed.')
                return
            else:
                print('Delete cancelled.')
                return
    print(f'Employee {name} not found.')
    return main_menu()

main_menu()    