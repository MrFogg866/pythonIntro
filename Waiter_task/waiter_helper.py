
# here is the menu variable with string data inside
menu_starters = ["chicken liver parfait", "oysters", "tempura prawns", "buffalo wings", "smoked salmon",]
menu_main = ["Sticky bbq ribs", "seafood paella", "risotto", "geang massaman gai", "udon noodle soup",]
menu_dessert = ["mango and sticky rice", "applepie", "baked alaska"]

# here i tested the variable are working

# print(menu_starters)
# print(menu_main)
# print(menu_dessert)

# here we introduce
print("hello i will be your waiter today, would you like to see the  menu? y/n")
customer = input()

# here the menu is shown

print(menu_starters + menu_main + menu_dessert)

print("what would you like to order?")

customer = input()

print("thank you for your order? would you like me to repeat that back to you y/n")
customer = input()

#print(f"{customer}thank you you have ordered{menu_starters}")







# print(f""{menu_starters.upper()} are the starters available today)
# print(f""{menu_main.upper()} are the mains available today)
# print(f""{menu_dessert.upper()} are the desserts available today)
