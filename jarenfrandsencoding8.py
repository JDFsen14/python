"""This program reads in a txt file provided by the professor, scans the lines of text,
and outputs a state and its capitol if they both start with the same letter."""


def state_and_capitol():
    """This function checks if the first letter of the state and capitol city are
    the same letter, and if they are, prints them out."""

    infile = open("StatesANC.txt", encoding="utf-8")

    # Checks each line and gets the state's first letter, while putting all of the info into a list
    for line in infile:
        data = line.split(",")
        letter = data[0][0:1]

        # Checks to see if the first letter of the state is the same as the first
        # letter of the capitol. If it is, it will print both out.
        if data[3].startswith(letter):
            print((data[3].rstrip()) + ", ", data[0])

    infile.close()


def state_check():
    """This function asks the user to input a state and will then output all
    of the information for that state"""

    infile = open("statesANC.txt", encoding="utf-8")
    # Asks the user for the name of a state
    state = input("Please enter the name of a state: ")

    for line in infile:
        data = line.split(",")

        # Checks each line in the file to see if the user input matches one of the state names
        # If it does, print out all information for that state.
        if data[0] == state:
            #print((data[0].rstrip()) + ", " + (data[1].rstrip()) + ", " +
            #      (data[2].rstrip()) + ", " + (data[3].rstrip()))
            print(data)


def state_and_slogan():
    """This creative element function will see if the state has the same beginning letter
    as the state's slogan, and if they do, print both out."""

    infile = open("statesANC.txt", encoding="utf-8")

    # Checks each line and gets the state's first letter, while putting all of the info into a list
    for line in infile:
        data = line.split(",")
        letter = data[0][0:1]

        # Checks to see if the first letter of the state is the same as the first
        # letter of the capitol. If it is, it will print both out.
        if data[2].startswith(letter):
            print((data[2].rstrip()) + ", ", data[0])

    infile.close()


print("Check for state and capitol:")
state_and_capitol()

print("\nCheck for state and slogan:")
state_and_slogan()

print()
state_check()
