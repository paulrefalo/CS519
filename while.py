# CS 519 assignment 2 - Fizz Buzz with while loop by Paul ReFalo

number = int(input("Enter a number: ")) # get user input

i = 1                                   # seed increment variable 'i' with value of 1

while i <= number:
    if (i % 3) and (i % 5):             # has remainder for div by 3 and div by 5
        print(i)
    elif (i % 3) or (i % 5):            # evenly divisible by 3 or 5
        if (i % 3):                     # evenly divisible by 5
            print(str(i) + " Buzz")
        elif (i % 5):                   # evenly divisible by 3
            print(str(i) + " Fizz")
        else:
            print("This shouldn't happen")
    else:                               # must be evenly divisible by both 3 and 5
        print(str(i) + " Fizz Buzz")
    i += 1

print("Done!")



'''
import platform

print("You are running Python version %s." % platform.python_version())
user = input("What is your name? ")
currentAge = input("How old are you now? ")
retirementAge = input("How old will you be when you retire? ")
currentlySaved = input("How much have you saved for retirement? ")
annualSavings = input("How much are you saving per year? ")
savings = int(currentlySaved) + (int(retirementAge) - int(currentAge)) * int(annualSavings)
print(user + ", you will have $" + str(savings) + " if you keep saving at the current rate.")
'''

# Example output
'''
You are running Python version 3.5.1.
What is your name? Paul ReFalo
How old are you now? 48
How old will you be when you retire? 70
How much have you saved for retirement? 42000
How much are you saving per year? 500
Paul ReFalo, you will have $53000 if you keep saving at the current rate.
'''