# text = 'Hello world'
# words = text.split()
# print(words)

# text = 'This is an altsample text'
# words = text.split()
# print(words)

# data = '90,85,100'
# my_data = data.split(',')
# print(my_data)

# data = 'apple, banana, cherry'
# fruits = data.split(',')
# print(fruits)

# text = 'Python is great for Data Science'
# words = text.split(sep=' ', maxsplit=2)
# print(words)
# word = 'PythonProgramming'
# characters = list(word)
# print(characters)

# print('enter your multiline text')
# lines = []
# while True:
#     line = input()
#     if line.strip().lower() == 'end':
#         break
#     lines.append(line)
# multiline_text= lines
# print(multiline_text)

# multiline_text = ''.join(lines)
# print(type(multiline_text))
# print(multiline_text)


def greet(name):
    print('hello world')

def greet(name):
    print(f'hello word{name}')
greet('john')


def add(a,b):
    return a + b
result = add(1,2)
print(result)

def get_info():
    name = 'je'
    age =10
    return name, age

n,a = get_info()
print(get_info)
print(n,a)

# text = 'Hello world'
# words = text.split()
# print(words)

# text = 'This is an altsample text'
# words = text.split()
# print(words)

# data = '90,85,100'
# my_data = data.split(',')
# print(my_data)

# data = 'apple, banana, cherry'
# fruits = data.split(',')
# print(fruits)

# text = 'Python is great for Data Science'
# words = text.split(sep=' ', maxsplit=2)
# print(words)
# word = 'PythonProgramming'
# characters = list(word)
# print(characters)

# print('enter your multiline text')
# lines = []
# while True:
#     line = input()
#     if line.strip().lower() == 'end':
#         break
#     lines.append(line)
# multiline_text= lines
# print(multiline_text)

# multiline_text = ''.join(lines)
# print(type(multiline_text))
# print(multiline_text)

# def greet(name):
#     print('hello world')

# def greet(name):
#     print(f'hello word{name}')
# greet('john')

# def add(a,b):
#     return a + b
# result = add(1,2)
# print(result)

# def get_info():
#     name = 'je'
#     add =10
#     age = 20
#     return name, age

# n,a = get_info()
# print(get_info)
# print(n,a)


#function with arguments

def print_info(name, age):
    print(f'Name: {name}, Age: {age}')
print_info('John', 30)

def print_numbers(*args):
    for number in args:
        print(number, end = '')

print_numbers(1, 2, 3, 4, 5)
print()
print_numbers(1,2)
print()
print_numbers(10, 20, 30, 40, 50)

print('\n')
def print_data(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')
        
print_data(name='John', age=30, city='New York') 

print('\n')
def multiply(x,y,z):
    return x * y + z
result = multiply(5, 10, 11)
result2 = multiply(2, 3, 4)
print(result, result2)

def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(double, numbers)
print(list(doubled_numbers))


words = ['apple', 'banana', 'cherry']
print(list(map(lambda x: x.upper(), words)))
print(list(filter(lambda x: len(x) > 5, words)))


#lambda function - for one liner (shorter version of using def)
add = lambda x, y: x + y 
result = add(5, 10)
print(result)


multiply = lambda x, y: x * y
result = multiply(5, 10)    
print(result)