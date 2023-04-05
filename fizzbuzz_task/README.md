# `if` Statements Task

## Tasks list 

- 1. Write a program that asks the user for a number. If the number is odd print "The number is odd!" and if it is even print "The number is even".
- 2. Write a program that has a number variable assigned between 1-20. Give the user three guesses to guess the number correctly. Try to give them a clue each time (do they need to go higher or lower?). Make sure to tell them if their guess does not fit in the limitations (1-20). Bonus Make the number to be guessed randomised each time.
- 3. FizzBuzz - Write a program that prints numbers from 1 - 100 but for multiples of 3 print "Fizz" and for multiples of 5 print "Buzz". For multiples of 3 and 5 print "FizzBuzz

## Task 1 

- i have first created the variable `number = input()` which will ask the user for their input, with a message `"Enter a number"`, i have added the `int` class to ensure that the programme only allows the user to input a integer.
- next i create a remainder value to calculate the input number divide by 2 `remainder = number % 2`
- then i create a if statement to calculate if the remainder value can have a zero in then it is a even number ```if (remainder == 0):
    print(number, "is an even number")```
- and finally a else statement for anything else that will be a odd number if the user input number cannot be traced back to zero

## Task 2 