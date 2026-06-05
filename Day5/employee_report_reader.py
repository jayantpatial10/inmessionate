with open('employee_report.txt', 'r') as file:
    report_content = file.read() # this will read the entire file as a single string
print(report_content)