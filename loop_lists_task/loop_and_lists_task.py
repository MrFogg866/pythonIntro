
# list = ["Hello"]
#
# for x in list:
#     print(x)


import getpass
import time
import sys
print("Welcome " + getpass.getuser() + "...")
time.sleep(0.25)
print("This program, powered by Python, it will ask you to enter names...")
time.sleep(0.5)
print("...once you have finished, enter END to print off your list")
names = ['jake', 'john', 'steve']
while True:
    name = input("Please enter a name: ")
    if name == "END":
        print(names)
        break
    names.append(name)



# for x in range(0, 101):
#     print(x)