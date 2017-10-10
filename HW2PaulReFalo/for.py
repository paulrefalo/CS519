# CS 519 assignment 2 - Fizz Buzz with for loop by Paul ReFalo

number = int(input("Enter a number: ")) # get user input

for i in range(1, number + 1):
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


