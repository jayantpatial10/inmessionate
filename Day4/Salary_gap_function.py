def SalaryGap (Current_Salary, Expected_Salary):
    print("Enter Current Salary in Rupees: ")
    current_salary = int(input())
    print("Enter Expected Salary in Rupees: ")      
    expected_salary = int(input())
    gap = expected_salary - current_salary 
    print("The Salary Gap is: ", gap)


SalaryGap(0, 0)    