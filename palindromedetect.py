"""This is a program that will ask the user for a phrase
and compare it to itself, but backwards to see if it
is the same forwards and backwards(known as a palindrome)"""
# --------------------------
# Jaren Frandsen
# 01/27/23
# Intro to Python, CS1300
# --------------------------


def check_palindrome(string):
    """This function takes in a string, replaces spaces, punctuation, and makes everything lowercase
    to compare it to itself backwards"""
    string = string.lower().replace(' ', '').replace("'", "").replace(
        '.', '').replace('?', '').replace('!', '').replace(',', '').replace(
        ':', '').replace(';', '').replace('"', '')
    return string == string[::-1]


def has_numbers(string):
    """This function will check and see if the string has any numbers in it"""
    return any(char.isdigit() for char in string)


# Takes in a phrase from a user and sends it to a function to check if it is a palindrome
phrase = input("Enter a phrase without numbers to check for a palindrome: ")
answer = check_palindrome(phrase)

# My creative element is to check and see if the phrase has any numbers in it.
# If it does, end the function and tell the user to try again
if has_numbers(phrase):
    print("Please type in a phrase that does not contain numbers")
    exit()

# The code will then tell you whether your phrase is a palindrome or not.
if answer:
    print(phrase + " is a palindrome!")
else:
    print(phrase + " is NOT a palindrome!")

# Thoughts: I learned that an easy way to read a string backwards
# is to use the command: string[::-1]. This was a cool and easy way to
# compare the regular string to itself, but read backwards.
