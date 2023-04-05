# loops

# for loops and foreach loops in other languages

# in python just for loops that you can then specify how you want to loop

list_data = [1,2,3,4,5]
embedded_lists = [[1,2,3],[4,5,6]]
dict_data = {
    1: {"name": "Bronson",
        "money": "$0.05"},
    2: {"name": "Masha",
        "money": "$3.66"},
    3: {"name": "Tasha",
        "money": "$1.14"}

}

#basic loop
#for num in list_data:
    #print(num * 2)

# # nested loop
# for data in embedded_lists:
#     print(data)
#     for num in data:
#         print(num)
# looping for dictionaries

# for value in dict_data"
#    print(value)

for item in dict_data.values():
    print(item)

for item in dict_data.values():
    for embed_value in item.values():
        print(embed_value)

for items in dict_data.values():
    print(items["money"])

for num in list_data:
    if num == 3:
        print("i found three")
    elif num > 3:
        print("iv gone too far")
    else:
        print("too soon")

# while loops

# while loop = monitors a condition

x = 0

while x < 10:
    print(f"its working -> {x}")
    x += 1

# using while loops to verify user input

#age =
#print(f"Your age is {age}")

user_prompt = True

while user_prompt:
    age = input("what is your age")
    if age.isdigit() and int(age) < 117:
        user_promt = False
    else:
        print("please prove your age in digits")

print(f"your age is {age}")

