Employees = {
    "John Doe": 50000,
    "Jane Smith": 60000,
    "Emily Davis": 55000,
    "Michael Brown": 70000,
    "Sarah Wilson": 65000
  }
for employee, salary in Employees.items():
    print(f"{employee}: ${salary}")
highest_sal = -1
for employee, salary in Employees.items():
    if salary > highest_sal:
        highest_sal = salary
        highest_paid_employee = employee

print(f"Highest paid employee: {highest_paid_employee} with a salary of ${highest_sal}")

lowest_sal = float('inf')
for employee, salary in Employees.items(): 
    if salary < lowest_sal:
        lowest_sal = salary
        lowest_paid_employee = employee

print(f"Lowest paid employee: {lowest_paid_employee} with a salary of ${lowest_sal}")

average_sal = sum(Employees.values()) / len(Employees)
print(f"Average salary: ${average_sal:.2f}") 