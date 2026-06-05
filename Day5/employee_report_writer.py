employees = {
    "John":50000,
    "Jane":60000,
    "Smith":45000
}
with open('employee_report.txt', 'w') as file:
    for name, salary in employees.items():
        file.write(f'{name}: ${salary}\n')
        