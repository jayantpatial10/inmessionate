employees = {
    "John":50000,
    "Jane":60000,
    "Rahul":70000
}
def ask_employee_name():
    name = input("Enter employee name to search: ")
    return name

def search_employee(name):
    print(f"Searching for employee: {name}")
    if name in employees:
        print(f'Employee {name} found with salary: {employees[name]}')
    else:
        print(f'Employee {name} not found.')
        employee_name = ask_employee_name()
        search_employee(employee_name)

employee_name = ask_employee_name()
search_employee(employee_name)
