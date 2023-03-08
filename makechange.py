"""This program will take an amount of cents and give back coins"""
#01/30/2023
#Jaren Frandsen
#CSIS 1300

#Set up the variables for each coin type
quarters = 0
dimes = 0
nickels = 0
pennies = 0

#My creative element was to use while loops for all of the coin countings
#Get the amount of change from the user
moneyAmount = int(input("Enter an amount of money(0 - 99 cents): "))

#Add all of the quarters that will be needed
while moneyAmount >= 25:
    quarters += 1
    moneyAmount -= 25

#Add all of the dimes that will be needed
while moneyAmount >= 10:
    dimes += 1
    moneyAmount -= 10

#Add all of the nickels that will be needed
while moneyAmount >= 5:
    nickels += 1
    moneyAmount -= 5

#Add all of the pennies that will be needed
while moneyAmount >= 1:
    pennies += 1
    moneyAmount -= 1

#Print out all of the coins needed for the change
print("Quarters: " + str(quarters) + ", Dimes: " + str(dimes) + ", Nickels: "
      + str(nickels) + ", Pennies: " + str(pennies))
