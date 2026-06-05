Employee  = {"John": 50000, "Jane": 60000, "Doe": 45000, "Smith": 55000}

def salary_toolkit(Employee):
    print("Welcome to the Employee Salary Toolkit!")
    print("Please select an option:")
    print("1. Calculate highest salary")
    print("2. Calculate lowest salary")
    print("3. Calculate average salary")
    print("4. Calculate total salary")
    option = int(input())   
    return option

def highest_salary(Employee):
    
    highest = max(Employee.values())
    print("The highest salary is: ", highest)

def lowest_salary(Employee):
    lowest = min(Employee.values())
    print("The lowest salary is: ", lowest)

def average_salary(Employee):
    average = sum(Employee.values()) / len(Employee)
    print("The average salary is: ", average)

def total_salary(Employee):
    total = sum(Employee.values())
    print("The total salary is: ", total)

def main():
    option = salary_toolkit(Employee)    

    if option == 1:
        highest_salary(Employee)
    elif option == 2:
        lowest_salary(Employee)
    elif option == 3:
        average_salary(Employee)
    elif option == 4:
        total_salary(Employee)
    else:
        print("Invalid option selected. Please try again.")   
        salary_toolkit(Employee)  


if __name__ == "__main__":
    main()