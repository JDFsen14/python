"""This is a program that will check the validity of a user
inputted credit card number"""
# --------------------------
# Jaren Frandsen
# 01/27/23
# Intro to Python, CS1300
# --------------------------


def valid(string):
    """This function will take in a credit card number and check its validity"""
    # Adding all of the extra variables I will need to get through the function
    even = 0
    odd = 0
    temp = 0
    counter = 0

    # Checks every number in the credit card and checks if it is odd or even
    # then does the calculations for odd numbers and even numbers seperately
    for i in string:
        if counter % 2 == 0:
            temp = int(i)*2
            if temp >= 10:
                temp -= 9
            even += temp
            temp = 0

        else:
            odd += int(i)
        counter += 1

    # Checks to see if the odd calculations and the even calculations are divisible by 10
    if (odd + even) % 10 == 0:
        return True
    return False


# Where the main function will actually start, asks the user to input a credit card number
cardNo = str(input("Enter a credit card number: "))

# Checks the length of the number inputted and will call the validity check function
if (len(cardNo) == 14 and valid(cardNo) is True):
    print("The number is valid")
else:
    print("The number is NOT valid")

    # Thoughts: This was a good math exersize to deal with all of the numbers. It was also
    # surprisingly easy to convert the numbers within a string to integers and do math with them
