with open('hello.txt', 'r') as file:
    lines = file.readlines()
line_count = len(lines)
print(f'Total Lines: {line_count}')