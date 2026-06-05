with open('hello.txt', 'r') as file:
    content = file.read() # this will read the entire file as a single string
word_count = len(content.split()) # split the content into words and count them
print(f'Total Words: {word_count}')