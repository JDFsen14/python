"""This program will take in an initial height and
velocity from the user then output the maximum height
the ball reaches and how long the ball takes to land."""
# --------------------------
# Jaren Frandsen
# 03/08/23
# Intro to Python, CS1300
# --------------------------


def isValid(heights, velocities):
    """Checks if the inputted height and velocity values are negative numbers"""
    if heights < 0 or velocities < 0:
        print("Please do not include negative numbers.")
        exit()


def getInput():
    """Gets info of initial height and velocity from user"""
    #Set the variables as global so they can be accessed outside the function
    global height
    global velocity
    global time
    global tempheight
    #Takes input from the user then sets the variables for those inputs
    height = float(input("Please enter an initial height(in feet): "))
    velocity = float(
        input("Please enter an initial velocity(in feet per second): "))
    time = 1.0
    tempheight = 0.01
    #Calls to check if the numbers are negative
    isValid(height, velocity)


#Start of the main part of the function, calls to get user inputs
getInput()

#Cakculates the max height
maxHeight = height + (velocity * (velocity/32)) - (16 * ((velocity/32) ** 2))

#Calculates the amount of time that the ball takes until it hits the ground
while tempheight > 0.0:
    time += 0.1
    tempheight = height + (velocity * time) - (16 * (time ** 2))

#I needed to truncate the time variable because it would add too many zeros at the end
#I truncate it to 1 decimal place because I only calculate every 10th of a second
time = '%.1f' % (time)

#Prints out the max height of the ball and time it takes for the ball to hit the ground
print("The max height of the ball is: " + str(maxHeight) + " feet.")
print("The ball will hit the ground in about " + str(time) + " seconds.")
