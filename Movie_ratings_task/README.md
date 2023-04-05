# :movie_camera: Movie Ratings Task :movie_camera:



### The task is to create a movie rating programe that allows the user to verify if they can watch the movie

## User Stories :paperclip:
- The program should ask the user for their age
- Then the Program should tell them what rated movies they can watch 
- The program should also not let the user enter an incorrect value (ages over 117 and ages under 1)
- Digits only for user input, strings should prompt the user to enter a valid input. (optional)

## Code Snippets :scissors:
 * i have started the program with a print statement and a question for the user to input their age 
```print("Welcome to the movie booking program, what is your age?")```
```age = input()```
 * Then i have created a `if` statement that asks if the customer is equal to or less than 12 they can watch the following movies ```if age.lower() <= "12":
    print("You can watch any movies rated U, PG and 12")```
 * After this i have 2 `elif` statements that provide the user with a response according the their age 

    `elif age.lower() <= "15":
    print("You can watch any movies rated U, PG, 12 and 15")`
    
    -`elif age.lower() >= "18":
    print("You can watch any movies rated U, PG, 12, 15 and 18")`
* And finally there is an `else` statement that returns a error message if the user inputs incorrect data