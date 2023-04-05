def add(num1 , num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    return num1 / num2

def multiply(num1, num2):
    return num1 * num2

choice = int(input('\n Enter 1 for addition and 2 for subtraction and 3 for division or 4 for multiply: '))

num1 = int(input('\n input your first number'))
num2 = int(input('\n input your second number'))

if choice == 1:
    print(num1, '+', num2, '=', add(num1, num2))
elif choice == 2:
    print(num1, '-', num2, '=', subtract(num1, num2))
elif choice == 3:
    print(num1, '/', num2, '=', divide(num1, num2))
elif choice == 4:
    print(num1, '*', num2, '=', multiply(num1, num2))
else:
    print('Invalid option')