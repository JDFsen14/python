"""This program will open and read the numbers in a file line by line,
then output how many lines there are, the highest number, and the lowest number.
My creative element is that I added the ability for the program to
output the average of all numbers in the .txt file"""


def main():
    """This is the main function of the program and is
    needed so that pylint doesn't get mad at me"""

    # Setting initial variables I will be using
    total = 0
    maximum = -9999999999
    minimum = 9999999999
    counter = 0

    # Opening the file, while specifying that it should encode it with utf-8
    new_file = open('Numbers.txt', encoding="utf-8")

    # For loop that will check the number for each line in the .txt file
    for line in new_file:

        # Adding all numbers together for creative element
        total += int(line)

        # Checks if the current line's value is the largest seen and keeps it
        if int(line) > maximum:
            maximum = int(line)

        # Checks if the current line's value is the smallest seen and keeps it
        if int(line) < minimum:
            minimum = int(line)

        # holds how many lines have been seen for the creative element
        counter += 1

    # print out all of the info kept track of for the program.
    print("Amount of numbers: " + str(counter))
    print("Maximum = " + str(maximum))
    print("Minimum = " + str(minimum))
    print("Sum = " + str(total))
    print("Average = " + str(total / counter))


main()
