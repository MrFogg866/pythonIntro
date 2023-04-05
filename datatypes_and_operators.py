# # Numbers, Strings, Booleans
#
# # Numbers = intergers, floats, longs(depreciated), doubles, complex
# # strings = any text "" or ''
# # boolean = True or false
# # a float is a decimal as the decimal can float
#
# # operators
#
# # arithmetic and comparison
#
# # arithmetic
# # + add two variables together
# # * multiplies two variables together
# # / divides two variables
# # % remainder of a division of the left variable by the right variable
#
# # comparison operators
# # > true if the left variable is greater than the right variable
# # < other way round
# # == equal to
# # != true if left variable is greater than or equal to the right
# # >= true if left variable is greater than or equal to the right
# # <= true if left variable is less than or equal to the right
#
# # numeric types
#
# # ints
# #
# # a = 24
# # b = 16
# #
# # print(a + b)
# # print(a - b)
# # print(a > b)
# #
# # # floats
#
#
#
# # input two numbers you want to add
#
# #strings
# #
# # single_quotes = 'loook! single quotes'
# # double_quotes = "look! double quotes"
# #
# # print(single_quotes)
# # print(double_quotes)
# #
# # string_failere = "i said 'wow'"
# # print(string_failure)
# #
# # escape_example = 'i said \'wow\''
# # print(escape_example)
#
# # string slicing
#
# Hw = "hello! world"
#
# print(Hw[-1])
#
# Hw = "hello! world"
#
# print(Hw[1:10])
# print(len[hw])
#
# # h e l l o ! w o r l d
# # 1 2 3 4 5 6 7 8 9 10 11
#
# # string methods
#
# example_text = "heres some text with lots of text"
#
# print(example_text.upper())
# print(example_text.lower())
# print(example_text.count("e"))
# print(example_text.replace("with, ","))
#
# # concatenation
#
# x = 2
# y= 5.4
# z = "theres now a number 24.5 unless we put a space in it"
#
# print(str(x) + " " + str(y) +z)
#
# # f - strings
#
# # python 3.6  onwards, strings that you can bring variables into without casting
#
# name = "lassie"
# years = "7"
# height = "180"
#
# print(f"{name} is {years} year and {height})
#
# # we can use methods in a string using f-strings
#
# name2 = "snoopy"
# age2 = 52
#
# print(f""{name2.upper()} is {age2 *7} YEARS OLD IN DOG YEARS )
#
# pi = 3.14159265359
#
# print(f"Pi to 3 decimal places: {pi:3f}")
# print(f"Pi to 7 decimal places: {pi: 7f}")
#
# score = 16
# max_score = 26

# print(f"you scored {score/max_score}")
# print(f"you scored {score/max_score:%}")
# print(f"you scored {score/max_score:.2%}")
# print(f"you scored {score/max_score:.0%}")


# Booleans

a = True
b = False

print(a == b) # false
print(a != b) # true

print( True and False) # false - both conditions must be true or with be false
print(False and True) # false
print(True and True)  #True

# Booleans with strings

hi = "HelloWorld"

print(hi.isalpha())
print(hi.endswith("d"))