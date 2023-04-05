

print("Welcome to the movie booking program, what is your age?")
age = input()

if age.lower() > "117":
    print("Congratulations, you are the oldest person in the world, please contact The Guiness Book Of Records, You can watch any movies rated U, PG, 12, 15 and 18")
elif age.lower() <= "12":
    print("You can watch any movies rated U, PG and 12")
elif age.lower() >= "15":
    print("You can watch any movies rated U, PG, 12 and 15")
elif age.lower() == "18":
    print("You can watch any movies rated U, PG, 12, 15 and 18")
else:
    print("this is not a correct value")