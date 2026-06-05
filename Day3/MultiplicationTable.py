print('Enter the number for which you want to see the multiplication table:')
number = int(input())
print('Multiplication Table of', number)
for i in range(1, 11):
    print(number, 'x', i, '=', number * i)
    