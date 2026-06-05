print('Enter the initial salary: ')
current_salary = float(input())
print('Enter years of growth: ')
years = int(input())

growth_rate = 0.15

for year in range(1, years + 1):
    current_salary += current_salary * growth_rate
    print(f'Year {year}: Rs. {current_salary:.2f}')

