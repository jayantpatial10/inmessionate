def salary_input_validator():
    while True:
        print('Enter your Salary:')
        try:
            salary = float(input())
            print(f'Your Salary is: {salary}')
        except ValueError:
            print('Invalid input. Please try again')

salary_input_validator()