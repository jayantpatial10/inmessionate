print('Enter your Salary : ')
salary = float(input())
print('Enter the percentage of your increment :')
increment = float(input())
print('Enter years of projection you want :')
years = int(input())
i=0
while i <years :
    salary += increment * salary / 100
    print(f'Salary in year {i+1} = {salary}')
    i += 1
