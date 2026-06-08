employees = [
    {"name":"John","department":"IT","salary":50000},
    {"name":"Jane","department":"HR","salary":60000},
    {"name":"Rahul","department":"IT","salary":70000}
]

def department_summary():
    for employee in employees:
        print(f"Employee {employee['name']} works in {employee['department']} department.")

department_summary()        