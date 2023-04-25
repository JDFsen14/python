"""DOCSITE"""
import sys
import random


def main():
    """The main function, everything starts and comes back here"""

    # Creating initial variables
    my_loop = True
    counter = 0

    # Getting a random number and storing it.
    my_number = random.randint(1, 100)
    print("I've thought of a number between 1 and 100")

    # Uncomment below to cheat the game
    # print("cheat: " + str(my_number))

    # Loop that runs until the player guesses correctly
    while my_loop is True:
        counter += 1
        guess = input("Guess the number: ")
        print(guess_check(guess, my_number))

        # makes sure what the user puts in is a digit.
        # If not, does not run into a type error
        if guess.isdigit() is True:
            if int(guess) == int(my_number):
                my_loop = False
                print("You got it in " + str(counter) + " guesses!")
                break

    # calls the play_again function
    play_again()


def guess_check(my_guess, my_number):
    """This function will check whether your answer is too low,
    too high, not a number, etc."""

    # If statements to check where guessed number is compared to random number
    if my_guess.isdigit() is False:
        return "You did not enter an Integer"
    if int(my_guess) > 100 or int(my_guess) < 1:
        return "Number must be between 1 and 100"
    if int(my_guess) < int(my_number):
        return "Too Low, Try again."
    if int(my_guess) > int(my_number):
        return "Too High, Try again."
    if int(my_guess) == int(my_number):
        return "Correct!"


def play_again():
    """*Creative Element* This function will restart the program if the
    user would like to play again after completing the previous round"""

    # Asks the user if they would like to play again. If yes,
    # restarts main function. Otherwise exits the system.
    again = input("Would you like to play again? (y / n): ")
    if again == "y":
        main()
    sys.exit()


main()

# Thoughts: This was a fun assignment that helped
# reinforce how python works with things like loops,
# if statements, the random class, etc.
