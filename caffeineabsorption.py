"""
This code takes the amount of caffeine and uses
equations to show how much caffiene will be in the
body when after every hour 13% of the caffeine is
absorbed into the body
"""

# --------------------------
# Jaren Frandsen
# 02/03/23
# Intro to Python, CS1300
# --------------------------

# Here I declare variables that will keep the amount of caffeine and a counter
caffAmount = 130.0
counter = 0

# Here is the equation to count how many hours it takes to get a caffeine level
# under 65 mg. with an absorption level of 13%
while caffAmount >= 65.0:
    caffAmount *= 0.87
    counter += 1

# Print out the amount of hours it takes to get under 65mg
print("With just one cup, less than 65 mg. will remain after "
      + str(counter) + " hours.")

# Reset the variables for a different calculation
caffAmount = 130.0
counter = 0

# Calculate how much caffeine is in the body after 24 hours
while counter < 24:
    caffAmount *= 0.87
    counter += 1

# Print out how much caffeine is in the body after 24 hours
print("After " + str(counter) + " hours, " + str(caffAmount) +
      "mg. of caffeine is still in the body.")

# Reset the variables for a different calculation
caffAmount = 130.0
counter = 0

# Calculate drinking a cup of coffe every hour
while counter < 24:
    caffAmount *= 0.87
    caffAmount += 130.0
    counter += 1

# Print the hourly cups equation
print("With hourly cups, " + str(caffAmount) +
      "mg. of caffeine is in the body after " + str(counter) + " hours")


# Creative element: How many cups would be toxic?
# fda.gov says that at around 1200mg of caffeine can cause toxic effects like seizures.

# Reset the variables for a different calculation
caffAmount = 130.0
counter = 0

# Drink a cup of coffee every hour until you reach the FDA limit where possible seizures start
while caffAmount < 1200.0:
    caffAmount += 130.0
    counter += 1

# Print out the limit of how many 8oz cups of coffee you should drink at one time
print("Drinking " + str(counter + 1) +
      " cups of coffee in a row will likely cause toxic effects like seizures")
