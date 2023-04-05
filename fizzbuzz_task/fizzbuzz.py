# this is the code for checking if a number is odd or even
number = int(input("Enter a Number"))
remainder = number % 2

if (remainder == 0):
    print(number, "is an even number")

else:
    print(number, "is a odd number")

# this is the code to guess a random number
import random

flag = True
while flag:
    num = input("type a number for your required range upto 20: ")

    if num.isdigit():
        print("Lets play")
        num = int(num)
        flag = False
    else:
        print("Invalid input! Try Again")

secret = random.randint(1, num)

guess = None
count = 1

while guess != secret:
    guess = input("please type a number between 1 and " + str(num) + ": ")
    if guess.isdigit():
        guess = int(guess)

    if guess == secret:
        print("you got it")
    else:
        print("please try again")
        count +- 1

print('it took you', count, 'guesses!')

r = random.randint(1, 20)
print(r)