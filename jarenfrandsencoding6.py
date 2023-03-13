"""This program will take a word or sentance
from the user and check each 3 letters in a
row of the phrase to see if the 3 letters are
ordered in alphabetical order"""
# --------------------------
# Jaren Frandsen
# 03/08/23
# Intro to Python, CS1300
# --------------------------


def isTripleConsecutive(phrase, min_length=3):
    """This function takes in the inputted word or
    phrase and checks if 3 of the letters are consecutive"""

    # Check if the length of the phrase the user inputted
    # is at least 3 letters long. If it is not, call an error.
    length = len(phrase)
    if length < min_length:
        raise ValueError(
            "String too short to contain repetition of length {}".format(min_length))

    for i in range(length-2):

        # Check if you get the same letter by subtracting 1 or 2 to the next ones
        if ord(phrase[i]) == ord(phrase[i+1])-1 == ord(phrase[i+2])-2:
            return "'" + phrase[i:i+3] + "' is 3 consecutive letters within your phrase"

        # Creative element:
        # Checks to see if 3 letters are consecutive in REVERSE alphabetiacl order
        if ord(phrase[i]) == ord(phrase[i+1])+1 == ord(phrase[i+2])+2:
            return "'" + phrase[i:i+3] + "' is 3 consecutive letters in reverse within your phrase"

    # If no 3 letters are consecutive, output to the user
    # that there are not 3 consecutive letters
    return "There are not 3 consecutive letters."


# Take input for the user
testword = input("Please enter a word: ")

# Call the function to check if letters are
# consecutive and print out the return statement it gives
print(isTripleConsecutive(testword))

# Thoughts: The 'ord' function is incredibly useful
# for this kind of program, as it has built in the
# alphabetical order for letters, and lets you check
# the order of letters whenever you would like
