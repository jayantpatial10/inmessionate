def calculate_bonus(salary):
    print("Enter your current salary in Rupees: ")
    salary = int(input())
    if salary < 50000:
        bonus = salary * 0.10
    elif salary >= 50000:
        bonus = salary * 0.15    
    print("Your bonus is: ", bonus)

calculate_bonus(0)