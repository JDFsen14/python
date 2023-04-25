""" This program is designed to take in a txt file list of
all of the Rose Bowl winners before 2014, count how many
wins each team has, and will print out all of the teams
that have more than 4 total wins. """


def main():
    """Main function, this calls the other functions,
    but everything relays back to this function"""
    rose_bowl_dic = text_to_dic()
    top_teams(rose_bowl_dic)

    # Creative element
    print(team_check(rose_bowl_dic))


def text_to_dic():
    """Opens the file with all of the Rose Bowl information,
    then creates a dictionary that contains each winning
    team's name and counts the wins that each team has."""

    # opens the file, and strips the newlines from each of the lines,
    # putting them into a list.
    infile = open("Rosebowl.txt", encoding="utf-8")
    rose_list = [line.rstrip() for line in infile]
    infile.close()

    # Creates a set we can scan from our initial list
    set1 = set(rose_list)

    # scans the set and for each team, adds a new
    # entry into our dictionary, then counts how
    # many wins each of those teams has.
    rose_dic = {}
    for counter in set1:
        rose_dic[counter] = 0

    for counter in rose_list:
        rose_dic[counter] += 1

    return rose_dic


def top_teams(dic_name):
    """Takes in the dictionary, sorts all of the information
    by how many wins each team has, and then prints out the
    teams with 4 or more wins while showing how many wins
    they have."""

    # Puts our dictionary into a list and sorts it by number of wins.
    list1 = list(dic_name.items())
    list1.sort(key=location, reverse=True)
    print("Teams with 4 or more Rose Bowl\nwins up to the year (for extra credit) 2022:")

    # If a team has more than 3 wins, this for loop will
    # print out the team and their number of wins
    for counter in list1:
        if counter[1] > 3:
            print(" " + counter[0] + ':', counter[1])


def location(k):
    """Returns the spot in the dictionary that
    the sorting algorithm will sort by"""
    return k[1]


def team_check(my_dictionaty):
    """Creative element - asks the user to input a team name,
    then will search the dictionary and print out how many
    wins the searched team name has."""
    list1 = list(my_dictionaty.items())
    my_team = input("Please enter a team name to see their amount of wins: ")

    # checks each spot in the dictionary for the given team name
    for counter in list1:
        if counter[0] == my_team:
            string1 = " " + str(my_team) + " has " + str(counter[1]) + " wins."
            return string1
    return " Team not found/has not won a Rose Bowl"


main()

# With this program, I learned how useful dictionaries can be.
# Based on what I learned from other programming classes, dictionaries
# can be used as simplified versions of 2-dimentional arrays.
